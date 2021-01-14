# 2020-12-23
# https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s = s.split(':')

    if s[-1][-2:] == "PM":
        s[0] = str(int(s[0]) + 12)
        if s[0] == "24":
            s[0] = "12"
    else: # "AM"
        if s[0] == "12":
            s[0] = "00"
        
    s = ':'.join(s)

    return s[:-2]
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
