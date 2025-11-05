#jofi tri fathan afiq
#2510457
#1A


total_meningkat = 0
hari_turun = 0
hari_sebelumnya = None

while True:
    tugas = int(input("Input Jumlah Tugas: "))

    if hari_sebelumnya is None:
        hari_sebelumnya = tugas
        continue

    if tugas > hari_sebelumnya:
        total_meningkat += tugas
        hari_turun = 0  
    else:
        hari_turun += 1

    hari_sebelumnya = tugas

    if hari_turun >= 3:
        break

if total_meningkat > 80:
    kategori = "Baik"
elif total_meningkat >= 30:
    kategori = "Cukup"
else:
    kategori = "Kurang"

print("\nTotal tugas yang meningkat:", total_meningkat)
print("Kategori:", kategori)
