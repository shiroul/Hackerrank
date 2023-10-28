#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum, high, low = 0,0,float('inf')
    for x in arr:
        sum+=x
        if x > high:
            high = x
        if x < low:
            low = x
    
    print(sum-high, end =" ")
    print(sum-low)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
