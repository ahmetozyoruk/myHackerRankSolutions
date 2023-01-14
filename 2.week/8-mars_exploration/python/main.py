#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    s.upper()
    changedCharacter = 0
    for item in range(len(s)):
        if((item % 3 ==0 or item % 3 ==2) and s[item] != "S" ):
            changedCharacter +=1
        if(item % 3 ==1 and s[item] != "O" ):
            changedCharacter +=1

    print(changedCharacter)
    return changedCharacter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

