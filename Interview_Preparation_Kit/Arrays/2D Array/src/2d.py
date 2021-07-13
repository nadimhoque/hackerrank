#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max=-63 # this is based off of all of the elements of the hourglass integeres being -9
    curr=0
    
    for i in range(4):
        for j in range(4):
            curr=sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
    
            if curr > max:
                max = curr

    return max
    

test=[[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]

print(hourglassSum(test))