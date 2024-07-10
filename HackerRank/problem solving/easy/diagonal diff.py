import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    maind = sum([arr[i][i] for i in range(n)])
    revd = sum([arr[i][n-1-i] for i in range(n)])
    return abs(maind-revd)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
