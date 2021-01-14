# 2021-01-15
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

# Use mathematical inference that the number of square integer
# between two integers is what the number of integer between two square roots.
# Plus, handling "two space-separated integers" in Python is key point.
# In this code, they are handled simultaneously by math library

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    if math.sqrt(a) == int(math.sqrt(a)):
       return int(math.sqrt(b)) - int(math.sqrt(a)) + 1
    else:
        return int(math.sqrt(b)) - int(math.sqrt(a))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
