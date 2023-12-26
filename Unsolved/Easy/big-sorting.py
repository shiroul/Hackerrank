#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_unsortedAY.
# The function accepts STRING_unsortedAY unsorted as parameter.
#

def bigSorting(unsorted):
    # if len(unsorted) < 1:
    #     return unsorted
    # index = -1
    # pivot = int(unsorted[-1])
    # for x in range(len(unsorted) - 1):
    #     if len(unsorted[-1]) > len(unsorted[x]):
    #         index+=1
    #         unsorted[x], unsorted[index] = unsorted[index], unsorted[x]
    #         continue

    #     if pivot > int(unsorted[x]):
    #         index+=1
    #         unsorted[x], unsorted[index] = unsorted[index], unsorted[x]
    
    # return bigSorting(unsorted[:index+1]) + [pivot] + bigSorting(unsorted[index+1:-1])
    # Write your code here

    return sorted(unsorted, key=lambda x: (len(x), x))

    #will sorted based on len of string x then if it have same len then will sort by string x it self
    
    #credit @thinhproee

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    print(unsorted)        
    result = bigSorting(unsorted)
    
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
