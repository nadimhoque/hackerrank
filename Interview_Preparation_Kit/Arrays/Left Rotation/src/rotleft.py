#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for itt in range(d):
        a.append(a.pop(0))
    return a

arr = [1,2,3,4,5]

print(rotLeft(arr,4))
