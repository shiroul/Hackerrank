#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for x in range(n):
        for y in range(n-(x+1)):
            print(' ', end ="")
        for y in range(x+1):
            print('#', end ="")
        print('')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
