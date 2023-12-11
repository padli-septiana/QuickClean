# Dummy data laundry
laundry = [
    {"id": 1, "nama": "Quick Clean", "wilayah": "Bandung"},
    {"id": 2, "nama": "Washify", "wilayah": "Jakarta"},
    {"id": 3, "nama": "Quick Clean", "wilayah": "Bogor"},
    {"id": 4, "nama": "Quick Clean", "wilayah": "Bekasi"},
    {"id": 5, "nama": "Quick Clean", "wilayah": "Karawang"}
]

# Dummy data paket
paket_cuci = [
    {"id_laundry": 1, "nama_paket": "paket 1", "durasi": 3, "harga": 5000, "unit": 2},
    {"id_laundry": 2, "nama_paket": "paket hemat", "durasi": 2, "harga": 6000, "unit": 5},
    {"id_laundry": 3, "nama_paket": "pahe a", "durasi": 5, "harga": 7000, "unit": 1},
    {"id_laundry": 4, "nama_paket": "murmer", "durasi": 4, "harga": 8000, "unit": 3},
    {"id_laundry": 5, "nama_paket": "murah", "durasi": 2, "harga": 9000, "unit": 4}
]

def tampilkan_nama_laundry():
    print("Pilih Laundry:")
    for data in laundry:
        print(f"{data['id']}. {data['nama']}")

def tampilkan_detail_laundry(id_laundry):
    selected_laundry = next((l for l in laundry if l['id'] == id_laundry), None)
    if selected_laundry:
        print(f"\nDetail Laundry {selected_laundry['nama']}:")
        print(f"Nama: {selected_laundry['nama']}")
        print(f"Wilayah: {selected_laundry['wilayah']}")
        menu_edit_hapus_lihat_paket(id_laundry)
    else:
        print("Laundry tidak ditemukan.")

def menu_edit_hapus_lihat_paket(id_laundry):
    while True:
        print("\nMenu:")
        print("1. Edit Data Laundry")
        print("2. Hapus Data Laundry")
        print("3. Lihat Paket Cuci")
        print("0. Kembali")

        pilihan = input("Masukkan pilihan (1/2/3/0): ")
        if pilihan == "1":
            edit_data_laundry(id_laundry)
        elif pilihan == "2":
            hapus_data_laundry(id_laundry)
            break
        elif pilihan == "3":
            lihat_paket_cuci(id_laundry)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

def edit_data_laundry(id_laundry):
    selected_laundry = next((l for l in laundry if l['id'] == id_laundry), None)
    if selected_laundry:
        print("\nEdit Data Laundry:")
        selected_laundry['nama'] = input(f"Masukkan nama baru ({selected_laundry['nama']}): ") or selected_laundry['nama']
        selected_laundry['wilayah'] = input(f"Masukkan wilayah baru ({selected_laundry['wilayah']}): ") or selected_laundry['wilayah']
        print("Data Laundry berhasil diubah.")
    else:
        print("Laundry tidak ditemukan.")

def hapus_data_laundry(id_laundry):
    global laundry, paket_cuci
    laundry = [l for l in laundry if l['id'] != id_laundry]
    paket_cuci = [p for p in paket_cuci if p['id_laundry'] != id_laundry]
    print("Data Laundry berhasil dihapus beserta paket cuci yang terkait.")

def lihat_paket_cuci(id_laundry):
    paket_cuci_laundry = [p for p in paket_cuci if p['id_laundry'] == id_laundry]
    
    print("\nPaket Cuci:")
    for paket in paket_cuci_laundry:
        print(f"Nama Paket: {paket['nama_paket']}, Durasi: {paket['durasi']} hari, Harga: {paket['harga']}, Unit: {paket['unit']}")

    while True:
        pilihan_paket = input("Masukkan Nama Paket Cuci (0 untuk kembali): ")
        if pilihan_paket == "0":
            break
        else:
            lihat_detail_paket_cuci(id_laundry, pilihan_paket)

def lihat_detail_paket_cuci(id_laundry, nama_paket):
    selected_paket = next((p for p in paket_cuci if p['id_laundry'] == id_laundry and p['nama_paket'] == nama_paket), None)

    if selected_paket:
        print(f"\nDetail Paket Cuci {selected_paket['nama_paket']}:")
        print(f"Durasi: {selected_paket['durasi']} hari, Harga: {selected_paket['harga']}, Unit: {selected_paket['unit']}")
        menu_edit_hapus_paket_cuci(id_laundry, nama_paket)
    else:
        print("Paket Cuci tidak ditemukan.")

def menu_edit_hapus_paket_cuci(id_laundry, nama_paket):
    while True:
        print("\nMenu Paket Cuci:")
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

def edit_paket_cuci(id_laundry, nama_paket):
    selected_paket = next((p for p in paket_cuci if p['id_laundry'] == id_laundry and p['nama_paket'] == nama_paket), None)
    if selected_paket:
        print("\nEdit Paket Cuci:")
        selected_paket['durasi'] = int(input(f"Masukkan durasi baru ({selected_paket['durasi']}): ") or selected_paket['durasi'])
        selected_paket['harga'] = int(input(f"Masukkan harga baru ({selected_paket['harga']}): ") or selected_paket['harga'])
        selected_paket['unit'] = int(input(f"Masukkan unit baru ({selected_paket['unit']}): ") or selected_paket['unit'])
        print("Data Paket Cuci berhasil diubah.")
    else:
        print("Paket Cuci tidak ditemukan.")

def hapus_paket_cuci(id_laundry, nama_paket):
    global paket_cuci
    paket_cuci = [p for p in paket_cuci if not (p['id_laundry'] == id_laundry and p['nama_paket'] == nama_paket)]
    print("Data Paket Cuci berhasil dihapus.")

# Contoh Penggunaan
while True:
    tampilkan_nama_laundry()
    id_laundry_pilihan = int(input("Masukkan ID Laundry yang ingin dilihat (0 untuk keluar): "))
    
    if id_laundry_pilihan == 0:
        print("Program selesai.")
        break

    tampilkan_detail_laundry(id_laundry_pilihan)
