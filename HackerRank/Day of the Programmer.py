# 2021-01-04
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if 1700 <= year and year <= 1917: # Julian
        if year%4 == 0:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
        else:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif year == 1918:
        days = 31 + 15 + 31 + 30 + 31 + 30 + 31 + 31
        return str(256-days)+".09."+str(year)
    else: # Gregorian
        if year%4 == 0 or year%400 == 0: # leap yaer
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
            if year%100 == 0 and year%400 != 0: # not leap yaer
                days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
        else: # not leap yaer
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31

    return str(256-days)+".09."+str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
