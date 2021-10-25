# Functions to analyze sorted TASD19 Data
from datetime import *
import numpy as np


class sTASD19:
    
    def __init__(self, name):
        self.name = name
        
    def datetimeArray(self):
        data = []
        f = open('C:/ASIM/TimeMatching/Data/TASDData_sorted.txt', 'r')
        for line in f:
            columns = line.split(' ')

            temp1 = columns[0].split('-')
            temp2 = columns[1].replace('.', ':').split(':')
            data.append(datetime(int(temp1[0]),
                                 int(temp1[1]), 
                                 int(temp1[2]),
                                 int(temp2[0]),
                                 int(temp2[1]),
                                 int(temp2[2]),
                                 int(temp2[3])))
            
        f.close()
        return np.array(data)
