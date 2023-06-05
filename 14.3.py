import re


def replace_kata(kata_lama, kata_baru,artikel):
    artikel = re.sub(kata_lama,kata_baru,artikel)
    return artikel 

#baca isi file txt dalam bentuk string
def baca_file(nama_file):
    handle = open(nama_file)
    artikel = handle.read()
    return artikel

def update_file(nama_file,artikel):
    handle = open(nama_file,'w')
    handle.write(artikel)
    handle.close()


#input nama file
nama_file = input("Masukkan nama file: ")
artikel = baca_file(nama_file)

#input kata yang mau direplace
kata_lama = input("Masukkan kata yang akan direplace: ")
kata_baru = input("Masukkan kata penggantinya: ")


#proses utama
hasil = replace_kata(kata_lama, kata_baru,artikel)

#update isi file
update_file(nama_file, hasil)