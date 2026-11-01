# 3-11. Intentional Error
# Sebelumnya: print(names[3]) -> IndexError: list index out of range
# Penyebab: list hanya punya indeks 0, 1, dan 2
# Perbaikan: pakai names[2] (item terakhir)

names = ["Andi", "Budi", "Citra"]
print(names[2])