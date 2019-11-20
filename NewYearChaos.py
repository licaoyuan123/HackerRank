#!/bin/python3
#Only count how many person overtake another
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count=0
    for i in range(len(q)):
        if q[i]-i>3:
            print("Too chaotic")
            return
        for j in range(max(0, q[i]-2), i):
            if q[j]>q[i]:
                count+=1
    print(count)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
