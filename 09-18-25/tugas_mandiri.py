#Nama   :Jofi Tri Fathan Afiq
#NIM    :2510457

nilai = ["88","75","63","97","82","74","91","80","81","63"]
nilai_int = [int(x) for x in nilai]

nilai.sort()
nilai_besar = nilai[0]
nilai_kecil = nilai[-1]
nilai_ratarata = sum(nilai_int) /  len(nilai_int)

print(f"Nilai mahassiwa terkecil: {nilai_kecil}")
print(f"Nilai Mahasiswa terbesar: {nilai_besar}")
print(f"Nilai rata rata mahasiswa: {nilai_ratarata}")

nilai_kedua = sorted(set(nilai_int), reverse=True)[1]
print(f"Nilai Terbesar kedua: {nilai_kedua}")