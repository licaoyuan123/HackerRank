#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median
from collections import deque
# Complete the activityNotifications function below.
class RunningMedian():
    def __init__(self, maxlen):
        self.maxLen = maxlen
        self.d = [0] *201
        self.queue = deque()
    def add(self, value):
        self.queue.append(value)
        self.d[value]+=1
        if len(self.queue)>self.maxLen:
            val = self.queue.popleft()
            self.d[val]-=1
    def median(self):
        a = int(self.maxLen/2)
        b=a+1
        mid1 = None
        mid2 = None
        rs = 0

        for idx, v in enumerate(self.d):
            rs+=v
            if rs>=a and mid1 is None:
                mid1=idx
            if rs>=b:
                mid2=idx
                break
        if self.maxLen%2==0:
            return (mid1+mid2)/2
        else:
            return mid2

def activityNotifications(expenditure, d):
    count=0
    r = RunningMedian(d)
    for v in expenditure[:d]:
        r.add(v)
    for idx, v in enumerate(expenditure[d:]):
        median=r.median()
        if v>=2*median:
            count+=1
        r.add(v)
    return count

# def activityNotifications(expenditure, d):
#     #Sliding window
#     count = 0
#     for i in range(len(expenditure)-d):
#         window = expenditure[i:i+d]
#         #print("window: ", window)
#         window.sort()
        
#         cur = expenditure[i+d]
#         m= median(window)
#         #print("cur: ", cur)
#         # if d%2==0:
#         #     median = (window[d//2]+window[d//2-1])/2
#         # else:
#         #     median = window[d//2]
#         #print("median: ", median)
#         if cur>=2*m:
#             count+=1
#     return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
