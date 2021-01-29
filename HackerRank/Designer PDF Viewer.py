# 2021-01-29
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    ddic = defaultdict(int)
    
    j = 0
    for i in range(97,123):
        ddic[chr(i)] = h[j]
        j+=1
    
    max_size = 0
    for w in word:
        if ddic[w] > max_size:
            max_size = ddic[w]
            
    return max_size * len(word)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
