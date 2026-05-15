def input_data():
    data = []
    jumlah = int(input"Jumlah mahasiswa"))
    for i in range(jumlah):
        nilai = float(input(g"Nilai mahasiswa {i+1}:"))
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
    return -1
def tampilkan_data(data):
    print("Data:", data)