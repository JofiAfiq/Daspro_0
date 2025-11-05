#jofi tri fathan afiq
#2510457

jammulai = int(input("Jam mulai: "))
menitmulai = int(input("Menit mulai: "))
detikmulai = int(input("Detik mulai: "))
print("")
jamselesai = int(input("Jam selesai: "))
menitselesai = int(input("Menit selesai: "))
detikselesai = int(input("Detik selesai: "))

totalmulai = jammulai * 3600 + menitmulai * 60 + detikmulai
totalselesai = jamselesai * 3600 + menitselesai * 60 + detikselesai

selisih = totalselesai - totalmulai

# konversi kembali ke jam, menit, detik
jam = selisih // 3600
selisih %= 3600
menit = selisih // 60
detik = selisih % 60

print(f"Selisih: {jam} jam - {menit} menit - {detik} detik")
