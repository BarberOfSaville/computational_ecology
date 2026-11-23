#Brian Saville
#November 11th, 2026

#A completed script for expanding my specimen data sheet
#to include a row for each individual collected. 
#This can then be joined to pinned specimen data.

#import libraries
#import libraries and functions
from pathlib import Path
import pandas as pd
from filename_datetime import filename_maker
from datetime import datetime

#Establish project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

#Establish data directory
DATA_DIR = PROJECT_DIR / "data" / "raw"

#Establish output directory
OUTPUT_DIR = PROJECT_DIR / "outputs"

#load in the input CSV
#Set directory where input data will be found
file = DATA_DIR / "specimens_sum26.csv"

#open the old dataframe
old_df = pd.read_csv(file)
old_df["# of Bees"] = old_df["# of Bees"].fillna(0).astype(int)

#create new dataframe
new_df = pd.DataFrame(columns = old_df.columns)

#add rows for each individual bee from each specimen collecting event
for index, old_row in old_df.iterrows():
    numbees = int(old_row["# of Bees"])
    for i in range(numbees):
        new_df.loc[len(new_df)] = old_row

#Add new columns for ID number and preliminary species identification
new_df.insert(0, column ="prelim_id", value = "")
new_df.insert(0, column ="ID_no", value = "")

#rename the existing columns
new_df = new_df.rename(columns= {"ID" : "old_ID_no",
                                 "Status?" : "status",
                                 "Temp ID" : "temp_ID_no",
                                 "Site" : "site",
                                 "Date Collected" : "date",
                                 "Time Collected" : "time",
                                 "# of Bees" : "bee_count",
                                 "Method" : "method",
                                 "Plant" : "plant",
                                 "Description" : "notes"})

#convert date to the proper datetime format
new_df["date"] = pd.to_datetime(new_df["date"], errors="coerce")
print(new_df["date"].dtype)

#merge with the collection events csv
collections = pd.read_csv(DATA_DIR / "collection_events_sum26.csv")

#put end time in the start column for collections (to ensure that the join uses the correct time)
#a little inelegant, but a quick fix for what I needed it to do
collections.loc[collections["method"] == "bowl", "start"] = collections["end"]

#grab desired columns from collections dataframe
collection_subset = collections[["date", "start", "mean_temp", "mean_rhum",
                                "max_wspd", "total_prcp"]]
#convert date to the proper datetime format
collection_subset["date"] = pd.to_datetime(collection_subset["date"], errors="coerce")


#Merge collections and specimens dataframes by date and time
merged_df = new_df.merge(collection_subset,
                         left_on = ["date", "time"],
                          right_on = ["date", "start"],
                           how = "left" )

#Remove redundant columns and fill in n/a for bowl specimen plants
merged_df = merged_df.drop(["start", "temp_ID_no", "bee_count"], axis = 1)
replace = {"plant" : "n/a"}
merged_df = merged_df.fillna(value = replace)

#Export new sheet as a csv with a unique filename
file = "new_spec_sheet_sum26"
new_filename = filename_maker(file) + ".csv"
merged_df.to_csv(OUTPUT_DIR / new_filename , index=False)
print("Output saved as " + new_filename)