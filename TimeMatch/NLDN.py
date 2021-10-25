# Functions to analyze NLDN Data
from datetime import *
import numpy as np


class NLDN:

    def __init__(self, name):
        self.name = name

    def datetimeArray(self):
        data = []
        f = open(self.name, 'r')
        for line in f:
            columns = line.split()
            
            temp1 = columns[0].split("-")
            temp2 = columns[1].replace('.', ':').split(":")
            
            temp2[3] = temp2[3][:-3]
            
            
            data.append(datetime(int(temp1[0]),
                                 int(temp1[1]), 
                                 int(temp1[2]),
                                 int(temp2[0]),
                                 int(temp2[1]),
                                 int(temp2[2]),
                                 int(temp2[3])))
        f.close()
        return np.array(data)