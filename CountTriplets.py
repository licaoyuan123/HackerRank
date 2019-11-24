#From https://www.hackerrank.com/challenges/count-triplets-1/forum
#Couple of hints:
#Can be done in O(n) -> single pass through data
#No division necessary and single multiplications by R are all that's needed
#Using map(C++) or dict(Java, Python) is a must -> can be unordered map (saves O(logN))
#Try to think forward when reading a value -> will this value form part of a triplet later?
#No need to consider (R == 1) as a corner case
#Very interesting problem and it took a while to think it through properly. If anyone is desperate for the code, drop me a message.
'''
As a base consider a triplet made up of numbers A,B and C (where B = A* r and C = A* r * r = B* r).

For each value (say X) in the array, you have to consider that X may be an A, B and/or C in some triplet.

When can X be a middle of a triplet (that is case X = B in the triplet)? -> when I already have had one or more previous values which will fulfill the requirements of A for this B. So we need to check if there are any previous A's "waiting" for this B. Here we just check the map mentioned in the previous comment. If there's any that means that we need to consider how many A's are "waiting" to know how many 2/3 complete triplets we'd now have with this X.

Similarly to the previous comment we will then let future Cs know that we have these extra 2/3 triplets ready. So store in map of almost complete triplets (ensuring that we add to any previous ones already stored). This is the second part of the loop.

Final case, when X completes one or more previously 2/3 complete triplets. Simply check how many (if any incomplete triplets) are "waiting" for this value to become complete. So check the map of 2/3 triplets and accumulate the result.

In any case X can be an A of a future triplet so add it to the map2 so future B's know of this A's existence -> Final part of the loop.
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from collections import defaultdict
# Complete the countTriplets function below.
# def valid(list_array, r):
#     for i in range(1, len(list_array)):
#         if list_array[i]!=list_array[i-1]*r:
#             return False
#     return True

# def countTriplets(arr, r):
    #n=len(arr)
    # count=0
    # comb = list(combinations(arr, 3))
    # for item in comb:
    #     #print(item)
    #     if valid(item, r):
    #         #print(item, "valid")
    #         count+=1
    # return count

def countTriplets(arr, r):
    dic2 = defaultdict(int)
    dic3 = defaultdict(int)
    count=0
    for item in arr:
        count+=dic3[item]
        dic3[item*r]+=dic2[item]
        dic2[item*r]+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
