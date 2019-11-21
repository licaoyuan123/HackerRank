#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    char_num_a = [0]*26
    char_num_b = [0]*26
    count=0
    for ch in a:
        char_num_a[ord(ch)-ord('a')]+=1
    for ch in b:
        char_num_b[ord(ch)-ord('a')]+=1
    for i in range(26):
        count+=abs(char_num_a[i]- char_num_b[i])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
