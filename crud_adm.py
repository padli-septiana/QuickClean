## AS ADMIN

# Dummy data laundry
laundry = [
    {"id": 1, "nama": "Quick Clean", "wilayah": "Bandung"},
    {"id": 2, "nama": "Washify", "wilayah": "Jakarta"},
    {"id": 3, "nama": "Klik Klin", "wilayah": "Bogor"},
    {"id": 4, "nama": "Moza Klin", "wilayah": "Bekasi"},
    {"id": 5, "nama": "Bersih", "wilayah": "Karawang"}
]

# Dummy data paket
paket_cuci = [
    {"id_laundry": 1, "nama_paket": "paket 1", "durasi": 3, "harga": 5000, "unit": "kg"},
    {"id_laundry": 2, "nama_paket": "paket hemat", "durasi": 2, "harga": 6000, "unit": "kg"},
    {"id_laundry": 3, "nama_paket": "pahe a", "durasi": 5, "harga": 7000, "unit": "kg"},
    {"id_laundry": 4, "nama_paket": "murmer", "durasi": 4, "harga": 8000, "unit": "kg"},
    {"id_laundry": 5, "nama_paket": "murah", "durasi": 2, "harga": 9000, "unit": "kg"}
]


# MENAMPILKAN NAMA-NAMA LAUNDRY DARI DUMMY DATA
def tampilkan_nama_laundry():
    print("\n>>> Pilih Laundry <<<")
    for data in laundry:
        print(f"{data['id']}. {data['nama']}")


# MENAMPILKAN DATA LAUNDRY YANG TELAH DIINPUT SEBELUMNYA OLEH USER,
# DAN MENAMPILKAN MENU EDIT, DELETE, DAN DETAIL PAKET LAUNDRY
def tampilkan_detail_laundry(id_laundry):
    selected_laundry = next((l for l in laundry if l['id'] == id_laundry), None)
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
        print("=== Data Laundry berhasil diubah. ===")
    else:
        print("Laundry tidak ditemukan.")

# FUNCTION HAPUS DATA LAUNDRY
def hapus_data_laundry(id_laundry):
    global laundry, paket_cuci
    laundry = [l for l in laundry if l['id'] != id_laundry]
    paket_cuci = [p for p in paket_cuci if p['id_laundry'] != id_laundry]
    
    # Perbarui nomor urutan setelah penghapusan
    for i, l in enumerate(laundry):
        l['id'] = i + 1

    print("=== Data Laundry berhasil dihapus beserta paket cuci yang terkait. ===")


# FUNCTION <LIHAT PAKET CUCI> DARI PILIHAN MENU 
def lihat_paket_cuci(id_laundry):
    paket_cuci_laundry = [p for p in paket_cuci if p['id_laundry'] == id_laundry]
    
    print("\n<< Paket Cuci: >>")
    for idx, paket in enumerate(paket_cuci_laundry, start=1):
        print(f"{idx}. Nama Paket: {paket['nama_paket']}")

    while True:
        pilihan_paket = input("--> Masukkan angka paket Laundry (0 untuk kembali): ")
        if pilihan_paket == "0":
            break
        else:
            pilihan_paket = int(pilihan_paket)
            if 1 <= pilihan_paket <= len(paket_cuci_laundry):
                selected_paket = paket_cuci_laundry[pilihan_paket - 1]
                lihat_detail_paket_cuci(id_laundry, selected_paket['nama_paket'])
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka yang benar.")

# DETAIL PAKET CUCI YANG SEBELUMNYA DIINPUTKAN USER
def lihat_detail_paket_cuci(id_laundry, nama_paket):
    selected_paket = next((p for p in paket_cuci if p['id_laundry'] == id_laundry and p['nama_paket'] == nama_paket), None)

    if selected_paket:
        print(f"\n<<< Detail Paket Cuci {selected_paket['nama_paket']}: >>>")
        print(f"Durasi: {selected_paket['durasi']} hari, Harga: {selected_paket['harga']}, Unit: {selected_paket['unit']}")
        menu_edit_hapus_paket_cuci(id_laundry, nama_paket)
    else:
        print("Paket Cuci tidak ditemukan.")


# TAMBAH PAKET CUCI
def tambah_paket_cuci(id):
    print("\n>>> Masukkan Paket Laundry <<<")
    id_laundry = id
    nama_paket = input("Masukkan nama paket cuci => ")
    durasi = int(input("Masukkan durasi pengerjaan paket cuci (dalam hari) => "))
    unit = str(input("Masukkan unit paket cuci (pasang/kg) => "))
    harga = int(input(f"Masukkan harga paket cuci per {unit} => "))
    
    paket_cuci.append({
        "id_laundry": id_laundry,
        "nama_paket": nama_paket,
        "durasi": durasi,
        "unit": unit,
        "harga": harga,
    })
    print(f"=== Paket Cuci {nama_paket} berhasil ditambahkan ===\n")


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
    selected_paket = next((p for p in paket_cuci if p['id_laundry'] == id_laundry and p['nama_paket'] == nama_paket), None)
    if selected_paket:
        print("\n>> Edit Paket Cuci: <<")
        selected_paket['nama_paket'] = input(f"Masukkan nama paket baru ({selected_paket['nama_paket']}): ") or selected_paket['nama_paket']
        selected_paket['durasi'] = int(input(f"Masukkan durasi baru ({selected_paket['durasi']}): ") or selected_paket['durasi'])
        selected_paket['harga'] = int(input(f"Masukkan harga baru ({selected_paket['harga']}): ") or selected_paket['harga'])
        selected_paket['unit'] = str(input(f"Masukkan unit baru ({selected_paket['unit']}): ") or selected_paket['unit'])
        print("=== Data Paket Cuci berhasil diubah. ===")
    else:
        print("Paket Cuci tidak ditemukan.")


# FUNCTION HAPUS PAKET CUCI
def hapus_paket_cuci(id_laundry, nama_paket):
    global paket_cuci
    paket_cuci = [p for p in paket_cuci if not (p['id_laundry'] == id_laundry and p['nama_paket'] == nama_paket)]
    print("=== Data Paket Cuci berhasil dihapus. ===")


# Contoh Penggunaan
while True:
    tampilkan_nama_laundry()
    id_laundry_pilihan = int(input("-> Masukkan angka Laundry yang ingin dilihat (0 untuk keluar): "))
    
    if id_laundry_pilihan == 0:
        print("--- Program selesai terima kasih. ---")
        break

    tampilkan_detail_laundry(id_laundry_pilihan)
