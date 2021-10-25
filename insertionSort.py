# Takes 60-80 mins to run over current data library

# Initialization
from datetime import *
from TASD19 import TASD19
import numpy as np
import glob

pathTASD = 'C:/ASIM/TimeMatching/Data/TASDData/**/*.dat'
# test on smaller file to see if it's working
#pathTASD = 'C:/ASIM/TimeMatching/Data/TASDData/TASD18_030_sd_timestamp.dat'
TASDData = np.array([])

for file in glob.glob(pathTASD, recursive=True):
    TASDData = np.concatenate((TASDData, TASD19.datetimeArray(TASD19(file))))
    
# TASDData encompases all data files compiled into one zone for analysis
#print([TASDData])

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6] 

insertionSort(TASDData)

# removes duplicate values
resTASDData = []
for x in TASDData:
    if x not in resTASDData:
        resTASDData.append(x)
        
        
f = open('C:/ASIM/TimeMatching/Data/TASDSorted.txt', 'w')
for i in range(len(resTASDData)): 
    #print ("% d" % TASDData[i]) 
    f.write(("%s\n" % resTASDData[i]))
    #f.write("%m/%d/%Y, %H:%M:%S.%f")
    #f.write('\n')

f.close()