#Jofi Tri Fathan Afiq
#2510457
#kelas 1A

percobaan = 3

while percobaan > 0:
    print("Silakan Login!")
    username = (input("Masukkan Username Anda: "))
    password = (input("Masukkan Password Anda: "))

    if username == "Techno" and password == "works123":
        print("Login Berhasil! Selamat datang did sistem TechnoWorks!")
        break
    else:
        percobaan -= 1
        if percobaan > 0:
            print(f"Login Salah! Kesempatan tersisa {percobaan} kali lagi.\n")
        
        else:
            print("Akses ditolak. Anda telah gagal login 3 kali. Silakan hubungi Kepala HRD untuk mereset Password")