#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    counter = Counter(s)
    frequency= list(counter.values())
    n=len(set(frequency))
    if n<2:
        return "YES"
    if n>2:
        return "NO"
    if n==2:
        max_fre= max(frequency)
        min_fre=min(frequency)
        max_count = frequency.count(max_fre)
        min_count = frequency.count(min_fre)
        if min_count==1:
            return "YES"
        #if max_count>1 or max_fre-min_fre>1:
        if max_count>1 or max_fre-min_fre>1:
        #max_count> 1 for the case of "aaaabbcc"
        #or "aabbcceeefff"
            return "NO"
        return "YES"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
