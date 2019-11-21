#https://www.hackerrank.com/challenges/minimum-swaps-2/submissions/code/131479377
#count the number of edges-1 and sum up
#remember [*enumerate(arr)]
#.sort(key=lambda n:n[1])

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count=0
    new_arr = [*enumerate(arr)]
    new_arr.sort(key= lambda po:po[1])
    visited= [False]*len(arr)
    for i in range(len(arr)):
        if visited[i] or new_arr[i][0]==i:
            continue
        j=i
        edge=0
        while not visited[j]:
            visited[j]=True
            j=new_arr[j][0]
            edge+=1
        if edge>0:
          count+=edge-1
    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
