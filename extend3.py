def input_data():
    data = []
    jumlah = int(input("Jumlah mahasiswa: "))

    for i in range(jumlah):
        nilai = float(input(f"Nilai mahasiswa {i+1}: "))
        data.append(nilai)

    return data


def hitung_nilai(data):
    # simulasi sederhana (bisa dikembangkan dengan bobot)
    return data


def insertion_sort(data):
    count = 0  # menghitung perbandingan

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # sorting DESCENDING (nilai terbesar ke terkecil)
        while j >= 0:
            count += 1
            if data[j] < key:
                data[j + 1] = data[j]
                j -= 1
            else:
                break

        data[j + 1] = key

    print("Jumlah perbandingan Insertion Sort:", count)
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
data = insertion_sort(data)
tampilkan_data(data)

target = float(input("\nCari nilai: "))
posisi = linear_search(data, target)

if posisi != -1:
    print("Nilai ditemukan pada posisi (index):", posisi)
else:
    print("Nilai tidak ditemukan")