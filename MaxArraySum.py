'''
To address with DP, work through the array, keeping track of the max at each position until you get to the last value of the array. You should start with the base cases defined before iterating through the remainder of the array.

max @ position 0: value @ 0

max @ position 1: either:

value @ 0
value @ 1
from that point forward, the max of the next position is either:

the current value at that position
the max value found so far
the max value from 2 positions back plus the current value
keep track of the max at each position until you get to the last position of the array
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr)<3:
        return max(arr)
    result = [arr[0], max(arr[0], arr[1])]
    for i in range(2, len(arr)):
        result.append(max(arr[i], max(result[i-1], result[i-2]+arr[i])))
        #pass

    return result[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
