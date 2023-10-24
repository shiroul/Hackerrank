#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def cutTheSticks(arr):
    arr = sorted(arr)
    print(len(arr))
    while True:
        if len(arr) == 1:
            break
        while True:
            if len(arr) == 1:
                return
            if arr[0] != arr[1]:
                break
            arr.remove(arr[0])
        for x in range(1, len(arr)):
            arr[x] -= arr[0]
        
        arr.remove(arr[0])
        print(len(arr))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
