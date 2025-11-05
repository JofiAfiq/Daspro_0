students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

student_info = {
    "Alice":{"age": 20, "major": "Computer Science"},
    "Bob": {"age":21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}
name = input("Masukkan Nama Siswa: ")

if name in student_info:
    age = student_info[name]["age"]
    major = student_info[name]["major"]
    print(f"Umur {name} adalah {age} dan Prodinya adalah {major}")