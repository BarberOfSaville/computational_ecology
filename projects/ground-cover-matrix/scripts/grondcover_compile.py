#Brian Saville
#September 17th, 2026

#Compile ground cover data collected previously for 
#individual gardens into one CSV.

#CSVs to be read should be placed in data/groundcover_input.
#Designed to read CSVs as formatted by groundcover_test.

from pathlib import Path
import pandas as pd
from filename_datetime import filename_maker
from pathlib import Path

#Establish project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

#Establish data directory
DATA_DIR = PROJECT_DIR / "data" / "intermediate"

#Set directory where input data will be found
folder = DATA_DIR

#Create master dataframe
master_df = pd.DataFrame(
    columns=["garden", "area (sqm)", "vegetable", "flower", "wild",
             "lawn", "soil", "impervious", "mulch", "shannon",
             "simpson"]
)


#loop through files, adding desired data to master dataframe
row = 0
for csv_file in folder.glob("*.csv"):
    df = pd.read_csv(csv_file)

    master_df.loc[row, "garden"] = df.columns[0]
    master_df.loc[row, "area (sqm)"] = df.iloc[7,3]
    master_df.loc[row, "vegetable"] = df.iloc[0,3]
    master_df.loc[row, "flower"] = df.iloc[1,3]
    master_df.loc[row, "wild"] = df.iloc[2,3]
    master_df.loc[row, "lawn"] = df.iloc[3,3]
    master_df.loc[row, "soil"] = df.iloc[4,3]
    master_df.loc[row, "impervious"] = df.iloc[5,3]
    master_df.loc[row, "mulch"] = df.iloc[6,3]
    master_df.loc[row, "shannon"] = df.iloc[0,4]
    master_df.loc[row, "simpson"] = df.iloc[0,5]

    row += 1

#Export master csv
file = "_garden_summary"
new_filename = filename_maker(file) + ".csv"
master_df.to_csv(PROJECT_DIR / "outputs" / new_filename, index=False)
print("Output saved as " + new_filename + ".csv.")
