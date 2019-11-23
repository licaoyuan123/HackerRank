#Get all the substrings, sort them, use counter to combine the same together and get the number
#

from collections import Counter
from itertools import combinations
def sherlockAndAnagrams1(s):
    count=[]
    for i in range(1, len(s)):
        a=["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b=Counter(a)
        print(b)

        first = [list(combinations(['a']*b[j],2)) for j in b]
        print(first)
        middle=[len(list(combinations(['a']*b[j],2))) for j in b]
        count.append(sum([len(list(combinations(['a']*b[j],2))) for j in b]))

    return sum(count)

def sherlockAndAnagrams(s):
    count = 0
    #i is the length of the substring
    for i in range(1,len(s)):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        print(a)
        b = Counter(a)
        print(b)
        for j in b:
            count+=b[j]*(b[j]-1)//2
    return count
st= "cdcd"
print(sherlockAndAnagrams1(st))
