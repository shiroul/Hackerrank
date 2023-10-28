#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p == 1:
        return 0
    if n == p:
        return 0
    if n == p+1:
        if n%2 == 0:
            return 1
        else:
            return 0
    
    output = (p/2)

    backward = (n-p)/2

    if backward < output:
        return int(backward)
    return int(output)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
