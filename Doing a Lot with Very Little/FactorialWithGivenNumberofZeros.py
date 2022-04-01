
'''
Factorial:
n! = 1 * 2 * 3 * ... *( n - 1 ) * n
              0! = 1
0's at the end
factorial(5) = 120 -> 1 cero
factorial(100) = 24
    933262154439441526816992388562667
    0049071596826438162146859296389521
    75999932299156089414639761565182862
    53697920827223758251185210916864
   --> 000000000000000000000000 <---

0 = 2 * 5
00 = 2^2 * 5^5
000 = 2^3 * 5^3
Factors of 2 and 5
Factor of 5 is enought

21 factorial
() factor of 2
[] factor of 5
1,(2),3,(4),[5],(6),7,(8),9,([10]),11,(12),13,(14),[15],(16),17,(18),19,([20]),21
more factor of 5 than factor of 2

zeros(n) = n/s + n/s^2 + n/s^3 + ... 

Linear solution: while zeros(n) < num_zeros: n+ =1
zeros(24) = 4, zeros(25) = 6
zeros(n) < zeros(n + something) ?
Binary search, so search the answer

// Floor division means dividing and rounding down to the nearest integer
'''

def zeros(n):
    num_zeros = 0
    while n:
        num_zeros += n // 5
        n //= 5
    return num_zeros

def linear_search(num_zeros):
    n = 0
    #print("n:", n)
    #print("num_zeros:", num_zeros)
    while zeros(n) < num_zeros:
        n += 1

    if zeros(n) == num_zeros:
        return n 
    return None

def binary_search(num_zeros):
    left = 0
    right = 5*num_zeros
    while left < right:
        middle = (left + right) // 2
        if zeros(middle) < num_zeros:
            left = middle + 1
        else:
            right = middle 
    if zeros(left) == num_zeros:
        return left
    return None

def numberOfEndZeros(timesFive):
    print('algo')


for i in range(125):
    print(i, binary_search(i))
    assert binary_search(i) == linear_search(i)


def triailingZeros(A):
    count = 0
    for i in range(0, A+1, 5):
        while i % 5 == 0 and i:
            i //=5
            count +=1
    return count

print('\n ** triailingZeros **')
print(triailingZeros(495))
