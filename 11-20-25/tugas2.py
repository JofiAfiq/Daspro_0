#jofi tri fathan afiq
#2510457

def binarySearch(array, mahasiswa):
    indexLow, indexHigh = 0, len(array) -1

    while indexLow <= indexHigh:
        middle = (indexLow + indexHigh) // 2
        middleValue = array[middle]

        if middleValue == mahasiswa:
            return middle
        elif middleValue < mahasiswa:
            indexLow = middle + 1
        else:
            indexHigh = middle -1
    return -1

sortedArray = ["Faris","Mario","Jofi","Ahnaf","Aldi","Firdaus","Azka","Fadhil","Syamil","Syauqi","Dzikri","Farhan","Sulthan","Azzuri","Brasco","Putra","Wahyu","Afiq",
"Adel","Gaitha","Arkan"
]
sortedArray = sorted(sortedArray)

cari = input("Input nama Mahasiswa (huruf pertama kapital): ")
result = binarySearch(sortedArray, cari)    

if result != -1:
    print(f"Nilai {cari} ditemukan pada index ke-{result}.")
else:
    print(f"Nilai {cari} tidak ditemukan dalam array.")