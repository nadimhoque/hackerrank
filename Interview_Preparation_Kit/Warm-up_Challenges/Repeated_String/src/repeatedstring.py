#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    numa = 0
    suba = 0

    for i in range(len(s)):
        if s[i] == 'a':
            suba = suba + 1

    if s == 'a':
        numa = n
    else:
        if n % len(s) == 0:
            numa = suba * (n/len(s))
        else:
            numa = suba * math.floor(n/len(s))
            for i in range(n%len(s)):
                if s[i] == 'a':
                    numa = numa +1

    return math.floor(numa)

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
