#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    output=0
    for x in range(len(B)):
        if B[x]%2 != 0:
            if x == len(B)-1:
                return 'NO'
            B[x]+=1
            B[x+1]+=1
            output+=1
    return output*2
        
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)
    
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
