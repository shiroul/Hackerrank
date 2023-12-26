#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    
    setWeight = set()
    weight = ord(s[0]) - 96
    setWeight.add(weight)
    for x in range(1, len(s)):
        if s[x] == s[x-1]:
            weight += ord(s[x]) - 96
            setWeight.add(weight)
            continue
        weight = ord(s[x]) - 96
        setWeight.add(weight)

    return ['Yes' if x in setWeight else 'No' for x in queries]
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
