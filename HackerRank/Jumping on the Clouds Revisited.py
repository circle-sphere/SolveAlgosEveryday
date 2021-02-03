# 2021-02-04
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    i = 0
    flag = True
    while flag:
        if c[i] == 1:
            e -= 2
        e -= 1
        
        i = (i+k)%n
        if i == 0:
            flag = False
            
    return e
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
