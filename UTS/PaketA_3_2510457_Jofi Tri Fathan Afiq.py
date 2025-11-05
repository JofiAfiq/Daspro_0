#jofi tri fathan afiq
#2510457
#1a

genap = 0
ganjil = 0
hari = 1

while hari <=7:
    jam = int(input(f"Input lembur : "))

    if jam>0:
        if hari%2==0:
            genap+=jam
        else:
            ganjil+=jam
    hari+=1

print(f"Total jam lembur pada tanggal genap : {genap}")
print(f"Total jam lembur pada tanggal ganjil : {ganjil}")

#15+25+20+20 = 80
#
