import csv
from ..files import files as fl

data_users = fl.read_from_csv("users.csv")
def login():
    print("\nLogin")
    username = input("Username :")
    password = input("Password :")
    for data_user in data_users:
        if data_user['username'] == username and data_user['password'] == password:
            return data_user
        
    print("Username atau Password salah\n")
    return False

def regist():
    print("\nRegister")
    id = fl.get_max_id("users.csv") + 1
    nama = input("Nama : ")
    username = input("Username : ")
    password = input("Password : ")
    data_user = {
        "id": id,
        "nama": nama,
        "username": username,
        "password": password,
        "role": 1,
    }
    data_users.append(data_user)
    fl.write_to_csv("users.csv", data_users)
    print("Registrasi Berhasil\n")

def printRole(user):
    if user['role'] == '1':
        return 'user'
    elif user['role'] == '2':
        return 'mitra'
    elif user['role'] == '3':
        return 'admin'

def menuLogin():
    print("SUDAH PUNYA AKUN?")
    print("0. Keluar")
    print("1. Login")
    print("2. Daftar")
    pilihan = input("Masukan Opsi: ")

    if pilihan == "1":
        return login()
    elif pilihan == "2":
        regist()
        menuLogin()
    elif pilihan == "0":
        exit()
    else:
        print("Opsi Tidak ditemukan\n")