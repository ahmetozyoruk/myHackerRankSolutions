#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    temp = 0
    resultGrades = []
    
    for grade in grades:
        temp = 0
        
        if grade < 37:
            resultGrades.append(grade)
            continue
        
        temp = 5 - (grade % 5)
        
        if temp < 3:
            grade = grade + temp
            
        resultGrades.append(grade)
        
        
    return resultGrades
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
