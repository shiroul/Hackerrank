#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    divisor = str(n)
    output = 0
    for x in divisor:
        if int(x) == 0:
            continue
        if n % int(x) == 0:
            output+=1
    print(output)
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        # fptr.write(str(result) + '\n')

    # fptr.close()
