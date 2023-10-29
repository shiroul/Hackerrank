#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    index = 0
    maximum = 0
    s = 0
    any = 0
    for x in range(0, n):
        if x == c[index]:
            index+=1
            if index==len(c):
                s = n-x
                break
            if any:
                temp = int(s/2 + (s%2>0))
            else:
                temp = s
                any = 1

            if temp> maximum:
                maximum = temp 
            s=0
            continue
        s+=1
    if s>maximum:
        return s
    return maximum
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
