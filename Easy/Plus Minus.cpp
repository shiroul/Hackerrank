#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zero,plus,minus = 0,0,0
    for x in arr:
        if x == 0:
            zero+=1
            continue
        if x >0:
            plus+=1
            continue
        else:
            minus+=1
    
    print(format(plus/len(arr), '.6f'))
    print(format(minus/len(arr), '.6f'))
    print(format(zero/len(arr), '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
