#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_level = 0
    count=0
    for ch in s:
        if ch=="D" and current_level==0:
            count+=1
        if ch=="U":
            current_level+=1
        else:
            current_level-=1
    return count



    # level_list = [0]
    # current_level = 0
    # count=0
    # for char in s:
    #     if char=='U':
    #         current_level+=1
    #     else:
    #         current_level-=1
    #     level_list.append(current_level)
    # for i in range(len(level_list)-1):
    #     if level_list[i]==0 and level_list[i+1]<0:
    #         count+=1
    # return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
