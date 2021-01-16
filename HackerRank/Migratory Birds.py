# 2021-01-16
# https://www.hackerrank.com/challenges/migratory-birds/problem

# O(n+n+n+n) = O(n)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    dic = {}
    
    for typ in arr:
        if dic.get(typ) == None:
            dic[typ] = 1
        dic[typ] += 1
    
    mx = max(dic.values())
    lst = [tpl[0] for tpl in dic.items() if tpl[1] == mx]
    
    return min(lst) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
