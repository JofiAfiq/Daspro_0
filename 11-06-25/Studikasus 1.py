import numpy as np

suhu_celcius = np.array([30.5, 31.2, 29.8, 32.0, 33.1, 30.9, 29.5, 31.7, 32.8, 30.2])

suhu_fahrenheit = (suhu_celcius * 9/5) + 32

print("Suhu dalam Celcius:")
print(suhu_celcius)

print("\nSuhu dalam Fahrenheit:")
print(suhu_fahrenheit)
