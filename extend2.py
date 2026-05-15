def input_data():
    data = []
    jumlah = int(input("Jumlah mahasiswa: "))

    for i in range(jumlah):
        nilai = float(input(f"Nilai mahasiswa {i+1}: "))
        data.append(nilai)

    return data


def hitung_nilai(data):
    # contoh sederhana: bisa dikembangkan (misalnya bobot)
    # di sini tetap dikembalikan langsung
    return data


def bubble_sort(data):
    n = len(data)
    count = 0  # menghitung jumlah perbandingan

    for i in range(n):
        for j in range(0, n - i - 1):
            count += 1
            if data[j] < data[j + 1]:  # sorting descending
                data[j], data[j + 1] = data[j + 1], data[j]

    print("Jumlah perbandingan Bubble Sort:", count)
    return data


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def tampilkan_data(data):
    print("\nData nilai mahasiswa (terurut):")
    for i in range(len(data)):
        print(f"{i+1}. {data[i]}")


# =========================
# PROGRAM UTAMA
# =========================

data = input_data()
data = hitung_nilai(data)
data = bubble_sort(data)
tampilkan_data(data)

target = float(input("\nCari nilai: "))
posisi = linear_search(data, target)

if posisi != -1:
    print("Nilai ditemukan pada posisi (index):", posisi)
else:
    print("Nilai tidak ditemukan")