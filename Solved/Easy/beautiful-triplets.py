#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
def beautifulTriplets(d, arr):
    output=0
    for x in range(len(arr) - 2):
        for y in range(x+1, len(arr) -1):
            if arr[y] - arr[x] != d:
                continue
            for z in range(y+1, len(arr)):
                if arr[z] - arr[y] != d:
                    continue
                output+=1
    
    return output

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
