#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):

  a.sort()

  noDupe = []
  temp = []
  iteration = -1
  for x in a:
    if x not in noDupe:
      noDupe.append(x)
      iteration+=1
      temp.append(1)
      continue
    temp[iteration]+=1
  
  if len(noDupe) == 1:
    return temp[0]

  output = 0

  for x in range(1, len(noDupe)):
    if noDupe[x] - noDupe[x-1] == 1:
      if temp[x] + temp[x-1] > output:
        output = temp[x] + temp[x-1]
  
  for x in temp:
    if x > output:
      output = x

  return output
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
