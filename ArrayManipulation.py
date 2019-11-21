#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #Solution form discuss, only store the different
    arr = [0]*(n+1)
    for i in range(len(queries)):
        arr[queries[i][0]-1]+=queries[i][2]
        if queries[i][1]<n+1:
            arr[queries[i][1]]-=queries[i][2]
    max_value=x=0
    for i in range(len(arr)):
        x+=arr[i]
        max_value = max(max_value, x)
    return max_value




    #My first solution using numpy, however hackerrank do not support numpy
    # arr= np.array([0]*n)
    # for i in range(len(queries)):
    #     arr[queries[i][0]-1:queries[i][1]]+=queries[i][2]
    # return max(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
