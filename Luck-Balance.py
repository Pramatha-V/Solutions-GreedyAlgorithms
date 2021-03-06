#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
  luckValue = 0
  contests.sort(reverse=True)
  for i in contests:
    if (i[1] == 0):
        luckValue += i[0]
    elif (k > 0):
        luckValue += i[0]
        k -= 1
    else:
        luckValue -= i[0]
  return luckValue
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
