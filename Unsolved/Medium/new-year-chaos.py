#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    output = 0
    for x in range(1, len(q)):
        if q[x-1]<x:
            continue
        if q[x-1] - x > 2:
            print('Too chaotic')
            return
        output+= q[x-1] - x
    print(output)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
    
def minimumBribes(q):
    n = len(q)
    numSwaps = 0

    for i in range(n):
        if q[i] - i > 3:
            # q[i] - i == 3 means i moved forward twice
            print("Too chaotic")
            return
        
        # to count bribes we count the number of elements to the
        # left of i that is greater than q[i]
        # but get timeout if we iterate all left sub-array (0:i-1) 
        
        # let k = index of left-most number > q[i] where k < i
        # k is index to the left of q[i] on original sorted array
        # Ex: [1, 2, 3, 4, 5] -> left-most possible number > 4 is
        # 5 at index 2, so we only iterate starting at index 2
        
        k = q[i] - 2
        
        if q[i] == 1:
            # we can't have k = -1 since its an index
            k = 0
        for j in range(k, i):
            # we add a bribe for every number > q[i]
            if q[j] > q[i]:
                numSwaps += 1

    print(numSwaps)
    return


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
