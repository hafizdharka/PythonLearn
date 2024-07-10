#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    low = arr.index(min(arr))
    high = arr.index(max(arr))
    maxv = 0
    minv = 0
    for i in range(len(arr)):
        if i!=low:
            maxv = maxv + arr[i]
        if i!=high:
            minv = minv + arr[i]
    print(minv, maxv)

    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
