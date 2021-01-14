# 2021-01-06
# https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n%2 == 0:
        n += 1
        
    return min([p//2, (n - p)//2])  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
