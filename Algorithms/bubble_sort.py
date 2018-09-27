#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numSwaps = 0
    j = 0
    while j < len(a)-1:
        i = 0
        while i < len(a)-1 - j:
            if a[i] > a[i+1]:
                numSwaps+=1
                a[i], a[i+1] = a[i+1], a[i]
            i+=1
        j+=1
    return (numSwaps, a)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))
    result, b = countSwaps(a)
    print('Array is sorted in', result, 'swaps.')
    print('First Element:', b[0])
    print('Last Element:', b[len(a)-1])
