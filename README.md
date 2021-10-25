# Atmoshperic Space Interactions Monitor (ASIM)

Matching ASIM information to the TASD data

There are two types of searches that need to be done for the ASIM matching:

1. MMIA vs TASD (uses python files)
2. TGF & Lightning vs TASD (by hand)

## First steps:

1. Run the file *RUN_ME_FIRST.py*
2. Check to make sure that directories *Data*, *ASIMData*, *TASDData*, and *TASDDataUpdate* have been created.
3. run: *pip install -r requirments.txt*
4. Register an account on this website to get ASIM information: https://asdc.space.dtu.dk/
	- This may take 1-5 business days to get registered, so give yourself ample time to do so!

##  Get data

1. Data should be housed on tasdserv, but as of now data is acquired through Rasha, Joe, or Hans
2. The files for ASIM data are sorted on a year to year basis and further sorted by day. This data comes in 4 columns: *Event Time*, *ISS Latitude*, *ISS Longitude*, and *TLE*
	- Only Rasha has permission to take these files from the ASDC website
3. The files for the TASD data are found as *sd_timestamp* files, and may be found on tasdserv under */pool02/mdproc2-mdproc2/dm-5/jackson/sd_time_stamp*. The files here may not be current, confirm with Hans or Joe
	- Before, we were using timestamps that only contained 3 colums for times. These files go into the *Data/TASDData* folder.
	- We now use 15 column timestamp files. There is a place in the code to switch between the two. These files go into the *Data/TASDDataUpdate* folder

# Search

## MMIA vs TASD

1. Go to the *match.py* file
2. Set the parameters and run
3. Once completed, the output file should be listed in the *TimeMatch* directory as *MatchedLocations.txt*

In order to conduct the search, edit the *timeDiff* parameter and *locdelta* parameter.
 	- We would like to see a time correlation on the scale of milleseconds, but this has not happened 
	- *locdelta* should be taken to be measured above the TASD, but lightning is capable of traveling 40 km so paremeter is set to size of SD (700 km radius) + 40 km = 740 km default

## TGF & Lightning vs TASD

Becuase the lists given from the ASDC website are so short, we can conduct this search by hand

1. Go to the ASDC website and use your credentials to log in
2. At the top of the page, click on Data/MXGS Triggers
3. Select *Instrumental TGF Search Mode* in "Instrument Mode"
4. Choose Level 1
5. Choose the appropriate Longitude and Latitude. I have been using the following
	- Longitude start: -115
	- Longitude finish: -110
	- Latitude start: 36
	- Latitude finish: 40
6. Choose the appropriate date range. This range can span multiple months

The output should list data of MMIA, HED, and LED trigger types. HED and LED come from MXGS, 
	- MMIA detects Transient Luminous Events (TLEs), which are flashes of light that occur in the stratosphere and mesosphere above active thunderstorms. 
		- These are known as sprites, blue jets, pixies, and trolls
		- https://www.skybrary.aero/index.php/Transient_Luminous_Events_(TLEs)#:~:text=8%20Further%20Reading-,Description,and%20Cumulonimbus%20(Cb)%20clouds.
	- HED = High Energy Detector
	- LED = Low Energy Detector

	- MXGS = https://link.springer.com/article/10.1007/s11214-018-0573-7
	- MMIA = https://link.springer.com/article/10.1007/s11214-019-0593-y

7. Compare to the *.dat* files in *TASDData* or *TASDDataUpdate*

This concludes the TGF search. In order to search for Lightning correltaion vs TASD, perform the following steps:

8. If you are still signed in, click on Data/Lightning Data
9. Select *Lightning* in "Observation Type"
10. Repeat steps 4-7

