#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh=int(s[:2])
    if "PM" in s:
        if hh!=12:
            hh+=12

    if "AM" in s:
        if hh==12:
            hh=00
    
    hour=(str(hh)).zfill(2)
    
    return f"{hour}{s[2:-2]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
