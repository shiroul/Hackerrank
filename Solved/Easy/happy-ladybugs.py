#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    temp = set(b)
    try:
        temp.remove('_')
    except KeyError:
        pass

    for x in temp:
        if b.count(x) == 1:
            return 'NO'
    
    if '_' in b:
        return 'YES'
    
    if b[0] != b[1]:
        return 'NO'
    
    for x in range(1, len(b)-1):
        if b[x] == b[x-1]:
            continue
        if b[x] == b[x+1]:
            continue
        return 'NO'
    
    if b[-1] != b[-2]:
        print(5)
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
