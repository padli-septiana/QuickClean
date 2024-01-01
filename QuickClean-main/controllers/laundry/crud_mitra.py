import os
import time
import csv
from ..files import files as fl
from . import order

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

def tampilkan_data_laundry(id_user):
    laundries = fl.read_from_csv("laundries.csv")
    for row in laundries:
        if row['id_user'] == id_user:
            print(f"{row['nama']} - {row['wilayah']}")
            return row['id']
#=====================================================================


def edit_data_laundry(id_user):
    while True:
        border("Edit Data")
        # Membaca data asli dari file CSV
        laundries = fl.read_from_csv("laundries.csv")

        for laundry in laundries:
            if laundry['id_user'] == id_user:
                print(f"{laundry['nama']} - {laundry['wilayah']}")
                # Input untuk nama baru
                nama_baru = input("Masukkan nama baru (kosongkan untuk menggunakan nilai sebelumnya): ")
                if nama_baru != "":
                    laundry['nama'] = nama_baru

                # Input untuk wilayah baru
                wilayah_baru = input("Masukkan wilayah baru (kosongkan untuk menggunakan nilai sebelumnya): ")
                if wilayah_baru != "":
                    laundry['wilayah'] = wilayah_baru

        # Menyimpan data yang diperbarui ke file CSV
        fl.write_to_csv("laundries.csv", laundries)

        print("Data telah berhasil diubah.")
        pause()
        main(id_user)
        
def hapus_data_laundry(id_user):
    # Membaca data asli dari file CSV
    laundries = fl.read_from_csv("laundries.csv")
    wash_packets = fl.read_from_csv("wash_packets.csv")
    users = fl.read_from_csv("users.csv")
    newLaundry = []
    newPacket = []
    # Menemukan indeks baris yang sesuai dengan id
    for laundry in laundries:
        # Menghapus baris yang sesuai dengan id=2
        if laundry['id_user'] != id_user:
            newLaundry.append(laundry)
            id_laundry = laundry['id']

    # Menemukan indeks baris yang sesuai dengan id
    for paket in wash_packets:
        # Menghapus baris yang sesuai dengan id=2
        if paket['id_laundry'] == id_laundry:
            newPacket.append(paket)

    # mengubah role user
    for user in users:
        if user['id'] == id_user:
            user['role'] = '1'
    
    # Menyimpan data yang telah dihapus kembali ke file CSV
    fl.write_to_csv("users.csv", users)
    fl.write_to_csv("laundries.csv", newLaundry)
    fl.write_to_csv("wash_packets.csv", newPacket)
    print("Data berhasil dihapus")
    pause()
    exit()
    
def lihat_paket(id_laundry):
    border("Lihat Paket")
    reader = fl.read_from_csv("wash_packets.csv")
        
    for row in reader:
        if row['id_laundry'] == id_laundry:
            print(f"{row['nama']} - {row['durasi']} hari - {row['harga']}/{row['unit']}")
    pause()

def tambah_paket(id_laundry):
    border("Tambah Paket")
    
    # Baca data terakhir dari file CSV
    wash_packets = fl.read_from_csv("wash_packets.csv")
    data_terakhir = list(wash_packets)[-1] if any(wash_packets) else {}

    # Dapatkan ID terakhir
    id_terakhir = int(data_terakhir.get("id", 0))

    # Tambahkan satu ke ID terakhir untuk mendapatkan ID baru
    id_baru = id_terakhir + 1

    id_laundry = id_laundry
    nama_paket = input("Masukkan Nama Paket: ")
    durasi_paket = int(input("Masukkan Durasi Paket: "))
    harga_paket = int(input("Masukkan Harga Paket: "))
    unit_paket = input("Masukkan Unit Paket (kg/pasang): ")

    # Tambahkan data baru ke file CSV
    wash_packets.append({
        'id': id_baru,
        'id_laundry' : id_laundry,
        'nama': nama_paket,
        'durasi': durasi_paket,
        'harga': harga_paket,
        'unit': unit_paket,
    })
    fl.write_to_csv("wash_packets.csv", wash_packets)

    print("Paket baru berhasil ditambahkan.")
    pause()

def edit_paket(id_laundry, id_user):
    border("Edit Paket")

    # Baca data dari file CSV dengan id_laundry 2
    rows = fl.read_from_csv("wash_packets.csv")
    relevant_rows = [row for row in rows if row['id_laundry'] == id_laundry]

    while True:
        # Tampilkan data paket dengan id_laundry 2
        for row in relevant_rows:
            print(f"{row['id']}. {row['nama']} - {row['durasi']} hari - {row['harga']}/{row['unit']}")

        id_paket = int(input("\nMasukkan ID paket yang ingin diubah (0 untuk kembali): "))
        if id_paket == 0:
            main(id_user)

        # Filter data yang sesuai dengan ID paket yang dimasukkan pengguna
        selected_row = next((row for row in relevant_rows if int(row['id']) == id_paket), None)

        if not selected_row:
            print("Nomor baris tidak valid. Silakan masukkan nomor baris yang benar.\n")
        else:
            break
        
    print("\nkosongkan untuk menggunakan nilai sebelumnya")
    nama_baru = input("Masukkan nama baru: ")
    durasi_baru = input("Masukkan Durasi: ")
    harga_baru = input("Masukkan harga baru: ")
    unit_baru = input("Masukkan unit baru: ")

    # Perbarui data yang sesuai
    if nama_baru:
        selected_row['nama'] = nama_baru
    if harga_baru:
        selected_row['harga'] = harga_baru
    if unit_baru:
        selected_row['unit'] = unit_baru    
    if durasi_baru:
        selected_row['durasi'] = durasi_baru

    # memperbarui data
    for row in rows:
        if selected_row['id'] == row['id']:
            row = selected_row

    # Menyimpan data yang diperbarui kembali ke file CSV
    fl.write_to_csv("wash_packets.csv", rows)
    

    print("\nData paket telah berhasil diubah.")
    pause()

def hapus_paket(id_laundry, id_user):
    border("Hapus Paket")

    # Baca data dari file CSV
    packets = fl.read_from_csv("wash_packets.csv")
    while True:
        for packet in packets:
            if packet['id_laundry'] == id_laundry:
                print(f"{packet['id']}. {packet['nama']} - {packet['durasi']} hari - {packet['harga']}/{packet['unit']}")

        id_paket = input("Masukkan ID paket yang ingin dihapus: ")

        newPacket = []
        isDelete = None
        # Cari indeks baris yang sesuai dengan ID paket yang ingin dihapus
        for packet in packets:
            # Hapus baris dengan indeks yang sesuai
            if packet['id'] != id_paket:
                newPacket.append(packet)
            else:
                isDelete = True

        # Menyimpan data yang diperbarui kembali ke file CSV
        if isDelete == True:
            fl.write_to_csv("wash_packets.csv", newPacket)
            print("\nData paket telah berhasil dihapus.")
            pause()
            main(id_user)
        else:
            print("ID paket tidak ditemukan. Silakan masukkan ID paket yang benar.")

def main(id_user):
    while True:
        border("SELAMAT DATANG")
        id_laundry = tampilkan_data_laundry(id_user)
        printMenu("Edit Data Laundry", "Hapus Data Laundry", "Lihat Paket", "Tambah Paket", "Edit Paket", "Hapus Paket", "Lihat Order", "Kembali")
        pilihan = input("> ")
        if pilihan == "1":
            edit_data_laundry(id_user)
        elif pilihan == "2":
            hapus_data_laundry(id_user)
        elif pilihan == "3":
            lihat_paket(id_laundry)
        elif pilihan == "4":
            tambah_paket(id_laundry)
        elif pilihan == "5":
            edit_paket(id_laundry, id_user)
        elif pilihan == "6":
            hapus_paket(id_laundry, id_user)
        elif pilihan == "7":
            order.lihatOrder(id_laundry)
        elif pilihan == "8":
            exit()
        else:
            print("Pilihan tidak valid!")
            break