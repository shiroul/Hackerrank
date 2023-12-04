#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    
    for x in range(n-1):
        if arr[x] > arr[x+1]:
            arr[x], arr[x+1] = arr[x+1], arr[x]
            for y in range(0, x):
                if arr[x-y] < arr[x-y-1]:
                    arr[x-y], arr[x-y-1] = arr[x-y-1], arr[x-y]
                else:
                    break
        print(*arr)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
