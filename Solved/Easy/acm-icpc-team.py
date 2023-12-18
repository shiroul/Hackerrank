#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    maxTopic = 0
    maxTeam = 0

    for x in range(len(topic)-1):
        firstTopic = int(topic[x],2)
        for y in range(x+1, len(topic)):
            secondTopic = str(bin(firstTopic | int(topic[y], 2))).count('1')
            
            if secondTopic > maxTopic:
                maxTopic = secondTopic
                maxTeam = 1
                continue
            if secondTopic == maxTopic:
                maxTeam+=1

    return maxTopic, maxTeam
            
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
