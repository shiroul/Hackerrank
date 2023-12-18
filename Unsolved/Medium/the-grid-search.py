#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    index = 0
    temp = ''
    for x in range(len(G)):
        # index+=1
        # if P[0] in G[x]:
        #     for y in range(1, len(P)):
        #         if P[y] in G[index]:
        #             index+=1
        #             continue
        #         return 'NO'
        #     return 'YES'
        if P[0] in G[x]:
            for y in P[0]:
                if 

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()
