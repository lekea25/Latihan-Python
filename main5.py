#Fungsi (Function)
'''def sapa(nama):
    print("Halo,", nama, "!")
    print(f"Halo, {nama}!")'''

'''sapa("Eka Lestari")  #Output: Halo, Lekea!'''

'''def tambah(a, b):
    hasil = a + b
    return hasil'''

'''jumlah = tambah(3, 5)
print(jumlah) # Output: 8'''

'''def tambah(a, b):
    hasil = a + b
    return hasil'''

'''jumlah = tambah(3, 5)
hasil_bagi = jumlah / 2
print("Hasil penjumlahan adalah:",jumlah)
print("Hasil pembagian adalah:",hasil_bagi) 
#Output: 8'''


# Cara kaka nya
'''def tambah(a, b, c):
    hasil = (a + b) / c
    return hasil'''

'''jumlah = tambah(3, 5, 2)
print("Hasil penjumlahan adalah:",jumlah)
#Output: 8:4=2'''

# Struktur Data pake LIST
'''buah = ["apel", "pisang", "mangga"]'''

#Mengakses elemen
'''print(buah[0]) # Output: apel'''

#Mengubah elemen
'''buah[1] = "jeruk"
print(buah) # Output: ['apel', 'jeruk', 'mangga']'''

'''buah = ["apel", "pisang", "mangga"]
print(buah[0]) # Output: apel
buah[1] = "jeruk"
print(buah) # Output: ['apel', 'jeruk', 'mangga']'''

'''buah = ["apel", "pisang", "mangga"]'''

'''#Menambahkan dua buah
buah += ["alpukat", "durian"]'''

'''#Menghapus "mangga"
buah.remove("mangga")'''

'''print(buah) # Output: ['apel', 'pisang', 'alpukat', 'durian']'''

# Atau cara

'''fruit = ["apple", "banana", "mango"]
fruit.append("durian")
fruit.append("avocado")'''

'''fruit.remove("mango")
print(fruit)'''

'''# Pake Insert (kalo mau nambahin urutan pertama)
# Menambahkan list baru dengan index tertentu
buah.insert(0, "anggur")'''

'''buah = ["apel", "pisang", "mangga"]
buah[1] = "jeruk"'''
buah.insert(0, "anggur")
buah.append("alpukat")
print(buah)
'''


''' # Struktur data tuple (kurung biasa ())
# angka1 = (1, 2, 3)
# angka2 = (4, 5, 6)
# print (angka1)
# print (angka2)