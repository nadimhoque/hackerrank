#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    numjump=0
    jump=0
    size=len(c) -1
    while (jump <= size):
        if  (jump+2) < size and c[jump+2] == 0:
            jump=jump+2
            numjump = numjump+1
        elif c[jump+1] == 0:
            jump=jump+1
            numjump = numjump+1     
    print(numjump)

"""
if __name__ == '__main__':
    main()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
n = int(input())
c = list(map(int, input().rstrip().split()))
jumpingOnClouds(c)
#result = jumpingOnClouds(c)
#print(result)

