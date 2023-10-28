#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    if len(arr) == 1:
        return arr
    first = 0
    second = 0
    y = len(arr)-1
    for x in range(len(arr)):
        first+=arr[x][y]
        y-=1
    y=0
    for x in range(len(arr)):
        second+=arr[x][y]
        y+=1
    
    return abs(second-first)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
