# 2021-02-02
# https://www.hackerrank.com/challenges/angry-professor/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    a.sort() # O(nlogn)
    
    condition = True
    i = 0
    while condition: # O(k)
        i += 1
        if a[i] > 0:
            condition = False
            
    if i < k:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
