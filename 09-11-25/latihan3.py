celsius = float(input("Masukkan suhu dalam Celsius : "))
# print(celsius)
reamur = float(celsius * 4/5)
fahrenheit = float(celsius * 9/5 + 32)
kelvin = float(celsius + 273)

print(f"Suhu {celsius} sama dengan \n{reamur}° reamur \n{fahrenheit}° fahrenheit \n {kelvin} kelvin")
