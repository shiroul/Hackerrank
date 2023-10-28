#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    temp = 0
    energy = 100
    cloud = len(c)

    energy-=1
    if c[temp] == 1:
        energy-=2
    temp+=k
    
    if temp > cloud-1:
        temp-=cloud
        
    while temp!=0:
        energy-=1
        if c[temp] == 1:
            energy-=2
        temp+=k
        if temp > cloud-1:
            temp-=cloud
    
    print(energy)
 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
