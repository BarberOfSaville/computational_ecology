#Brian Saville
#August 26th, 2026

#The Moment of Truth!
#Attempt to use my iNat code to generate the Bee Dex.

from inat_download_function import inat_download
from inat_list_function import inat_list
from pathlib import Path
from inat_merge import inat_merge

#Establish project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

#Establish data directory
DATA_DIR = PROJECT_DIR / "data" / "intermediate"


#Download Manhattan bee data
nyc_bee_params = {
    "taxon_id": 630955,
    "quality_grade": "research",
    "place_id": 1264,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on",
    "rank" : "species"
}

citybees = inat_download(nyc_bee_params)
inat_list(citybees, "manhattan_bees")

#Download Bronx bee data
bronx_bee_params = {
    "taxon_id": 630955,
    "quality_grade": "research",
    "place_id": 1189,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on",
    "rank" : "species"
}

bxbees = inat_download(bronx_bee_params)
inat_list(bxbees, "bronx_bees")

#Merge Manhattan and Bronx bee data into one sheet
file1 = DATA_DIR / "mbees.csv"
file2 = DATA_DIR / "bxbees.csv"
filename = "m_bx_bees"

merged_df = inat_merge(file1, file2, filename)




