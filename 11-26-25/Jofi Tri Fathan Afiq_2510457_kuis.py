#jofi tri fathan afiq
#2510457

#1. 

# jumlah = int(input("Masukkan jumlah jenis barang: "))


# inventori = []

# for i in range(jumlah):
#     print(f"\nData barang ke-{i+1}")
#     nama = input("Nama barang : ")
#     kode = input("Kode barang : ")
#     stok = int(input("Jumlah stok : "))

#2. 

# kode = []
# nama = []
# stok = []

# jumlah = int(input("Masukkan jumlah jenis barang: "))

# for i in range(jumlah):
#     print(f"\nData barang ke-{i+1}")
#     nama_barang = input("Nama barang : ")
#     kode_barang = input("Kode barang : ")
#     stok_barang = int(input("Jumlah stok : "))

#     nama.append(nama_barang)
#     kode.append(kode_barang)
#     stok.append(stok_barang)

# print("\n=== DAFTAR BARANG DI GUDANG ===")
# if jumlah == 0:
#     print("Belum ada data barang.")
# else:
#     for i in range(jumlah):
#         print(f"[{i}] Kode: {kode[i]}, Nama: {nama[i]}, Stok: {stok[i]}")

#3. 

# kode = ["01", "02", "03", "04", "05", "06", "07"]
# nama = ["meja","botol","mouse","laptop","keyboard","monitor","ketua"]
# stok = [25, 12, 15, 90, 64, 27, 39]

# def sort_stok(kode, nama, stok):
#     n = len(stok)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if stok[i] > stok[j]:
#                 stok[i], stok[j] = stok[j], stok[i]
#                 kode[i], kode[j] = kode[j], kode[i]
#                 nama[i], nama[j] = nama[j], nama[i]

# sort_stok(kode, nama, stok)

# print("=== DAFTAR BARANG DI GUDANG YANG TELAH TERURUT ===")
# for i in range(len(kode)):
#     print(f"[{i}] Kode: {kode[i]}, Nama: {nama[i]}, Stok: {stok[i]}")

#4. 

# kode = ["01", "02", "03", "04", "05", "06", "07"]
# nama = ["meja","botol","mouse","laptop","keyboard","monitor","ketua"]
# stok = [25, 12, 15, 90, 64, 27, 39]

# def sort_stok(kode, nama, stok):
#     n = len(stok)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if stok[i] > stok[j]:
#                 stok[i], stok[j] = stok[j], stok[i]
#                 kode[i], kode[j] = kode[j], kode[i]
#                 nama[i], nama[j] = nama[j], nama[i]

# def cari_barang(nama_dicari, kode, nama, stok):
#     for i in range(len(nama)):
#         if nama_dicari.lower() == nama[i].lower():
#             return i
#     return -1


# sort_stok(kode, nama, stok)

# print("=== DAFTAR BARANG DI GUDANG YANG TELAH TERURUT ===")
# for i in range(len(kode)):
#     print(f"[{i}] Kode: {kode[i]}, Nama: {nama[i]}, Stok: {stok[i]}")

# cari = input("\nInput nama barang: ")
# index = cari_barang(cari, kode, nama, stok)

# if index != -1:
#     print(f"Barang ditemukan: Kode {kode[index]}, Nama {nama[index]}, Stok {stok[index]}")
# else:
#     print("Maaf, barang tidak ada pada inventory kami")


#5. 


kode = ["01", "02", "03", "04", "05", "06", "07"]
nama = ["meja","botol","mouse","laptop","keyboard","monitor","ketua"]
stok = [25, 12, 15, 90, 64, 27, 39]


def sort_stok(kode, nama, stok):
    n = len(stok)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if stok[i] > stok[j]:
                stok[i], stok[j] = stok[j], stok[i]
                kode[i], kode[j] = kode[j], kode[i]
                nama[i], nama[j] = nama[j], nama[i]

def laporan_kritis(batas, kode, nama, stok):
    print(f"\n=== LAPORAN BARANG KRITIS (stok < {batas}) ===")
    jumlah = 0
    for i in range(len(stok)):
        if stok[i] < batas:
            print(f"Kode: {kode[i]}, Nama: {nama[i]}, Stok: {stok[i]}")
            jumlah += 1
    if jumlah == 0:
        print("Tidak ada barang dengan stok di bawah batas minimum.")
    print(f"Jumlah barang kritis: {jumlah}")

sort_stok(kode, nama, stok)

batas = int(input("Masukkan batas minimum stok: "))

laporan_kritis(batas, kode, nama, stok)

