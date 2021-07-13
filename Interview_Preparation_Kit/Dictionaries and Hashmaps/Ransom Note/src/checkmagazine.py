#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
   md = Counter(magazine.split(' '))

   for i in note.split(' '):
      if i in md.keys() and md[i] != 0 :
        md[i] = md[i] - 1
      else:
        return False

   return True

#mag = "ive got a lovely bunch of coconuts"
#note = "ive got some coconuts"

#checkMagazine(mag,note)

mag="two times three is not four"
note="two times two is four"

if checkMagazine(mag,note) == True:
    print("Yes")
else:
    print("No")