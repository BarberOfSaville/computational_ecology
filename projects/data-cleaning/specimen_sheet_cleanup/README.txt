Brian Saville
November 23, 2026

~PROJECTS: SPECIMEN SHEET CLEANUP: README~

The goals of this project are three-fold:
	1. Expand specimen data so that every individual bee has a row, not just every capture
	2. Merge weather data added to collections data with specimen data
	3. Clean up and compile specimen/collections data into one sheet for further use, removing unnecessary fields


SCRIPTS

1. specimen_sheet_expand.py	Specimen Sheet Expand & Cleanup 

This script takes two CSVs: one of my summer bee collection events, and one of my specimens collected on said events, and merges relevant info into one dataframe, outputting this as a new CSV.

The specimens sheet details each netting and pan-trapping event that occurred during each collection event. The specimen sheet has a column for "number of specimens", indicating how many bees were collected per flower per event (netting) or per bowl (pan trapping). This script delivers a CSV with a row for every individual SPECIMEN, and so expands a row listing 5 collected bees into 5 separate rows.

The two sheets are merged by their date and time columns. The collections sheet contains weather data that was added using my Weather Download scripts-- see the weather_download project to find these. 

The outputted sheet will be used going forward as individual bees are pinned and identified.


FUNCTIONS

1. filename_datetime.py		Unique Filename Generator

This function takes a generic output filename and appends the date and time to the end of it, ensuring that no files written to the output folder are overwritten. 



COLUMNS OF INPUT CSVs:

	Specimen Sheet
		ID
		Status?
		location
		Temp ID
		Site
		Date Collected
		Time Collected
		# of Bees (used to determine number of duplicate rows to add to output)
		Method
		Plant
		Description
		
	Collections Sheet
		site
		address
		method
		date
		start
		end
		start_dt
		end_dt
		weather_start_dt
		latitude
		longitude
		station
		mean_temp
		mean_rhum
		max_wspd
		total_prcp


COLUMNS OF OUTPUT CSV:
	
	ID_no 		blank, to be filled in later
	prelim_id 	blank, to be filled in later
	old_ID_no 	from Specimen Sheet ID
	status 		from Specimen Sheet Status?
	location 	from Specimen Sheet location
	site 		from Specimen Sheet Site
	date 		from Specimen Sheet Date Collected
	time 		from Specimen Sheet Time Collected
	method 		from Specimen Sheet Method
	plant 		from Specimen Sheet Plant
	notes 		from Specimen Sheet Description
	mean_temp 	from Collections Sheet mean_temp
	mean_rhum 	from Collections Sheet mean_rhum
	max_wspd 	from Collections Sheet max_wspd
	total_prcp 	from Collections Sheet total_prcp