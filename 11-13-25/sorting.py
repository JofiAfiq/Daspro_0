def bubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            # if array [j] > array [j+1]: #ascending
            if array [j] < array [j+1]: #descending
                array[j], array[j + 1] = array [j+1], array [j]

    return array

unordered = [5,3,2,1,6,4,0,9,7,8]
print(bubbleSort(unordered))

def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_idx = 1
        for j in range (i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# unordered = [1,9,2,8,3,7,4,6,5,0]
print (selectionSort(unordered))