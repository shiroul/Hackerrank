#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()
    alphabet = [chr(x) for x in range(97, 123)]
    
    for x in s:
        if x in alphabet:
            alphabet.remove(x)

    return 'pangram' if not alphabet else 'not pangram'
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

## alternate solution by @Perry901
    
# def pangrams(s):
#     # Write your code here
#     a = dict(Counter(s.lower()))
#     print(a)
#     if len(a)>=27:
#         return 'pangram'
#     return 'not pangram'
    
# first make all the input to be either lowercase or uppercase with string.lower() or string.upper() function
# make dictionary base on that so we get all unique letter
# if there is only less than 26 key in dictionary then return not pangram and if we have exact 26 key then return pagram
