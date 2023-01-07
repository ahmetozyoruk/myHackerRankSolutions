#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    
    resultNumber = int()
    binaryNumber = '{:032b}'.format(n,'b')
    
    print(binaryNumber)
    flippedNumber = ''.join(['1' if i == '0' else '0' for i in binaryNumber])
    
    resultNumber = int(flippedNumber,2)

    return resultNumber
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
