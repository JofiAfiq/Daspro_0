#jofi tri fathan afiq
#2510457

def linearSearch(array, cariBarang):
    for i in range(len(array)):
        if array[i]== cariBarang:
            return i
    return -1

array = ("mainan","palu","obeng","lakban","keyboard","mouse","laptop","headphone","headset","kacamata","meja","kursi","kabel","handphone","monitor")
cari = input("Masukkan Barang yang Ingin dicari: ")
result = linearSearch(array, cari)
#search, but searched in order dari 0 sampe 5
if result != -1:
    print(f"Stok {cari} ditemukan pada index ke-{result}")
else:
    print(f"Stok {cari} tidak ditemukan dalam array.")     