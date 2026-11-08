print("Kalkulator penjumlahan. Ketik 'q' kapan saja untuk keluar.")

while True:
    first_number = input("\nAngka pertama: ")
    if first_number == "q":
        break

    second_number = input("Angka kedua: ")
    if second_number == "q":
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Maaf, kamu harus memasukkan angka, bukan teks.")
    else:
        print(f"Hasil penjumlahan: {total}")