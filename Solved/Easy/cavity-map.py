#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    if len(grid) == 1:
        return grid
    output = []
    output.append(grid[0])
    for x in range(1, len(grid)-1):
        temp = str(grid[x])
        for y in range(1, len(grid)-1):
            if grid[x][y] > grid[x][y-1] and grid[x][y] > grid[x][y+1] and grid[x][y] > grid[x-1][y] and grid[x][y] > grid[x+1][y]:
                temp= temp[:y] + 'X' + temp[y+1:] 
        output.append(temp)
    output.append(grid[-1])
    return output
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)
    
    for x in result:
        print(x)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
