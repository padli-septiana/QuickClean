data_laundry = {"Nama": "Quick Clean", "Wilayah": "Bandung"}
paket_cuci = {"Paket 1": {"durasi": 3, "harga": 5000, "unit": "kg"}}

def tampilkan_data():
    print("\nData Laundry:")
    for key, value in data_laundry.items():
        print(f"{key}: {value}")

def edit_data_laundry():
    global data_laundry
    tampilkan_data()

    #USER MENGINPUT DATA BARU
    nama_baru = input(f"Nama ({data_laundry['Nama']}): ") or data_laundry['Nama']
    wilayah_baru = input(f"Wilayah ({data_laundry['Wilayah']}): ") or data_laundry['Wilayah']

    data_laundry ={
        "Nama": nama_baru,
        "Wilayah" : wilayah_baru
    }
    print("\nDATA LAUNDRY BERHASIL DI PERBAHARUI")
    print("====================================")

def hapus_data():
    global data_laundry

    input_hapus_data = input("Apakah anda ingin menghapus data laundry?")
    if input_hapus_data == 'y':
        data_laundry = {}
        print("\n DATA LAUNDRY TELAH DIHAPUS.")
    else:
        print("HAPUS DATA DIBATALKAN")

def tampilkan_paket():
    print("\n DAFTAR PAKET CUCI: ")
    print(paket_cuci)

def edit_paket():
    global paket_cuci
    tampilkan_paket()
    
    pilih_paket = input("Pilih paket yang akan di edit: ")
    if pilih_paket in paket_cuci:
        durasi_baru = input("Masukan Durasi baru: ") or paket_cuci[pilih_paket]['durasi']
        harga_baru = input("Masukan harga baru: ") or paket_cuci[pilih_paket]['harga']
        unit_baru = input("Masukan unit baru: ") or paket_cuci[pilih_paket]['unit']  

        paket_cuci[pilih_paket] = {
            "durasi" : durasi_baru,
            "harga" : harga_baru,
            'unit' : unit_baru
        }

        print(f"\nPaket Cuci '{pilih_paket}', Berhasil di Update")
    else:
        print(f"\nPaket Cuci Tidak Ditemukan.")

def tambah_paket():
    global paket_cuci
    nama_paket_baru = input("Masukkan Nama Paket Baru: ")
    durasi_baru = int(input("Masukkan Durasi Paket Baru: "))
    harga_baru = int(input("Masukkan Harga Paket Baru: "))
    unit_baru = input("Masukkan Unit Paket Baru: ")

    paket_cuci[nama_paket_baru] = {
        "durasi": durasi_baru,
        "harga": harga_baru,
        "unit": unit_baru
    }

    print(f"\nPaket Cuci '{nama_paket_baru}' Telah Ditambahkan.")

def hapus_paket():
    global paket_cuci
    tampilkan_paket()

    pilih_paket = input("Pilih paket yang ingin dihapus: ")
    if pilih_paket in paket_cuci:
        del paket_cuci[pilih_paket]
        print(f"\n Paket Cuci '{pilih_paket} Berhasil dihapus.")
    else:
        print(f"\n PAKET TIDAK DITEMUKAN.")


while True:
    print("QUICK CLEAN MENU")
    print("========================================")
    print("\nMenu:")
    print("1. Tampilkan Data Laundry")
    print("2. Edit Data Laundry")
    print("3. Hapus Data Laundry")
    print("4. Tampilkan Paket Cuci")
    print("5. Edit Paket Cuci")
    print("6. Tambah Paket")
    print("7. Hapus Paket Cuci")
    print("8. Keluar")

    konfirmasi = input("Pilih Menu: ")

    if konfirmasi == "1":
        tampilkan_data()
    elif konfirmasi == "2":
        edit_data_laundry()
    elif konfirmasi == "3":
        hapus_data()
        break
    elif konfirmasi == "4":
        tampilkan_paket()
    elif konfirmasi == "5":
        edit_paket()
    elif konfirmasi == "6":
        tambah_paket()
    elif konfirmasi == "7":
        hapus_paket()
    elif konfirmasi == "8":
        print("PROGRAM SELESAI.")
        break
    else: 
        print("OPSI TIDAK DITEMUKAN")
