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

    page = 0
    output = 0

    for x in arr:
        maxPage = int(x/k) + (x%k>0)
        problem = 1
        for y in range(1, maxPage+1):
            page+=1
            print('problem = ', problem, 'page = ', page, 'x = ', x, 'y = ', y)
            if problem > page:
                page+=maxPage-y
                break
            
            if x>k:
                x-=k
                if page>= problem and page<=y*k:
                    output+=1
                    print('pop')
                problem+=k
                continue
            if page>= problem and page<problem+x:
                print(page, problem, x, y)
                output+=1
                print('pop')
            
    return output
                

            

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    n = 5

    k = 3

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
