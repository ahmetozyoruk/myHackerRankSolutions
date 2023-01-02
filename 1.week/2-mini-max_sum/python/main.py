#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
    
    

def miniMaxSum(arr):
    total = sum(number for number in arr)
    minSum = total
    maxSum = 0
    for number in arr:
        currSum = total - number
        if currSum < minSum: 
            minSum = currSum
        if currSum > maxSum:
            maxSum = currSum
    print(f"{minSum} {maxSum}")  

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
