#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    temp = sorted(a)
    double = []

    for x in range(1, len(a)):
        if temp[x] == temp[x-1]:
            double.append(temp[x])
    
    output = float('inf')
    tempOutput = 0

    for x in double:
        for y in range(a.index(x)+1, len(a)):
            if x == a[y]:
                tempOutput = abs(a.index(x) - y)
                if tempOutput < output:
                    output = tempOutput
    
    if output == float('inf'):
        return -1
    return output
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
