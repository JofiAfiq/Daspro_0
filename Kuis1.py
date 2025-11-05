# Nama    : Jofi Tri Fathan Afiq
# NIM     : 2510457
# Kelas   : 1A
# Paket   : A


    # 1. 
# minute = float(input("Masukkan Menit :"))
# second = minute * 60

# third = float(input("Masukkan Detik :"))
# fourth = second + third

# print(fourth)


    # 2. 
# panjang = float(input("Masukkan Panjang: "))
# tinggi = float(input("Masukkan Tinggi: "))
# lebar = float(input("Masukkan Lebar: "))
# luas = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)
# # print(luas)
# harga = luas * 580000
# print(f"Rp{harga}")


    # 3. 
# jualan = {"kerudung", "kemeja", "rok", "celana_panjang", "baju_renang","topi","tas","sepatu","kacamata"}
# bulan = {"ikat_rambut","sandal"}
# jualan.add("Piyama")
# jualan.update(bulan)
# print(jualan)
# print(len(jualan))

    # 4. 
# print("Mobil lama Pak Oki adalah: \nMerk : Honda \nTipe : HRV\nWarna : Hitam\nTahun : 2018")
# merk = str(input("Masukkan Merk Mobil       : "))
# tipe = str(input("Masukkan Tipe Mobil       : "))
# warna = str(input("Masukkan Warna Mobil     : "))
# tahun = int(input("Masukkan Tahun Mobil     : "))

# # print(f"{mobil}, {merk}, {tipe}, {warna}, {tahun}")s
# print("------------***------------")
# print(f"Mobil baru Pak Oki adalah:\nMerk: {merk}\nTipe: {tipe}\nWarna: {warna}\nTahun: {tahun}")
# print("------------***------------")

    # 5.
nilai = [78, 90, 56, 98, 65, 38, 42, 74, 89, 90]

nomor = int(input("Masukkan nomor urut siswa (1-10): "))

if 1 <= nomor <= len(nilai):
    print(f"Nilai siswa nomor urut {nomor} adalah {nilai[nomor - 1]}")
