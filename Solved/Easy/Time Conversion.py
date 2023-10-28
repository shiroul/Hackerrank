#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    temp = ''
    if s[-2] == 'A':
        temp = s[:2]
        if temp == '12':
            s = '00' + s[2:]
        return s[:-2]
    
    temp = s[:2]
    if temp == '12':
        return s[:-2]
    
    temp = s[:2]
    temp2 = int(temp) + 12
    return str(temp2) + s[2:-2]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
