import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for i in range (len(arr)):
        if arr[i]>0:
            pos += 1
        elif arr[i]<0:
            neg += 1
        else:
            zero+=1
    
    a = [pos,neg,zero]
    total = pos+neg+zero
    for i in range(len(a)):
        print(a[i]/total)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
