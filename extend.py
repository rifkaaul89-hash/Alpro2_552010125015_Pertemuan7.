def input_data():
    data = []
    jumlah = int(input("Jumlah mahasiswa:"))
    for i in range(jumlah):
        nilai = float(input(f"Nilai mahasiswa {i+1}:"))
        data.append(nilai)
    return data

def hitung_nilai(data):
    return data #Simulasi sederhana

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def linear_search(data, target):
    for i in range(len(data)):
        if data [i] == target:
            return i
    return -1

def tampilkan_data(data):
    print("Data nilai mahasiswa (terurut):", data)

#program utama
data = input_data()
data = hitung_nilai(data)
data = bubble_sort(data)
tampilkan_data(data)

target = float(input("Cari nilai:"))
posisi = linear_search(data, target)

print("Posisi:", posisi)