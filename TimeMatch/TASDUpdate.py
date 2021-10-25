# Functions to analyze TASD19 Data
from datetime import *
import numpy as np


class TASDUpdate:

    def __init__(self, name):
        self.name = name

    def datetimeArray(self):
        data = []
        f = open(self.name, 'r')
        for line in f:
            temp = split(' ')
            time = temp[3].split('.')
            for i in range(0, 3):
                if len(temp[i]) != 6:
                    temp[i] = temp[i].rjust(6, '0')

            data.append(datetime(2000 + int(temp[0][0:2]),
                                 int(temp[0][2:4]),
                                 int(temp[0][4:6]),
                                 int(temp[1][0:2]),
                                 int(temp[2][0:2]),
                                 int(time[0]),
                                 int(temp[1])))
        f.close()
        return np.array(data)
