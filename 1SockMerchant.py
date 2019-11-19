#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # ar.sort()
    # count=0
    # for ind, value in enumerate(ar):
    # counter = Counter(ar)
    # count = 0
    # for key in counter:
    #     count+=counter[key]//2
    # return count
    socks = set()
    count = 0
    for color in ar:
        if not (color in socks):
            socks.add(color)
        else:
            count+=1
            socks.remove(color)
    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
