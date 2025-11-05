def pengurangan (a,b):
    print(a - b)

pengurangan(5,2)
pengurangan(2,5)

print("")

def kelilingsegitiga(a, b, c):
    print(a+b+c) #notice that there are 3 variables

kelilingsegitiga(1,2,3) #there has to be 3 variables here too

print("")

#keyword arguments
def penjumlahan(a,b):
    print(f"Hasilnya adalah {a + b}")

penjumlahan(b = 2, a = 5)

print("")

# arbitrary argument
def funcArgs(*angka):
    print(f"Angka terakhir yang dimasukkan yaitu {angka[-1]}")

funcArgs(1,2,8,9,4,5)

def funcArg(*ankha):
    print(f"Angka yang dimasukkan yaitu {ankha[:]}")

funcArg(1, 2, 8, 9, 4, 5)

#arbitrary keyword arguments
def funcKwargs(**angka):
    print(f"Angka ketiga yaitu {angka['ketiga']}")

funcKwargs(pertama = 1, kedua = 2, ketiga = 3, keempat = 4)
print("")
#argument from list
def namaBuah(buah):
    for i in buah:
        print(i)

buah = ["apel","anggur","jeruk","mangga"]
namaBuah(buah)

