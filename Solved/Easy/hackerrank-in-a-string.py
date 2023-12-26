#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    word = 'hackerrank'
    index = 0
    count = 0
    
    for x in word:
        for y in range(index, len(s)):
            if s[y] == x:
                index+=1
                count+=1
                break
            index+=1
        if count == 10:
            return 'YES'
    return 'NO'
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

# alternate solution by @matthew_adkins
    
# def hackerrankInString(s):
#     correct = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
#     for i in range(len(s)):
# 		    if correct and s[i] == correct[0]:
# 			      correct.pop(0)
#     return "YES" if not correct else "NO"

## this will return 'YES' if value of 'correct' is empty or '[]' and will return 'NO' if there is something left inside 'correct'