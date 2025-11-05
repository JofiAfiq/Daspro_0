#function-
def penjumlahan(a, b):
    hasil = a + b
    return hasil

penjumlahan(2,3)
print(penjumlahan(2,3))


#procedure-
def greeting(nama):
    print(f"Halo, {nama}!")

greeting("Sasa")

#contoh global variable-
globalVar = 10
def globalFunction():
    print(f"Nilai dari global variable adalah: {globalVar}")

globalFunction()
print(globalVar) #you can print it

#local variable-
def localFunction():
    local = 5
    print(f"Nilai dari local variable adalah: {local}")

localFunction()
              # print(local) #it aint gonna print

