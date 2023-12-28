## AS ADMIN

import csv
import os

# Dummy data laundry
def read_laundries_from_csv():
    try:
        with open("files/laundries.csv", mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_laundries_to_csv():
    with open("files/laundries.csv", mode='w', newline='') as file:
        fieldnames = ["id", "nama", "wilayah"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(laundry)
        
def read_pakets_from_csv():
    try:
        with open("files/wash_packets.csv", mode='r', encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            return [dict(row) for row in reader]
    except FileNotFoundError:
        return []

def write_pakets_to_csv():
    with open("files/wash_packets.csv", mode='w', newline='') as file:
        fieldnames = ["id", "id_laundry", "nama", "durasi", "harga", "unit"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(paket_cuci)
        
laundry = read_laundries_from_csv()
paket_cuci = read_pakets_from_csv()

# Menampilkan Nama-Nama Laundry
def tampilkan_nama_laundry():
    print("\n>>> Pilih Laundry <<<")
    for data in laundry:
        print(f"{data['id']}. {data['nama']}")

# MENAMPILKAN DATA LAUNDRY YANG TELAH DIINPUT SEBELUMNYA OLEH USER,
# DAN MENAMPILKAN MENU EDIT, DELETE, DAN DETAIL PAKET LAUNDRY
def tampilkan_detail_laundry(id_laundry):
    laundries = read_laundries_from_csv()
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
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# FUNCTION EDIT DATA LAUNDRY
def edit_data_laundry(id_laundry):
    selected_laundry = next((l for l in laundry if l['id'] == id_laundry), None)
    if selected_laundry:
        print("\n>> Edit Data Laundry: <<")
        selected_laundry['nama'] = input(f"Masukkan nama baru laundry ({selected_laundry['nama']}): ") or selected_laundry['nama']
        selected_laundry['wilayah'] = input(f"Masukkan wilayah baru ({selected_laundry['wilayah']}): ") or selected_laundry['wilayah']
        
        with open("files/laundries.csv", mode='w', newline='') as file:
            fieldnames = ["id", "nama", "wilayah"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(laundry)
            
        print("=== Data Laundry berhasil diubah. ===")
    else:
        print("Laundry tidak ditemukan.")
    
# FUNCTION HAPUS DATA LAUNDRY
def hapus_data_laundry(id_laundry):
    global laundry, paket_cuci

    deleted_laundry = None

    # Cari laundry yang akan dihapus
    for l in laundry:
        if l['id'] == id_laundry:
            deleted_laundry = l
            break

    if deleted_laundry:
        # Hapus data laundry
        laundry = [l for l in laundry if l['id'] != id_laundry]

        # Hapus paket_cuci yang terkait dengan laundry yang dihapus
        paket_cuci = [p for p in paket_cuci if p['id_laundry'] != id_laundry]

        # Perbarui nomor urutan setelah penghapusan
        for i, l in enumerate(laundry):
            l['id'] = i + 1

        # Tulis ulang data laundry ke file CSV
        write_laundries_to_csv()

        # Hapus paket_cuci dari file wash_packets.csv
        with open("files/wash_packets.csv", mode='w', newline='') as file:
            fieldnames = ["id", "id_laundry", "nama", "durasi", "harga", "unit"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(paket_cuci)

        print("=== Data Laundry berhasil dihapus beserta paket cuci yang terkait. ===")
    else:
        print("Laundry tidak ditemukan.")

# FUNCTION <LIHAT PAKET CUCI> DARI PILIHAN MENU 
def lihat_paket_cuci(id_laundry):
    pakets = read_pakets_from_csv()
    print("\n<< Paket Cuci: >>")
    for paket in pakets:
        if paket['id_laundry'] == id_laundry:
            print(f'{paket["id"]}. {paket["nama"]} - Rp.{paket["harga"]}/{paket["unit"]}')

    while True:
        pilihan_paket = input("--> Masukkan angka paket Laundry (0 untuk kembali): ")
        if pilihan_paket == "0":
            break
        else:
            pilihan_paket = int(pilihan_paket)
            if 1 <= pilihan_paket <= len(paket_cuci):
                selected_paket = paket_cuci[pilihan_paket - 1]
                lihat_detail_paket_cuci(id_laundry, selected_paket['nama'])
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka yang benar.")

# DETAIL PAKET CUCI YANG SEBELUMNYA DIINPUTKAN USER
def lihat_detail_paket_cuci(id_laundry, nama_paket):
    selected_paket = next((p for p in paket_cuci if p['id_laundry'] == id_laundry and p['nama'] == nama_paket), None)

    if selected_paket:
        print(f"\n<<< Detail Paket Cuci {selected_paket['nama']}: >>>")
        print(f"Durasi: {selected_paket['durasi']} hari, Harga: {selected_paket['harga']}, Unit: {selected_paket['unit']}")
        menu_edit_hapus_paket_cuci(id_laundry, nama_paket)
    else:
        print("Paket Cuci tidak ditemukan.")


# TAMBAH PAKET CUCI
def tambah_paket_cuci(id_laundry):
    print("\n>>> Masukkan Paket Laundry <<<")
    id_laundry = id_laundry_pilihan
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
    write_pakets_to_csv()  # Panggil fungsi ini setelah menambahkan paket cuci

### MENU EDIT DAN HAPUS PAKET CUCI <PAKET CUCI> MUNCUL APABILA DI AWAL SUDAH MEMILIH LAUNDRY YANG DITAMPILKAN ###
def menu_edit_hapus_paket_cuci(id_laundry, nama_paket):
    while True:
        print("\n>>> Menu Paket Cuci <<<")
        print("1. Edit Paket Cuci")
        print("2. Hapus Paket Cuci")
        print("0. Kembali")

        pilihan = input("Masukkan pilihan (1/2/0): ")
        if pilihan == "1":
            edit_paket_cuci(id_laundry, nama_paket)
        elif pilihan == "2":
            hapus_paket_cuci(id_laundry, nama_paket)
            break
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# FUNCTION EDIT PAKET CUCI
def edit_paket_cuci(id_laundry, nama_paket):
    selected_paket = next((p for p in paket_cuci if p['id_laundry'] == id_laundry and p['nama'] == nama_paket), None)
    if selected_paket:
        print("\n>> Edit Paket Cuci: <<")
        selected_paket['nama'] = input(f"Masukkan nama paket baru ({selected_paket['nama']}): ") or selected_paket['nama']
        selected_paket['durasi'] = int(input(f"Masukkan durasi baru ({selected_paket['durasi']}): ") or selected_paket['durasi'])
        selected_paket['harga'] = int(input(f"Masukkan harga baru ({selected_paket['harga']}): ") or selected_paket['harga'])
        selected_paket['unit'] = str(input(f"Masukkan unit baru ({selected_paket['unit']}): ") or selected_paket['unit'])
        print("=== Data Paket Cuci berhasil diubah. ===")
    else:
        print("Paket Cuci tidak ditemukan.")


# FUNCTION HAPUS PAKET CUCI
def hapus_paket_cuci(id_laundry, nama_paket):
    global paket_cuci
    paket_cuci = [p for p in paket_cuci if not (p['id_laundry'] == id_laundry and p['nama'] == nama_paket)]
    print("=== Data Paket Cuci berhasil dihapus. ===")


# Contoh Penggunaan
while True:
    tampilkan_nama_laundry()
    id_laundry_pilihan = input("-> Masukkan angka Laundry yang ingin dilihat (0 untuk keluar): ")
    
    if int(id_laundry_pilihan) == 0:
        print("--- Program selesai terima kasih. ---")
        break

    tampilkan_detail_laundry(id_laundry_pilihan)
