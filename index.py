from controllers.auth import auth
from controllers.admin import crud_adm as ca
from controllers.laundry import daftar as df
from controllers.laundry import crud_mitra as cm
from controllers.order import order as od

def startingPoint():
    user = None
    user = auth.menuLogin()

    while user is None or user is False:
        user = auth.menuLogin()
    while user != {}:
        if user['role'] == '3':
            print(f"Selamat Datang {auth.printRole(user)} {user['nama']}")
            ca.menuAdmin()
            user = {}
            print("Berhasil keluar\n")
        elif user['role'] == '2':
            print(f"Selamat Datang {auth.printRole(user)} {user['nama']}")
            cm.main(user['id'])
            user = {}
            print("Berhasil keluar\n")
        elif user['role'] == '1':
            print(f"Selamat Datang {auth.printRole(user)} {user['nama']}")
            print("\nMenu Pelanggan")
            print("0. Keluar")
            print("1. Order")
            print("2. Buka Laundry")
            mainMenu = input("Masukkan pilihan: ")
            if mainMenu == "1":
                od.menu(user['id'])
            elif mainMenu == "2":
                df.laundries(user['id'])
            else:
                user = {}
                print("Berhasil keluar\n")
                startingPoint()

while True:
    startingPoint()