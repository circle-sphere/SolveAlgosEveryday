# 2021-01-21
# https://www.hackerrank.com/challenges/picking-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import Counter
def pickingNumbers(a):
    dic = dict(Counter(a))
    sorted_dic = sorted(dict(Counter(a)).items())
    
    max_len = max(dic.values())
    for i in range(len(sorted_dic)-1):
        k_diff = sorted_dic[i+1][0] - sorted_dic[i][0]
        v_diff = sorted_dic[i+1][1] + sorted_dic[i][1]
        
        if k_diff <= 1 and max_len < v_diff:
            max_len = v_diff
            
    return max_len
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
