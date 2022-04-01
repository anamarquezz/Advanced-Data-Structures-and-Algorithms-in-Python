'''
Given five positive integers, find the minimum and maximum values that can be calculated 
by summing exactly four of the five integers. 
Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.

Example
arr = [1, 3, 5 , 7, 9]
The minimum sum is and the maximum sum is . The function prints
'''


def miniMaxSum(arr):
    # Write your code here    
    arr.sort()
    sumMin = sum(arr[0:4])
    sumMan = sum( arr[1:5])
    print(sumMin,sumMan)


array = [7, 69 ,2 ,221 ,8974]
miniMaxSum(array)