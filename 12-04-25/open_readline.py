with open("folder/oldfile.txt", "r") as file:
    content = file.read()
print(content)

with open ("folder/oldfile.txt","a") as file:
    file.write("Tulisan ini baru ditambahkan pada file yang sudah ada")

print("\n----------------------------------------------------------------\n")

with open("folder/oldfile.txt","r") as file:
    content = file.read()
print(content)