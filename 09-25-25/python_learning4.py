kucing = {
    "nama": "Rainbow Dash",
    "umur": 22,
    "ras": "Pegasus",
    "betina": True,
    "cantik": True,
    "hobi": ["makan", "tidur"]
}

# print(kucing)
# print(len(kucing))

# buah = dict(nama = "Apel", warna = "Merah", manis = True)
# print(buah)

kuda = dict(name = "Rainbow Dash", color = "Cyan", awesome = True, howmuch = "20%", hobby = ["Flying", "Eating", "Sex"])
print(kuda['name'])
print(kuda.get("color"))
print(kuda["hobby"][2]) 
# print(kucing["hobi"][1])

# print(kucing.keys())
# print(kuda.keys())
# print(kuda.values())

kucing["umur"]=18
kucing["anak"]=4
kucing["warna"]="Cyan"

kucing.update({"umur": 19})
kucing.update({"warna": ["Pink"]})


x = kucing.items()
print(x)

if"nama" in kucing:
    print("Ada key 'nama' pada dictionary")

kucing.pop("cantik")
print(kucing)