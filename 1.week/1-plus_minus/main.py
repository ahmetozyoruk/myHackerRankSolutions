#!/bin/python3

import math
import os
import random
import re
import sys
from enum import Enum

_lenghtOfFloat = 8;

class Condition(Enum):
    isPositive = 1
    isNegative = 2
    isEqual = 3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def getRatioOfCondition(arr,condition):
    numRation = 0
    countItem = 0
    for item in arr:
        if getConditionStatement(item,condition):
            countItem = countItem +1
    numRation = countItem / len(arr)
    return numRation

def getConditionStatement(item,condition):
    if condition == Condition.isPositive: return (item > 0)
    if condition == Condition.isEqual: return (item == 0)
    if condition == Condition.isNegative: return (item < 0)
    return False
    
def plusMinus(arr):
    ratios = []
    ratios.append(getRatioOfCondition(arr=arr,condition=Condition.isPositive))
    ratios.append(getRatioOfCondition(arr=arr,condition=Condition.isNegative))
    ratios.append(getRatioOfCondition(arr=arr,condition=Condition.isEqual))    
    for ratioItem in ratios:
        print(str(ratioItem) [:_lenghtOfFloat]);

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
