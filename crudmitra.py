data_laundry = [
    {"id": 1, "nama": "Quick Clean", "wilayah":"Bandung"}
]

def tampilkan_data_mitra(data):
    print("Data Mitra Laundry")
    for mitra in data:
        print(f"ID: {mitra['id']}")
        print(f"Nama: {mitra['nama']}")
        print(f"Wilayah: {mitra['wilayah']}")
        print("====================")

def ubah_data_mitra(data):
    print("UBAH DATA MITRA")
    print("====================\n")
    id_mitra = int(input("ID Mitra: "))
    for mitra in data:
        if mitra["id"] == id_mitra:
            mitra["nama"] = input("Nama Baru: ")
            mitra["wilayah"] = input("Wilayah Baru: ")
            print("Data Mitra Laundry berhasil diubah.")
            return
    print("ID Mitra tidak ditemukan.")

def hapus_mitra(data):
    hapus_id = int(input("Masukkan ID Mitra yang ingin dihapus: "))
    for i, mitra in enumerate(data):
        if mitra["id"] == hapus_id:
            del data[i]
            print("Data Mitra Laundry berhasil dihapus.")
            return
    print("ID Mitra tidak ditemukan.")

while True:
    print("DATA MITRA QUICK CLEAN")
    print("====================\n")
    print("1. Tampilkan Data Mitra")
    print("2. Edit Data Mitra")
    print("3. Hapus Data Mitra")
    print("4. Keluar")
    pilihan = input("Masukkan Opsi: ")

    if pilihan == "1":
        tampilkan_data_mitra(data_laundry)
    elif pilihan == "2":
        ubah_data_mitra(data_laundry)
    elif pilihan == "3":
        hapus_mitra(data_laundry)
    elif pilihan == "4":
        break
    else:
        print("Opsi tidak ditemukan.")