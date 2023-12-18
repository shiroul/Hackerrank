#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    output = 0

    if not bool(re.search(r'\d', password)):
        output+=1

    if not bool(re.search(r'[a-z]', password)):
        output+=1

    if not bool(re.search(r'[A-Z]', password)):
        output+=1

    if not bool(re.search(r'[-!@#$%^&*()+]', password)):
        output+=1

    if n < 6:
        temp = 6-n
        if temp > output:
            return temp

    return output
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
