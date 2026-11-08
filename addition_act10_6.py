print("Masukkan dua angka, nanti saya jumlahkan.")

first_number = input("Angka pertama: ")
second_number = input("Angka kedua: ")

try:
    total = int(first_number) + int(second_number)
except ValueError:
    print("Maaf, kamu harus memasukkan angka, bukan teks.")
else:
    print(f"Hasil penjumlahan: {total}")