#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for x in range(1,n):
        print(*arr[:n-x], end=' ')

        if arr[n-x] < arr[n-x-1]:
            print(arr[n-x-1], end=' ')
            arr[n-x],arr[n-x-1] = arr[n-x-1],arr[n-x]
        else:
            print(arr[n-x], end=' ')
            print(*arr[n-x+1:])
            return

        print(*arr[n-x+1:])
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
