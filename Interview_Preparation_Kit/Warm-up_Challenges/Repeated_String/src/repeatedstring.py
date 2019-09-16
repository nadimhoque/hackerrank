#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    numa = 0
    temp = ''

    if s == 'a':
        return n
    else:
        for i in range(n):
            temp = temp + s

        for j in range(n):
            if temp[j] == 'a':
                numa = numa + 1
    return numa

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
