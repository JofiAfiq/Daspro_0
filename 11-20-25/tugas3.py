#jofi tri fathan afiq
#2510457

import time

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34,
35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63,
65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85,90,93, 100
]

target = 60

#Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

start = time.time()
linear_result = linear_search(array, target)
linear_time = time.time() - start


#Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

start = time.time()
binary_result = binary_search(array, target)
binary_time = time.time() - start


print("Hasil Linear Search:")
print("Index =", linear_result)
print("Execution time =", linear_time)

print("\nHasil Binary Search:")
print("Index =", binary_result)
print("Execution time =", binary_time)
