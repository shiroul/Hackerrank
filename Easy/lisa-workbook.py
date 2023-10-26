#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    special = 0
    page = 1
    problem = 1

    for x in arr:
        problem = 1
        temp = x/ k
        r = x
        print(r)
        if temp.is_integer():
            temp = int(temp)
        else:
            temp = int(temp) + 1

        for y in range(1, temp+1):
            if problem>page:
                page = page + temp-y +1
                break
            if int(r/k):
                if page>=problem and page<=k*y:
                    special+=1
            else:
                if page>=problem and page<=r:
                    special+=1
            r-=k
            print(r)
            page+=1
            problem+=k
            input("Press Enter to continue...")
    return special
            

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    n = 90

    k = 29

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
