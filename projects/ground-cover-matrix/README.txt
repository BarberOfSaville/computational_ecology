Brian Saville
November 23, 2026

~PROJECTS: GROUND COVER- README~

The purposes of this project:
	1. measure and analyze ground-cover data from inputted matrices
	2. create appealing visualizations of ground-cover matrices
	3. compile analyses of multiple sites into one file for comparison and further analyses

SCRIPTS

1. ground_analysis.py	Ground Cover Analysis
	
	This script takes a text file containing a ground-cover matrix and outputs a CSV containing the number of grid spaces, area, and percent of area each of several ground cover types takes up, as well as the Shannon and Simpson diversity indices measured as if each ground cover type were a "species". 


2. ground_visual.py	Ground Cover Visualization 

	This script takes a text file containing a ground cover matrix and outputs a PNG showing a visualization image, with each grid space represented by a colored square. The X and Y axes show the length and width of the site, in meters.


3. groundcover_compile.py	Ground Cover Analysis Compilation

	This script takes multiple CSVs outputted by ground_analysis.py and returns a CSV compiling the info from each into one easy-to-read table. Input CSVs should be placed in the data / intermediate folder.


FUNCTIONS

1. diversity_function.py	Diversity Index Calculator
	
	Called by ground_analysis.py to measure Shannon and Simpson diversity indices for a site.

2. filename_datetime.py 	Unique Filename Generator

	This function takes a generic output filename and appends the date and time to the end of it, ensuring that no files written to the output folder are overwritten. 
	


INPUT MATRICES

Input matrices for ground_analysis.py and ground_visual.py represent field surveys of research sites. Each character in the matrix represents a 2m x 2m area. Each grid space has been assigned one of several ground cover types, chosen for their relevance to bee nesting and/or foraging. 

This ground cover types could be adjusted to suit other projects. Input matrix files can contain additional notes after the matrix-- matrix reading ends after a line break. 

Ground Cover Types:
	x	n/a (used when site area is not a perfect square)
	V	vegetable growth
	F	floral growth
	W	wild growth (weeds/wildflowers)
	L	lawn
	S	soil
	I	impervious surface
	M	mulch/woodchips
	A	water

Example Input Matrix:

FSIFMSVVVVVSMV
FIIMMVVVVMFFWW
MMMMVVVVVMFFMW
IMMMVVVVVMFFFV
IMMMVVVMMVMFFV
SMMMMVVMVVSFFV
FFFFMMMVMSWFFV
IIIIIISMVFWFFI

	