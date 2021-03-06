def three_loops(arr):
    n = len(arr)
    max_sum = arr[0]
    for start in range(n):
        for end in range(start, n):
            current_sum = sum(arr[start:end+1])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum




def two_loops(array):
    n = len(array)
    max_sum = array[0]
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += array[end]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def one_loop(array):
    n = len(array)
    max_sum = array[0]
    current_sum = array[0]
    for i in range(1, n):
        #print("current_sum: ",current_sum)
        #print("array[i]: ",array[i])
        current_sum = max(current_sum + array[i], array[i])
        #print("current_sum 2: ",current_sum)
        max_sum = max(max_sum, current_sum)
        #print("max_sum: ",max_sum)
    return max_sum

arr1 = [3, 4, -9, 1, 2]
arr2 = [1, 2, 3]
arr3 = [-1, -2, -3]

print("[1,2,3]")
print(one_loop([1,2,3]))

assert three_loops(arr1) == two_loops(arr1)
assert three_loops(arr2) == two_loops(arr2)
assert three_loops(arr3) == two_loops(arr3)

assert one_loop(arr1) == two_loops(arr1)
assert one_loop(arr2) == two_loops(arr2)
assert one_loop(arr3) == two_loops(arr3)