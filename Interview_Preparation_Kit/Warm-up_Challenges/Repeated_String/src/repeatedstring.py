#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    #numa is the total number of 'a' to be returned
    numa = 0
    #suba is the total number 'a' that appears in the substring.
    suba = 0

    #This forloop will give us the total number of 'a' in the substring
    for i in range(len(s)):
        if s[i] == 'a':
            suba = suba + 1

    #Here we check if the substring is all 'a' and if so the number of 'a' is just 'n'  
    if s == 'a':
        numa = n
    else:
        #Here we check if the modulo of n and the length of 's' is zero.
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
