#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zero_count = 0
    minus_count = 0
    positive_count = 0
    for num in arr:
        if num==0:
            zero_count += 1
        elif num<0:
            minus_count += 1
        else:
            positive_count += 1
    
    print(positive_count/len(arr))
    print(minus_count/len(arr))
    print(zero_count/len(arr))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
