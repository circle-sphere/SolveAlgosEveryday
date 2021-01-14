# 2021-01-15
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    def factorial(n):
        if n == 1:
            return 1
        res = n * factorial(n-1)
        return res
    
    print(factorial(n))

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
