#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # count = 0
    # for ch in s:
    #     if ch=='a':
    #         count+=1
    # len_s = len(s)
    # time = n//len_s
    # total_count = count*time
    # str_left = n%len_s
    # for i in range(str_left):
    #     if s[i]=='a':
    #         total_count+=1
    total_count = s.count("a")*(n//len(s))+ s[:n%len(s)].count("a")
    return total_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
