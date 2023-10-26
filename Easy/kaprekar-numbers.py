#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    temp = ''
    output = ''

    if p == 1:
        output+='1 '
    
    if p<4:
        p = 9
        
    for x in range(p, q+1):
        temp = str(x*x)
        if len(temp)%2 == 0:
            if int(temp[:int(len(temp)/2)]) + int(temp[-int(len(temp)/2):]) == x:
                output+= str(x) + ' '
                continue
            continue
        if int(temp[:int(len(temp)/2)]) + int(temp[-int(len(temp)/2+1):]) == x:
            output+= str(x) + ' '
    if output == '':
        print("INVALID RANGE")
        return
    print(output)
        
        
        
    # Write your code here

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
