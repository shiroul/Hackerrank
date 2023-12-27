#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    
    output = set(arr[0])
    temp = output
    
    for x in range(1, len(arr)):
        output = set()
        for y in set(arr[x]):
            if y in temp:
                output.add(y)
        temp = output
        
    return 0 if output == set() else len(output)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


## alternate solution by @Perry901
    
# def gemstones(arr):
#     # Write your code
#     result =set(arr[0])
#     for i in arr:
#         a = set(i)
#         result=result.intersection(a)  
#     return len(result)

# using intersection() only to get same value from both set