def binarySearch(array, cariNilai):
    indexLow, indexHigh = 0, len(array) -1

    while indexLow <= indexHigh:
        middle = (indexLow + indexHigh) // 2
        middleValue = array[middle]

        if middleValue == cariNilai:
            return middle
        elif middleValue < cariNilai:
            indexLow = middle + 1
        else:
            indexHigh = middle -1
    return -1

sortedArray = (0,6,4,7,8,9,1,2,5,3)
cari = 4
result = binarySearch(sortedArray, cari)    

if(result != -1):
    print(f"Nilai {cari} ditemukan pada index ke-{result}.")
else:
    print(f"Nilai {cari} tidak ditemukan dalam array.")