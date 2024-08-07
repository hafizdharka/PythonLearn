#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    countA = 0
    countB = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            countA = countA+1
        elif b[i]>a[i] :
            countB = countB +1

    return [countA,countB]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
