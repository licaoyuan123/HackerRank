#parameter of defaultdict should be callable lambda:0

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_counter = defaultdict(lambda:0)
    note_counter = defaultdict(lambda:0)
    for word in magazine:
        mag_counter[word]+=1
    for word in note:
        note_counter[word]+=1
    for word in note_counter:
        if note_counter[word]-mag_counter[word]>0:
            print("No")
            return
    print("Yes")


    # for ch in note_counter:
    #     if note_counter[ch]-mag_counter[ch]<0:
    #         print("No")
    #         return
    # print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
