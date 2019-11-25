#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    result = []
    dic = defaultdict(int)
    cnt = defaultdict(int)
    for query in queries:
        if query[0]==1:
            cnt[dic[query[1]]]-=1
            dic[query[1]]+=1
            cnt[dic[query[1]]]+=1
            
        elif query[0]==2:
            if dic[query[1]]>0:
                cnt[dic[query[1]]]-=1
                dic[query[1]]-=1
                cnt[dic[query[1]]]+=1

            
            # cnt[dic[query[1]]]-=1
            # cnt[dic[query[1]]] = max(0, cnt[dic[query[1]]])
            # dic[query[1]]-=1
            # dic[query[1]] = max(0, dic[query[1]])
            # cnt[dic[query[1]]]+=1
        
        else:
            if cnt[query[1]]>0:
                result.append(1)
            else:
                result.append(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
