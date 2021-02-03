# 2021-02-04
# https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    n_list = [int(d) for d in str(n)]
    
    cnt = 0
    for d in n_list:
        if d == 0:
            continue
        
        if n%d == 0:
            cnt += 1
            
    return cnt
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
