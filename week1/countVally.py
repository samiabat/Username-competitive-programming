#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    if path == "U":
        path = 1
    else:
        path = -1
    vally = 0
    l= []
    t = 0
    for i in range(steps):
        t += path
        l.append(t)
    
    for i in range(1, len(l)):
        if l[i] == 0 and l[i-1]<0:
            vally+=1
    print(vally)
    return vally
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
