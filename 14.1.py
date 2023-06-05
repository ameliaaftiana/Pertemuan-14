import re

#baca isi file txt dalam bentuk string
def baca_file(nama_file):
    handle = open(nama_file)
    artikel = handle.read()
    return artikel

def proses_regex(artikel):
    pattern = r"\b[A-Zz-z][a-z][a-z][a-z][a-z]" #mencari kata yang panjangnya 5 karakter
    #coba dengan fungsi search
    # hasil = re.search(pattern,artikel) #hanya diambil 1

    #pakai findall = ketemu semua dalam bentuk list
    hasil = re.findall(pattern,artikel)
    print (f"Ditemukan {len(hasil)} kata Jakarta")
    return hasil

#program utama
#minta input nama file
nama_file = input("Masukkan nama file: ")
#proses
artikel = baca_file(nama_file)
hasil = proses_regex(artikel)
hasil = proses_regex(artikel)
#ouput
print (hasil)
