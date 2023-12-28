import os
import time
import csv

# Program utama
data_laundry = 'laundries.csv'
data_Paket = 'wash_packets.csv' 

#=====================================================================
def pause():
    os.system("pause")
    
def border(teks):
    print(f'''
=====================
{teks}
=====================''')

def printMenu(*menu):
    for i in range(len(menu)):
        print(f"[{i+1}] {menu[i].title()}")
        time.sleep(0.0125)
    print()

def tampilkan_data_laundry():
    with open(data_laundry, 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['id'] == '2':
                print(row)
#=====================================================================


def edit_data_laundry():
    while True:
        os.system("cls")
        border("Edit Data")
        tampilkan_data_laundry()

        # Membaca data asli dari file CSV
        with open(data_laundry, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Menemukan indeks baris yang sesuai dengan id=2
        index_to_edit = None
        for i, row in enumerate(rows):
            if row['id'] == '2':
                index_to_edit = i
                break

        if index_to_edit is not None:
            # Input untuk nama baru
            nama_baru = input("Masukkan nama baru (kosongkan untuk menggunakan nilai sebelumnya): ")
            if nama_baru != "":
                rows[index_to_edit]['nama'] = nama_baru

            # Input untuk wilayah baru
            wilayah_baru = input("Masukkan wilayah baru (kosongkan untuk menggunakan nilai sebelumnya): ")
            if wilayah_baru != "":
                rows[index_to_edit]['wilayah'] = wilayah_baru

            # Menyimpan data yang diperbarui ke file CSV
            with open(data_laundry, 'w', newline='') as file:
                fieldnames = ['id', 'nama', 'wilayah']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(rows)

            print("Data telah berhasil diubah.")
            pause()
            main2()
        else:
            print("Data dengan id=2 tidak ditemukan.")
            pause()
            main2()
        
def hapus_data_laundry():
    os.system("cls")
    border("Edit Data")
    tampilkan_data_laundry()

    # Membaca data asli dari file CSV
    with open(data_laundry, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Menemukan indeks baris yang sesuai dengan id=2
    index_to_remove = None
    for i, row in enumerate(rows):
        if row['id'] == '2':
            index_to_remove = i
            break
        
    if index_to_remove is not None:
            # Menghapus baris yang sesuai dengan id=2
            del rows[index_to_remove]

            # Menyimpan data yang telah dihapus kembali ke file CSV
            with open('laundries.csv', 'w', newline='') as file:
                fieldnames = ['id', 'nama', 'wilayah']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Menulis header
                writer.writeheader()

                # Menulis baris-baris data yang tersisa
                writer.writerows(rows)

            print("Data telah berhasil dihapus.")
            pause()
            main2()
    else:
        print("Data dengan id=2 tidak ditemukan.")
        pause()
        main2()
    
def lihat_paket():
    os.system("cls")
    border("Lihat Paket")
    with open(data_Paket, 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['id_laundry'] == '2':
                print(row)
    pause()
    main2()

def tambah_paket():
    while True:
        os.system("cls")
        border("Tambah Paket")
        try:
            # Baca data terakhir dari file CSV
            with open(data_Paket, 'r', newline='') as file:
                reader = csv.DictReader(file)
                data_terakhir = list(reader)[-1] if any(reader) else {}

            # Dapatkan ID terakhir
            id_terakhir = int(data_terakhir.get("id", 0))

            # Dapatkan ID_Laundry terakhir
            id_laundryTerdaftar = int(data_terakhir.get("id_laundry", 0))

            # Tambahkan satu ke ID terakhir untuk mendapatkan ID baru
            id_baru = id_terakhir + 1

            id_laundry = 2
            nama_paket = input("Masukkan Nama Paket: ")
            durasi_paket = int(input("Masukkan Durasi Paket: "))
            harga_paket = int(input("Masukkan Harga Paket: "))
            unit_paket = input("Masukkan Unit Paket: ")

            if id_laundry < 1 or id_laundry > id_laundryTerdaftar:
                print("ID_Laundry tidak tersedia. Silakan masukkan ID Laundry yang benar.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            else:
                # Tambahkan data baru ke file CSV
                with open(data_Paket, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([id_baru, id_laundry, nama_paket, durasi_paket, harga_paket,unit_paket])

                print("Paket baru berhasil ditambahkan.")
        except ValueError:
            print("Masukan tidak valid. Pastikan durasi dan harga berupa angka.")

        input("Tekan Enter untuk melanjutkan...")
        main2()

def edit_paket():
    while True:
        os.system("cls")
        border("Edit Paket")

        # Baca data dari file CSV dengan id_laundry 2
        with open("wash_packets.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            relevant_rows = [row for row in reader if int(row['id_laundry']) == 2]

        # Tampilkan data paket dengan id_laundry 2
        for row in relevant_rows:
            print(row)

        id_paket = int(input("\nMasukkan ID paket yang ingin diubah: "))

        # Filter data yang sesuai dengan ID paket yang dimasukkan pengguna
        selected_row = next((row for row in relevant_rows if int(row['id']) == id_paket), None)

        if not selected_row:
            print("Nomor baris tidak valid. Silakan masukkan nomor baris yang benar.\n")
            input("Tekan Enter untuk melanjutkan...")
            continue

        nama_baru = input("\nMasukkan nama baru (kosongkan untuk menggunakan nilai sebelumnya): ")
        durasi_baru = input("Masukkan Durasi: ")
        harga_baru = input("Masukkan harga baru (kosongkan untuk menggunakan nilai sebelumnya): ")
        unit_baru = input("Masukkan unit baru (kosongkan untuk menggunakan nilai sebelumnya): ")

        # Perbarui data yang sesuai
        if nama_baru:
            selected_row['nama'] = nama_baru

        if harga_baru:
            selected_row['harga'] = harga_baru

        if unit_baru:
            selected_row['unit'] = unit_baru
        
        if durasi_baru:
            selected_row['durasi'] = durasi_baru

        # Menyimpan data yang diperbarui kembali ke file CSV
        with open("wash_packets.csv", 'w', newline='') as file:
            fieldnames = relevant_rows[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(relevant_rows)

        print("\nData paket telah berhasil diubah.")
        pause()
        main2()

def hapus_paket():
    while True:
        os.system("cls")
        border("Hapus Paket")

        with open("wash_packets.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
        
            for row in reader:
                if row['id_laundry'] == '2':
                    print(row)

        id_paket = int(input("Masukkan ID paket yang ingin dihapus: "))

        # Baca data dari file CSV
        with open("wash_packets.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            data_Paket = list(reader)

        # Cari indeks baris yang sesuai dengan ID paket yang ingin dihapus
        index_to_remove = None
        for i, row in enumerate(data_Paket):
            if int(row["id"]) == id_paket:
                index_to_remove = i
                break

        if index_to_remove is not None:
            # Hapus baris dengan indeks yang sesuai
            del data_Paket[index_to_remove]

            # Menyimpan data yang diperbarui kembali ke file CSV
            with open("wash_packets.csv", 'w', newline='') as file:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data_Paket)

            print("\nData paket telah berhasil dihapus.")
        else:
            print("ID paket tidak ditemukan. Silakan masukkan ID paket yang benar.")

        pause()
        main2()

#Program UTAMA
def main1():
    while True:
        os.system("cls")
        border("MENU UTAMA")
        printMenu("Tampikan Laundry", "Keluar")
        pilihan= input("Masukan Opsi (1/2): ")
        if pilihan == "1":
            main2()
        elif pilihan == "2":
            break

def main2():
    while True:
        os.system("cls")
        border("SELAMAT DATANG")
        tampilkan_data_laundry()
        printMenu("Edit Data Laundry", "Hapus Data Laundry", "Lihat Paket", "Tambah Paket", "Edit Paket", "Hapus Paket", "Kembali")
        pilihan = input("> ")
        if pilihan == "1":
            edit_data_laundry()
        elif pilihan == "2":
            hapus_data_laundry()
        elif pilihan == "3":
            lihat_paket()
        elif pilihan == "4":
            tambah_paket()
        elif pilihan == "5":
            edit_paket()
        elif pilihan == "6":
            hapus_paket()
        elif pilihan == "7":
            main1()
        
main1()