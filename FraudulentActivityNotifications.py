'''
4 thoughts that may help:
1.) Counting sort
2.) A Queue
3.) Pay attention to the even case.
4.) Integer division is a blessing and a curse, be careful.
I really enjoyed this problem :) It's an extremely practical use of the material, a little tricky,
but very doable with some good thought and planning.

On the input you have an array of frequencies for all possible numbers (0-200) for the gap of values from basic array
(this gap size is set by d input).

you create another one array and start to build it from frequencies array the following way:
you sum frequency of every number and frequencies of previous numbers.
What you really need to understand:
this second array values will give you last indexes at which every number of frequencies would appear in sorted array.

That is, imagine frequency array [0]2, [1]1, [2]0, [3]4. Building second array would give you [0]2, [1]1+2 =3, [2]0+3=3, [3]3+4=7.

Now, imagine building sorted array from input frequencies array: 0 0 1 3 3 3 3 [0][1][2][3][4][5][6]

so now you take just half of a 'd' and iterate through second array, looking for number which is more huge or equals to d.
Meeting such number means that you're currently pointing at index whose value would be in the middle of sorted array, 
and this is just what you need.
'''
#Implementation with out class
def median(v, d):
    count = 0
    if d%2==0:
        m1 = None
        m2 = None
        for i in range(len(v)):
            count += v[i]
            if count >= d/2 and m1 is None:
                m1 = i
            if count >= d/2 + 1:
                m2 = i
                break
        return (m1 + m2)/2
    else:
        for i in range(len(v)):
            count += v[i]
            if count > d/2:
                return i
    return -1

def activityNotifications(expenditure, d):
    dq = deque(expenditure[: d])
    v = [0]*201
    for n in dq:
        v[n] += 1
    count = 0
    for current in expenditure[d:]:
        if current >= median(v, d)*2:
            count += 1
        v[current] += 1
        dq.append(current)
        v[dq.popleft()] -= 1
    return count

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
