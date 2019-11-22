#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the substrCount function below.
def substrCount(n, s):
    ch_ind_list = []
    ans=0
    cur =None
    count=0
    #First pass to constract the list
    for i in range(n):
        if s[i]==cur:
            count+=1
        else:
            if cur is not None:
                ch_ind_list.append((cur, count))
            count=1
            cur=s[i]
    ch_ind_list.append((cur, count))
    #second pass to count all the same chars
    for i in range(len(ch_ind_list)):
        ans+=(ch_ind_list[i][1]*(ch_ind_list[i][1]+1))//2
    #Third pass to count the second situation
    for i in range(1, len(ch_ind_list)-1):
        if ch_ind_list[i][1]==1 and ch_ind_list[i-1][0]==ch_ind_list[i+1][0]:
            ans+=min(ch_ind_list[i-1][1], ch_ind_list[i+1][1])
    return ans




#My solution, however it is TLE
# def valid(s):
#     if s.count(s[0])==len(s):
#         #print(s)
#         return True
#     elif len(s)%2==1 and (s[0:len(s)//2]+s[len(s)//2+1:]).count(s[0])==len(s)-1:
#         #print(s)
#         return True
#     return False
# # Complete the substrCount function below.
# def substrCount(n, s):
#     count=n
#     for length in range(2,n+1):
#         for index in range(0,  n-length+1):
#             if valid(s[index:index+length]):
#                 count+=1
#     return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
