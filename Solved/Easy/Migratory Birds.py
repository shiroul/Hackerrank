#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    arr.sort()

    max = 0
    temp = 1
    output = 0

    for x in range(1, len(arr)):
        if arr[x] == arr[x-1]:
            temp+=1
            print(temp, arr[x])
            continue
        if temp>max:
            output = arr[x-1]
            max = temp
            temp = 1
    if temp>max:
        output = arr[x-1]
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
