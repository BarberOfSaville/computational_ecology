#Brian Saville
#August 7th, 2026
#Function to make a species list CSV from downloaded iNat data.

from collections import Counter
import pandas as pd
from filename_datetime import filename_maker
from inat_index_function import inat_index
import time
from pathlib import Path

#Establish project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

#Establish data directory
DATA_DIR = PROJECT_DIR / "data" / "intermediate"

#Establish output directory
OUTPUT_DIR = PROJECT_DIR / "outputs"


def inat_list(observations, filename):
    """Generates a species list CSV from downloaded iNaturalist data."""

    #collapsing the species into a checklist
    species = set()

    for obs in observations:
        if obs["taxon"]["rank"] == "species":
            species.add(obs["taxon"]["id"])

    #count observations per species
    species_counts = Counter()

    for obs in observations:
        if obs["taxon"]["rank"] == "species":
            species_counts[obs["taxon"]["id"]] += 1

    #Converting this count into a table
    species_df = pd.DataFrame(
        species_counts.items(),
        columns=["id", "observations"]
    )

    #Add species info
    for i, taxon_id in enumerate(species_df["id"]):

        species_info = inat_index(taxon_id)

        species_df.loc[i, "common_name"] = species_info.get("common_name")
        species_df.loc[i, "scientific_name"] = species_info.get("scientific_name")
        species_df.loc[i, "genus"] = species_info.get("genus")
        species_df.loc[i, "family"] = species_info.get("family")
        species_df.loc[i, "order"] = species_info.get("order")

        if species_info["common_name"] is None:
            print("Added info for " + species_df.loc[i, "scientific_name"])
        else:
             print("Added info for " + species_df.loc[i, "common_name"])
             
    time.sleep(1)

    #Sorting that dataframe
    species_df = species_df.sort_values(
        by="Observations",
        ascending=False
    )

    new_filename = filename_maker(filename) + ".csv"

    location = OUTPUT_DIR / new_filename

    #Exporting the dataframe
    species_df.to_csv(location, index=False)

    print("Species list exported as " + new_filename + ".csv")
