# 2021-01-07
# https://www.hackerrank.com/challenges/electronics-shop/submissions

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    
    res = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            price = keyboards[i] + drives[j]
            if b >= price:
                res.append(price)
    
    if len(res) == 0:
        return -1
    
    return max(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
