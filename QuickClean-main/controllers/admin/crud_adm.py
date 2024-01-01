import csv
from ..files import files as fl

# Menampilkan Nama-Nama Laundry
def tampilkan_nama_laundry():
    laundry = fl.read_from_csv("laundries.csv")
    print("\n>>> Pilih Laundry <<<")
    for data in laundry:
        print(f"{data['id']}. {data['nama']}")

# MENAMPILKAN DATA LAUNDRY YANG TELAH DIINPUT SEBELUMNYA OLEH USER,
# DAN MENAMPILKAN MENU EDIT, DELETE, DAN DETAIL PAKET LAUNDRY
def tampilkan_detail_laundry(id_laundry):
    laundries = fl.read_from_csv("laundries.csv")
    for laundry in laundries:
        if laundry['id'] == id_laundry:
            selected_laundry = laundry

    if selected_laundry:
        print(f"\n<< Detail Laundry {selected_laundry['nama']}: >>")
        print(f"Nama Laundry: {selected_laundry['nama']}")
        print(f"Wilayah: {selected_laundry['wilayah']}")
        menu_edit_hapus_lihat_paket(id_laundry)
    else:
        print("Laundry tidak dapat ditemukan.")

### FUNCTION MENU EDIT, HAPUS LAUNDRY DAN LIHAT PAKET <LAUNDRY> ###
def menu_edit_hapus_lihat_paket(id_laundry):
    while True:
        print("\n>>> Menu <<<")
        print("1. Edit Data Laundry")
        print("2. Hapus Data Laundry")
        print("3. Lihat Paket Cuci")
        print("4. Tambah Paket Cuci")
        print("0. Kembali")

        pilihan = input("-> Masukkan pilihan (1/2/3/0): ")
        if pilihan == "1":
            edit_data_laundry(id_laundry)
        elif pilihan == "2":
            hapus_data_laundry(id_laundry)
            break
        elif pilihan == "3":
            lihat_paket_cuci(id_laundry)
        elif pilihan == "4":
            tambah_paket_cuci(id_laundry)
        elif pilihan == "0":
            menuAdmin()
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# FUNCTION EDIT DATA LAUNDRY
def edit_data_laundry(id_laundry):
    laundry = fl.read_from_csv("laundries.csv")
    paket_cuci = fl.read_from_csv("wash_packets.csv")
    for laun in laundry:
        if laun['id'] == id_laundry:
            print("\n>> Edit Data Laundry: <<")
            laun['nama'] = input(f"Masukkan nama baru laundry ({laun['nama']}): ") or laun['nama']
            laun['wilayah'] = input(f"Masukkan wilayah baru ({laun['wilayah']}): ") or laun['wilayah']
            
            fl.write_to_csv("laundries.csv", laundry)
                
            print("=== Data Laundry berhasil diubah. ===")
        else:
            print("Laundry tidak ditemukan.")

    
# FUNCTION HAPUS DATA LAUNDRY
def hapus_data_laundry(id_laundry):
    laundry = fl.read_from_csv("laundries.csv")
    paket_cuci = fl.read_from_csv("wash_packets.csv")
    users = fl.read_from_csv("users.csv")
    newLaundry = []
    newPacket = []
    # Menemukan indeks baris yang sesuai dengan id
    for laun in laundry:
        # Menghapus baris yang sesuai dengan id=2
        if laun['id'] != id_laundry:
            newLaundry.append(laun)
            for user in users:
                if user['id'] == laun['id_user']:
                    user['id_laundry'] = 1

    # Menemukan indeks baris yang sesuai dengan id
    for paket in paket_cuci:
        # Menghapus baris yang sesuai dengan id=2
        if paket['id_laundry'] != id_laundry:
            newPacket.append(paket)

    fl.write_to_csv('laundries.csv', newLaundry)
    fl.write_to_csv('wash_packets.csv', newPacket)
    print("Berhasil dihapus.")
    menuAdmin()

# FUNCTION <LIHAT PAKET CUCI> DARI PILIHAN MENU 
def lihat_paket_cuci(id_laundry):
    pakets = fl.read_from_csv("wash_packets.csv")
    print("\n<< Paket Cuci: >>")
    for paket in pakets:
        if paket['id_laundry'] == id_laundry:
            print(f'{paket["id"]}. {paket["nama"]} - Rp.{paket["harga"]}/{paket["unit"]} - {paket["durasi"]} hari')

    max_id = max([int(paket['id']) for paket in pakets]) if pakets else 1  # Hitung ID terbaru
    while True:
        pilihan_paket = input("--> Masukkan angka paket Laundry (0 untuk kembali): ")
        if pilihan_paket == "0":
            break
        else:
            isValid = False
            for paket in pakets:
                if paket['id_laundry'] == id_laundry and paket['id'] == pilihan_paket:
                    isValid = True
            if isValid == True:
                lihat_detail_paket_cuci(id_laundry, pilihan_paket)
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka yang benar.")

# DETAIL PAKET CUCI YANG SEBELUMNYA DIINPUTKAN USER
def lihat_detail_paket_cuci(id_laundry, id_paket):
    paket_cuci = fl.read_from_csv("wash_packets.csv")
    for paket in paket_cuci:
        if paket['id_laundry'] == id_laundry and paket['id'] == id_paket:
            selected_paket = paket

    if selected_paket:
        print(f"\n<<< Detail Paket Cuci {selected_paket['nama']}: >>>")
        print(f"Durasi: {selected_paket['durasi']} hari, Harga: {selected_paket['harga']}, Unit: {selected_paket['unit']}")
        menu_edit_hapus_paket_cuci(id_laundry, selected_paket['id'])
    else:
        print("Paket Cuci tidak ditemukan.")


# TAMBAH PAKET CUCI
def tambah_paket_cuci(id_laundry):
    paket_cuci = fl.read_from_csv("wash_packets.csv")
    print("\n>>> Masukkan Paket Laundry <<<")
    id_laundry = id_laundry
    nama = input("Masukkan nama paket cuci => ")
    durasi = int(input("Masukkan durasi pengerjaan paket cuci (dalam hari) => "))
    unit = str(input("Masukkan unit paket cuci (pasang/kg) => "))
    harga = int(input(f"Masukkan harga paket cuci per {unit} => "))
    
    new_id = max([int(paket['id']) for paket in paket_cuci]) + 1 if paket_cuci else 1  # Hitung ID terbaru
    paket_cuci.append({
        "id": new_id,  # Gunakan ID terbaru
        "id_laundry": id_laundry,
        "nama": nama,
        "durasi": durasi,
        "unit": unit,
        "harga": harga,
    })
    
    print(f"=== Paket Cuci {nama} berhasil ditambahkan ===\n")
    fl.write_to_csv('wash_packets.csv', paket_cuci)  # Panggil fungsi ini setelah menambahkan paket cuci

### MENU EDIT DAN HAPUS PAKET CUCI <PAKET CUCI> MUNCUL APABILA DI AWAL SUDAH MEMILIH LAUNDRY YANG DITAMPILKAN ###
def menu_edit_hapus_paket_cuci(id_laundry, id_paket):
    while True:
        print("\n>>> Menu Paket Cuci <<<")
        print("1. Edit Paket Cuci")
        print("2. Hapus Paket Cuci")
        print("0. Kembali")

        pilihan = input("Masukkan pilihan (1/2/0): ")
        if pilihan == "1":
            edit_paket_cuci(id_laundry, id_paket)
        elif pilihan == "2":
            hapus_paket_cuci(id_laundry, id_paket)
            menuAdmin()
        elif pilihan == "0":
            menuAdmin()
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# FUNCTION EDIT PAKET CUCI
def edit_paket_cuci(id_laundry, id_paket):
    paket_cuci = fl.read_from_csv("wash_packets.csv")
    for paket in paket_cuci:
        if paket['id'] == id_paket:
            print("\n>> Edit Paket Cuci: <<")
            nama = input(f"Masukkan nama paket baru ({paket['nama']}): ")
            durasi = input(f"Masukkan durasi baru ({paket['durasi']}): ")
            harga = input(f"Masukkan harga baru ({paket['harga']}): ")
            unit = input(f"Masukkan unit baru ({paket['unit']}): ")
            paket['nama'] = nama if nama != "" else paket['nama']
            paket['durasi'] = durasi if durasi != "" else paket['durasi']
            paket['harga'] = harga if harga != "" else paket['harga']
            paket['unit'] = unit if unit != "" else paket['unit']
            fl.write_to_csv("wash_packets.csv", paket_cuci)
            print("=== Data Paket Cuci berhasil diubah. ===")


# FUNCTION HAPUS PAKET CUCI
def hapus_paket_cuci(id_laundry, id_paket):
    paket_cuci = fl.read_from_csv("wash_packets.csv")
    new_paket_cuci = []
    for wash_packet in paket_cuci:
        if wash_packet['id'] != str(id_paket):
            new_paket_cuci.append(wash_packet)
    fl.write_to_csv('wash_packets.csv', new_paket_cuci)
    print("=== Data Paket Cuci berhasil dihapus. ===")


# Contoh Penggunaan
def menuAdmin():
    tampilkan_nama_laundry()
    id_laundry_pilihan = input("-> Masukkan angka Laundry yang ingin dilihat (0 untuk keluar): ")
    print(id_laundry_pilihan, type(str(id_laundry_pilihan)))
    if id_laundry_pilihan == '0' or id_laundry_pilihan == '':
        print('')
    else:
        tampilkan_detail_laundry(id_laundry_pilihan)