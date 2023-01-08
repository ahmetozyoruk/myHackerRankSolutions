#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    leftArray = []
    rightArray = []
    
    sumLeft = int()
    sumRight = int()
    
    result = int()
    
    if len(arr) == 1 and len(arr[1]):
        return 0
    
    if len(arr) != len(arr[0]):
        print("please enter equal dimention array each other")
    
    for i in range(len(arr)):
        
        temp = (len(arr[0])-(i+1))
        righttItem = arr[i][temp]
        leftItem = arr[i][i]
        
        leftArray.append(leftItem)
        rightArray.append(righttItem)
    
    for i in leftArray:
        sumLeft = sumLeft + i
        
    for i in rightArray:
        sumRight = sumRight + i
    
    if sumLeft > sumRight:
        result = sumLeft - sumRight
    else:
        result = sumRight - sumLeft
        
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
