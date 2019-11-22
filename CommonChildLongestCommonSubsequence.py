
#My first solution however it is too slow and some error cases happen
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    #I guess I shall use dfs
    result=[]
    path=[]
    dfs(s1, s2, path, result)
    max_length=0
    for item in result:
        max_length = max(max_length, len(item))

    return max_length

def dfs(s1, s2, path, result):
    if not s1 or not s2:
        if path:
            result.append(path)
        return
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                dfs(s1[i+1:], s2[j+1:], path+[s1[i]], result)
                dfs(s1[i+1:], s2[j:], path, result)


    # for i in range(index1, len(s1)):
    #     for j in range(index2, len(s2)):
    #         if s1[i]==s2[j]:
    #             dfs(s1, s2, i+1, j+1, path+[s1[i]], result)
    #             dfs(s1, s2, i+1, j, path, result)
                



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
