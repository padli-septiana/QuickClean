import csv
import os

def crud_admin():
    while True:
        print("0. Keluar")
        print("1. Lihat laundry")
        menu = int(input("Masukkan menu: "))

        if menu == 1:
            read_laundry()
        else:
            exit()

def read_laundry():
    laundries = get_laundries()
    users = get_users()

    print("Daftar Laundry:")
    for i, laundry in enumerate(laundries, start=1):
        print(f"{i}. {laundry['nama']} - {laundry['wilayah']}")

    print("0. Kembali")
    selected_option = int(input("Pilih nomor laundry: "))

    if selected_option == 0:
        return
    else:
        selected_laundry = laundries[selected_option - 1]
        manage_laundry(selected_laundry)

def manage_laundry(laundry):
    while True:
        print("0. Kembali")
        print("1. Edit laundry")
        print("2. Lihat paket cuci")
        print("3. Tutup laundry")

        menu = int(input("Masukkan menu: "))

        if menu == 0:
            break
        elif menu == 1:
            edit_data_laundry(laundry)
        elif menu == 2:
            crud_wash_packets(laundry)
        elif menu == 3:
            close_laundry(laundry)

def edit_data_laundry(laundry):
    # selected_laundry = next((l for l in laundry if l['id'] == laundry), None)
    selected_laundry = get_laundries
    if selected_laundry:
        print("\n>> Edit Data Laundry: <<")
        selected_laundry['nama'] = input(f"Masukkan nama baru laundry ({selected_laundry['nama']}): ") or selected_laundry['nama']
        selected_laundry['wilayah'] = input(f"Masukkan wilayah baru ({selected_laundry['wilayah']}): ") or selected_laundry['wilayah']
        print("=== Data Laundry berhasil diubah. ===")
    else:
        print("Laundry tidak ditemukan.")

def crud_wash_packets(laundry):
    # Implementasi fungsi untuk mengelola paket cuci
    print(f"Managing wash packets for laundry: {laundry}")

def create_wash_packet(laundry):
    def tambah_paket_cuci(id):
        print("\n>>> Masukkan Paket Laundry <<<")
    id_laundry = id
    nama_paket = input("Masukkan nama paket cuci => ")
    durasi = int(input("Masukkan durasi pengerjaan paket cuci (dalam hari) => "))
    unit = str(input("Masukkan unit paket cuci (pasang/kg) => "))
    harga = int(input(f"Masukkan harga paket cuci per {unit} => "))

    tambah_paket_cuci(id).append({
        "id_laundry": id_laundry,
        "nama_paket": nama_paket,
        "durasi": durasi,
        "unit": unit,
        "harga": harga,
    })
    print(f"=== Paket Cuci {nama_paket} berhasil ditambahkan ===\n")
    return tambah_paket_cuci

def close_laundry(laundry):
    # Implementasi fungsi untuk menutup laundry
    print(f"Closing laundry: {laundry}")

def get_laundries():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'files', 'laundries.csv')
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        laundries = list(csv.DictReader(csvfile))
    return laundries

def get_users():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'files', 'users.csv')
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        users = list(csv.DictReader(csvfile))
    return users

# Panggil fungsi utama
crud_admin()
