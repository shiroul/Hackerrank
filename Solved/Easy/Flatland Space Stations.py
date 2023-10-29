#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    maximum = 0
    s = 0
    index = 0
    any = 0

    for x in range(n):
        if x == c[index]:
            if any:
                if int(s/2) + (s%2>0) > maximum:
                    maximum = int(s/2) + (s%2>0)
                s=0
            elif s>=maximum:
                any = 1
                maximum = s
            index+=1
            if index == len(c):
                s = n-c[index-1]-1
                break
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
