#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1count = Counter(s1)
    s2count = Counter(s2)


    for i in s1count.keys():
        if i in s2count:
            print(i)
        else:
            return 'No'


s1 = "hello"
s2 = "world"

ex=twoStrings(s1,s2)
print(ex)


