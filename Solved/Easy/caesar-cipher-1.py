#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    output = ''
    if k > 26:
        k = k - (26 * (int(k/27)))
        
    for x in s:

        temp = ord(x)
        
        if temp < 65 or (temp>90 and temp<97) or temp> 122:
            output+= x
            continue
        
        
        if temp <= 90:
            temp+= k
            if temp > 90:
                output+= chr(temp-26)
                continue
            output+= chr(temp)
            continue
        
        temp += k
        
        if temp > 122:
            output += chr(temp-26)
            continue
        output += chr(temp)

    return output
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
