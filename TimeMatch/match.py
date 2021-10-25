from datetime import *
from ASIM import ASIM
from TASD19 import TASD19
from sTASD19 import sTASD19
import numpy as np
import glob
from geopy.distance import geodesic

from mpl_toolkits.basemap import Basemap
#from PIL import Image
import matplotlib.pyplot as plt



# change timedelta([...]=#) for time manipulation
# hours=24, minutes=60, seconds=1, etc.
timeDiff = timedelta(hours=24)
TASDData = np.array([])
TASDDataUpdate = np.array([])
sTASDData = np.array([])
ASIMData = np.array([[]]).reshape(0, 2)
events = []
matches = []
# original TASDLocation = (39.29693, 112.90875)
TASDLocation = (39.28854, 111.60643)
pathTASD = 'C:/ASIM/TimeMatch/Data/TASDData/**/*.dat'
pathTASDUpdate = 'C:/ASIM/TimeMatch/Data/TASDDataUpdate/**/*.dat'
pathASIM = 'C:/ASIM/TimeMatch/Data/ASIMData/**/*.txt'

# file sorted via insertionSort.py 
sortedTASDData = 'C:/ASIM/TimeMatch/Data/TASDData_sorted.txt'

# location parameter from TASDLocation (center of TASD)
# in kilometers
locdelta = float(740)


# returns true if an event is within locdelta = float(...) km of the TASDLocation
# uses geodesic
def similarLocation(ASIM):
    if geodesic(ASIM, TASDLocation).km <= locdelta:
        return True
    else:
        return False

'''
# Takes an array and outputs a numpy array of burst events
def getBursts(array):
    data = []
    diff = np.diff(np.array(array))
    
    for i in range(0, len(diff)):
        #difference i <= i+1 a millisecond = burst TRUE
        if abs(diff[i]) <= timedelta(milliseconds=1):
            burst = True
            #startIndex = "first instance" of burst
            startIndex = i
            while burst:
                i = i + 1
                if diff[i] > timedelta(milliseconds=1):
                    burst = False
                    # i - 1 ?
                    for j in range(startIndex, i + 1):
                        data.append(array[j])
    return np.array(data)
'''

def getBursts(array):
    firstEvents, allEvents, temp = [], [], []
    burst = False
    #diff = function call for np library
    differences = np.diff(np.array(array))
    
    #diff now is a timedelta 
    for i, diff in enumerate(differences):
        #difference i <= i+1 a millisecond = burst TRUE
        #within a burst
        #bursts are typically taken with milliseconds=1
        if abs(diff) <= timedelta(milliseconds=1) and burst:
            temp.append(array[i])
        #starting a burst
        elif abs(diff) <= timedelta(milliseconds=1):
            firstEvents.append(array[i])
            temp.append(array[i])
            burst = True
        #ending a burst
        elif burst:
            temp.append(array[i])
            allEvents.append(temp)
            temp = []
            burst = False
    #checking if last instance is within a burst 
    if burst:
        temp.append(array[i+1])
        allEvents.append(temp)
            
    return np.array(allEvents), np.array(firstEvents)

# Returns the distance between the ASIM event and the TASD
def distanceToTASD(event):
    #print(event)
    location = (event[1][0], event[1][1])
    return geodesic(location, TASDLocation).km
    

# If using TASDDataUpdate, switch accordingly

for file in glob.glob(pathTASD, recursive=True):
    TASDData = np.concatenate((TASDData, TASD19.datetimeArray(TASD19(file))))

'''    
for file in glob.glob(pathTASDUpdate, recursive=True):
    TASDDataUpdate = np.concatenate((TASDDataUpdate, TASDUpdate.datetimeArray(TASDUpdate(file))))
'''

# If using sorted list, uncomment the lines for sTASDData   
''' 
for file in glob.glob(sortedTASDData, recursive=True):
    sTASDData = np.concatenate((sTASDData, sTASD19.datetimeArray(sTASD19(file))))
'''

for file in glob.glob(pathASIM, recursive=True):
    ASIMData = np.concatenate((ASIMData, ASIM.datetimeLocationArray(ASIM(file))))

allEvents, firstEvents = getBursts(TASDData)

# Get Location Matched Data and store in "events"
#for m in TASDbursts:
for n in ASIMData:
    if similarLocation(n[1]):
        events.append(n)



#-----------------------------------------------------------------------#
#                                                                       #
#                        Write data file                                #
#                                                                       #
#-----------------------------------------------------------------------#

f = open('MatchedLocations.txt', 'w')
f.write('TASD')
for i in range(0, 6):
    f.write('\t')
f.write('ASIM')
f.write('\n')
#for TASDtime in firstEvents/allEvents
for TASDtime in allEvents:
    for match in events:
        #if abs(match[0] - TASDtime) <= timeDiff: 
        if abs(match[0] - TASDtime[0]) <= timeDiff:
            # for every instance of TASDtime, make TASDtime == TASDtime[0] for allEvents
            f.write(TASDtime[0].strftime("%m/%d/%Y, %H:%M:%S.%f"))
            f.write('\t\t')
            f.write(match[0].strftime("%m/%d/%Y, %H:%M:%S.%f"))
            f.write('\n')
            f.write("Time Difference: " + str(abs(match[0] - TASDtime[0])) + " (H:M:S.f)")
            f.write("\nASIM Distance to TASD: " + str(distanceToTASD(match)) + " kilometers")
            f.write('\n')
            # take this out for firstEvents
            f.write("Number of bursts: " + str(len(TASDtime)))
            f.write('\n\n')
            
            #print(match[1])
            
            
            #f.write("\nallEvents: " + str(allEvents) + " (H:M:S.f)")
            #f.write('\n')
            
            
            #print(len(TASDtime))
            #print(TASDbursts)
            
            
            #x = str(abs(match[0] - TASDtime))
            #y = str(distanceToTASD(match))

            #plt.scatter(x, y, alpha=0.5)
            #plt.show()
            
f.close()


#-----------------------------------------------------------------------#
#                                                                       #
#                        Mapping and plot                               #
#                                                                       #
#-----------------------------------------------------------------------#


'''
#map = Basemap(llcrnrlon=3.75,llcrnrlat=39.75,urcrnrlon=4.35,urcrnrlat=40.15, epsg=5520)
map = Basemap(width=30000000,height=22500000,projection='lcc',
            resolution=None,lat_0=39.29693,lon_0=-112.90875)
#map.bluemarble()
#map.shadedrelief()
#map.drawstates(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)

20.3642249066446, 120.933789516621

lon = [-120.933789516621, -120.961442138364, -112.90875]
lat = [20.3642249066446, 20.3318006988992, 39.296930] 
xpt,ypt = map(lon,lat)
lonpt, latpt = map(xpt, ypt ,inverse=True)
map.plot(xpt, ypt, 'mo')


lats, lons = 40.6895811020007, -114.626819740824
xp, yp = map(lons, lats)
lonsp, latsp = map(xp, yp, inverse=True)
map.plot(xp, yp, color='b')




plt.show()
'''