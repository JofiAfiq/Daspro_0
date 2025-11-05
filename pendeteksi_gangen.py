#Jofi Tri Fathan Afiq
#2510457
angka = int(input("Masukkan sebuah bilangan: "))

if angka > 0:
    sifat = "positif"
elif angka < 0:
    sifat = "negatif"
else:
    sifat = "nol"

if angka % 2 == 0:
    jenis = "genap"
else:
    jenis = "ganjil"

if angka == 0:
    print("Bilangan tersebut adalah nol (tidak termasuk ganjil maupun genap).")
else:
    print(f"{angka} adalah bilangan {jenis} dan {sifat}.")
