'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to 10^-4 are acceptable.

Example
arr =[1, 1, 0, -1, -1]
There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000 , and
2/5 = 0.400000 and 1/5 = 0.200000.  Results are printed as:

0.400000
0.400000
0.200000

__Function Description__

Complete the plusMinus function in the editor below.
plusMinus has the following parameter(s):
    int arr[n]: an array of integers

__Print__
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6
digits after the decimal. The function should not return a value.

__Input Format__

The first line contains an integer,
, the size of the array.
The second line contains space-separated integers that describe aar[n]

.

__Constraints__
0 < m <= 100
-100 <= arr[i] <= 100

__Output Format__
Print the following 3 lines, each to 6 decimals:

    1.proportion of positive values
    2.proportion of negative values
    3.proportion of zeros

__Sample Input__

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

__Sample Output__

0.500000
0.333333
0.166667

Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: 2/6 = 0.500000 , negative: 2/6 =0.333333 and zeros: 1/6 = 0.166667. 
'''


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
    length_A = len(arr)
    negative = len(list(filter(lambda x: (x<0), arr)))
    positive = len(list(filter(lambda x: (x>0), arr)))
    zero = len(list(filter(lambda x: (x==0), arr)))
    
    ratio_N = negative / length_A
    ratio_P = positive / length_A
    ratio_Z = zero / length_A
    
    print("%.6f" % ratio_N)
    print("%.6f" % ratio_P)
    print("%.6f" % ratio_Z)

if __name__ == '__main__':
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
