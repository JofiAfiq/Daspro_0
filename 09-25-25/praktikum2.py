students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

prodis = {}
for name, prodi in students.items():
    if prodi not in prodis:
        prodis[prodi] = 1
    else:
        prodis[prodi] += 1

for prodi, jumlah in prodis.items():
    print(f"prodi {prodi} sebanyak {jumlah}")