#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def merge(arr, left_half, right_half):
    i, j, k = 0, 0, 0
    inversions = 0
    left_len, right_len = len(left_half), len(right_half)
    while i < left_len and j < right_len:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            inversions += left_len - i
        k += 1

    while i < left_len:
        arr[k] = left_half[i]
        i, k = i+1, k+1

    while j < right_len:
        arr[k] = right_half[j]
        j, k = j+1, k+1

    return inversions

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half, right_half = arr[:mid], arr[mid:]

        inversions = merge_sort(left_half) + merge_sort(right_half) + merge(arr, left_half, right_half)
        return inversions
    return 0



def countInversions(arr):
    return merge_sort(arr)
    #Try if bubble sort can work
    #count=0
    #Bubbule sort is too slow, so try to use merge sort
    # for i in range(len(arr)-1, -1, -1):
    #     for j in range(i):
    #         if arr[j]>arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #             count+=1
    #print("arr:", arr)
    #Split, merge
    # result = []
    # for i in range(len(arr)):
    #     if not result:
    #         result.append(arr[i])
    #     else:
    #         for j in range(len(result)-1, -1, -1):
    #             if result[j]<arr[i]:
    #                 result = result[:j+1]+[arr[i]]+result[j+1:]
    #             else:
    #                 count+=1
    # print(result)
    #return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
