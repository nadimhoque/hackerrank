#!/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    numjump = 0
    jump = 0
    size = len(c) -1
    while jump <= size:
        if (jump+2) < size and c[jump+2] == 0:
            jump = jump + 2
            numjump = numjump + 1
        elif c[jump+1] == 0 and (jump+1) < size:
            jump = jump + 1
            numjump = numjump+1
    return numjump


test = [0, 0, 1, 0, 0, 1, 0]

may=jumpingOnClouds(test)
print(may)
