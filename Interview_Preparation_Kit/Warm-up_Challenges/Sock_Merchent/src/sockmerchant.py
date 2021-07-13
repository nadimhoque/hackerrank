#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=0

    #create a new dictionary pairs. The keys will be the sock type and value is the number existing
    pairs = dict()

    #iterate through the array and do the following:
    #1. Check if it is in the pairs dictionary.
    #   *If it is in the dictionary and there is an existing sock, or in other words the value is 1, then add 1 to the counter and set the value to 0
    #   *If it is not in the dictionary add the sock and set the value to 1 since it does exist.
    for sock in range(n):
        if ar[sock] in pairs and pairs[ar[sock]] == 1:
            count=count+1
            pairs[ar[sock]] = 0
        else:
            pairs[ar[sock]] = 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    
    fptr.write(str(result) + '\n')

    fptr.close()
