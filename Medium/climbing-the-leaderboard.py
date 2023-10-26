#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
  temp = [1]
  output = []
  for x in range(1, len(ranked)):
    if ranked[x] == ranked[x-1]:
      temp.append(temp[x-1])
      continue
    temp.append(temp[x-1]+1)
  
  iterator = len(ranked)-1

  for x in player:
    if x < ranked[iterator]:
      output.append(temp[iterator]+1)
      continue
    if x >= ranked[0]:
      output.append(1)
      continue
    while iterator >= 0 and x >= ranked[iterator]:
      iterator-=1
    output.append(temp[iterator]+1)
  return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
