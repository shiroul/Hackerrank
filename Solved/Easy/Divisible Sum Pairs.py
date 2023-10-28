#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    element = [x for x in range(n)]
    comb = combinations(element,2)
    
    temp = 0
    output = 0
    for x in list(comb):
        for y in x:
            temp+=ar[y]
        if temp % k == 0:
            output+=1
        temp = 0
    return output
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
