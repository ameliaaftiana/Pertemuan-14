import re

def proses_email(email): #harus return tuple (username,host)
    email_split = email.split("@")
    return (email_split[0], email_split[1])

def pakai_regex(email):
    pattern = r"(.+)@(.+)" #ambil semua yang dipisahkan @


#input user
email = input("Masukkan alamat email yang valid")
hasil = proses_email(email)

print (f"Username: {hasil[0]}")
print (f"Hostname: {hasil[1]}")

