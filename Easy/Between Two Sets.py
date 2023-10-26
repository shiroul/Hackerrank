#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def factors(x, low, high):
    temp = []
    for i in range(low, x + 1):
        if i > high:
            return temp
        if x % i == 0:
            temp.append(i)
    return temp

def getTotalX(a, b):
    # Write your code here
    low = float('inf')
    high = float('-inf')

    temp = []
    temp2 = []
    output = []

    for x in b:
        if x<low:
            low = x
    

    for x in a:
        temp.clear()
        for y in range(x,low+1,x):
            temp.append(y)
        
        if not output:
            output = temp.copy()
            continue

        temp2 = output.copy()

        for y in output:

            if y in temp:
                continue

            temp2.remove(y)
        
        output = temp2.copy()
        temp2.clear()
    
    if not output:
        print('0')
        return
    
    low = float('inf')

    for x in output:
        if x<low:
            low = x
        if x>high:
            high = x

    for x in b:
        temp.clear()
        temp = factors(x, low, high)
        temp2 = output.copy()
        for y in output:
            if y in temp:
                continue
            temp2.remove(y)
        
        output = temp2.copy()
        temp2.clear()
    
    print(len(output))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    # fptr.write(str(total) + '\n')

    # fptr.close()
