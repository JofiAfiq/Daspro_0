#jofi tri fathan afiq
#2510457

data = input("Masukkan angka, pisahkan dengan koma: ")

angka = [float(x) for x in data.split(",")]

total = sum(angka)

rata_rata = total / len(angka)

print("Total:", total)
print("Rata-rata:", rata_rata)
