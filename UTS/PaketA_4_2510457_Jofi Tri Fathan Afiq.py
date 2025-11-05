# jofi tri fathan afiq
# 2510457
# 1A

print("--- Rekapitulasi Gaji Karyawan ---")

karyawan = int(input("Masukkan jumlah karyawan: "))

total_adit = 0
adit_tertinggi = 0
nama_tertinggi = ""

for i in range(1, karyawan + 1):
    print(f"\n-- Karyawan ke-{i} --")
    nama = input("Nama: ")
    adit = int(input("Gaji: "))

    total_adit += adit

    if adit > adit_tertinggi:
        adit_tertinggi = adit
        nama_tertinggi = nama

rata_rata = total_adit / karyawan

print("\n--- Laporan Gaji ---")
print("Total Gaji Seluruh Karyawan: Rp", total_adit)
print("Rata-rata Gaji: Rp", rata_rata)
print("Karyawan dengan Gaji Tertinggi:", nama_tertinggi)
