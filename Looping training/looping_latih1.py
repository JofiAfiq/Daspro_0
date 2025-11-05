#jofi tri fathan afiq
#2510457

angka = int(input("Masukkan Jumlah Hewan yang Akan Diinput: "))
daftar_hewan = []

for i in range(1, angka + 1):
    hewan = input(f"Masukkan hewan ke-{i}: ")
    daftar_hewan.append(hewan)

for i in range(1, angka + 1):
    print(f"Hewan ke-{i} adalah {daftar_hewan[i-1]}")