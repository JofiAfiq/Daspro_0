def linearSearch(array, cariNilai):
    for i in range(len(array)):
        if array[i]== cariNilai:
            return i
    return -1

array = [0,1,2,3,4,5]
nilai = 3
result = linearSearch(array, nilai)
#search, but searched in order dari 0 sampe 5
if(result != -1):
    print(f"Nilai {nilai} ditemukan pada index ke-{result}")
else:
    print(f"Nilai {nilai} tidak ditemukan dalam array.")     