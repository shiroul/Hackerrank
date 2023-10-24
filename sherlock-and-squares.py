#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    i = 1
    output = 0

    while True:
        if i*i >= a:
            break
        i+=1


    while True:
        if i*i >= b:
            if i*i == b:
                output+=1
            break
        output+=1
        i+=1

    print(output)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
