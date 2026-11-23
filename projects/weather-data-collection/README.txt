Brian Saville
November 23, 2026

~WEATHER DOWNLOADER: README~

PROJECT GOAL: Gather weather data for each field sampling event by querying the Meteostat API for the nearest weather station.


HOW TO USE

Input: CSV with the following columns:
	site		name of each site. Can be anything.
	address		the address of each site. Make sure they're consistent.
	method		either net/bowl. Relevant to my work, and used in the script because I downloaded weather a bit differently for each.
	date		date on which collection occurred.
	start		time that collection began. 13:00 format.
	end		time that collection concluded. 13:00 format.


SCRIPTS

1.  weather.collection.py	Master Weather Downloader

This is the script that makes everything happen. Here's roughly how it's done:
	- weather_collection reads the CSV to a dataframe.
	- timestamp_add function converts all date/time to timestamp objects.
	- bowl_date function adjusts the date for bowl events (because they take place over 24 hours).
	- get_lat_long_all function adds latitude and longitude for each unique site. 
		- uses Nominatim to gather coordinates
		- looks up unique addresses to avoid grabbing the same coordinates more than once. 
	-station_all function determines the nearest weather station for each site
	
	-for each row, adds mean temperature, mean relative humidity, max wind speed, and total precipitation for the given timeframe:
		- downloads weather using meteostat
		- truncates this down to just the four desired metrics
		- adds mean_temp, mean_rhum, max_wpsd, and total_prcp to the dataframe. 

Output: CSV like the initial, but with mean_temp, mean_rhum, max_wspd, and total_prcp added to each row.