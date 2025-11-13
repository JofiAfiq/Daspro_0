import numpy as np

nilai = np.random.randint(50, 101, 30)

print("Data nilai ujian (acak, belum diurutkan):")
print(nilai)

nilai_urut = np.sort(nilai)[::-1]

print("\nNilai ujian setelah diurutkan (terbesar → terkecil):")
print(nilai_urut)

lima_tertinggi = nilai_urut[:5]

print("\n5 Nilai tertinggi:")
print(lima_tertinggi)
