# 2021-01-25
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True)

    max_score = ranked[0]
    min_score = ranked[-1]
    leng_scores = len(ranked)
    
    res = []
    for p in player:
        if p > max_score:
            index_score = 1
        elif p < min_score:
            index_score = leng_scores+1
        else:
            index_score = binary_search(ranked, 0, leng_scores - 1, p)

        res.append(index_score)
    
    return res

def binary_search(arr, start, end, x):
    mid = 0
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == x:
            return mid + 1

        elif arr[mid] < x:
            end = mid - 1

        else:
            start = mid + 1

    return start + 1
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
