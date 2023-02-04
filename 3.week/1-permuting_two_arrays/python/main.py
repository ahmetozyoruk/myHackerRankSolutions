#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    sumNumberOfArray=0 
    sumPassedNumberOfK=0
    
    if(len(A) != len(B)):
        if(len(A) > len(B)):
            for i in range(len(A)-len(B)):
                B.append(0)
        else:
            for i in range(len(B)-len(A)):            
                A.append(0)    
          
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        sumNumberOfArray = A[i]+B[i] 
        if sumNumberOfArray >= k:
            sumPassedNumberOfK = sumPassedNumberOfK +1
        else:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
