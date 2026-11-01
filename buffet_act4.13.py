foods = ("rice", "noodles", "fried chicken", "salad", "soup")

for food in foods:
    print(food)

# Coba ubah satu item. Hapus tanda # di bawah, jalankan, lihat errornya,
# lalu beri # lagi:
# foods[0] = "bread"
# Hasil: TypeError: 'tuple' object does not support item assignment

# Menu baru: fried chicken dan soup diganti
foods = ("rice", "noodles", "grilled fish", "salad", "pudding")

print("\nRevised menu:")
for food in foods:
    print(food)