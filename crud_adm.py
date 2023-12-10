# view, edit, delete as admin

# dummy data
data_laundry = [
    {"nama": "Quick Clean", "harga": 5000, "unit": 2, "durasi": 3},
    {"nama": "Washify", "harga": 6000, "unit": 5, "durasi": 2},
    {"nama": "Klik Klin", "harga": 7000, "unit": 1, "durasi": 5},
    {"nama": "LaundryKlin", "harga": 8000, "unit": 3, "durasi": 4},
    {"nama": "Moza Laundry", "harga": 9000, "unit": 4, "durasi": 2}
]

def tampilkan_data():
    print("\n>> Data Mitra Laundry: <<")
    for i, data in enumerate(data_laundry, start=1):
        print(f"{i}. Nama Laundry: {data['nama']}, Harga: {data['harga']}, Unit: {data['unit']}, Durasi: {data['durasi']} hari")

def edit_data():
    tampilkan_data()
    index = int(input("-> Masukkan nomor data yang ingin diedit: ")) - 1

    if 0 <= index < len(data_laundry):
        data = data_laundry[index]
        print(f"Data saat ini: {data}")
        
        data['nama'] = input("Masukkan nama laundry baru: ")
        data['harga'] = int(input("Masukkan harga per unit baru: "))
        data['unit'] = input("Masukkan jumlah unit baru: ")
        data['durasi'] = int(input("Masukkan durasi pengerjaan baru (dalam hari): "))
        
        print("=== Data berhasil diubah! ===\n")
    else:
        print("!! Nomor data tidak valid. !!")

def hapus_data():
    tampilkan_data()
    index = int(input("-> Masukkan nomor data yang ingin dihapus: ")) - 1

    if 0 <= index < len(data_laundry):
        deleted_data = data_laundry.pop(index)
        print(f"=== Data {deleted_data['nama']} berhasil dihapus! ===\n")
    else:
        print("!! Nomor data tidak valid. !!")

# Contoh penggunaan
while True:
    print("\n>>> Pilih Menu <<<")
    print("(a) Tampilkan Data")
    print("(b) Edit Data")
    print("(c) Hapus Data")
    print("(d) Keluar")
    
    pilihan = input("-> Masukkan Pilih Menu (a/b/c/d): ")

    if pilihan == "a":
        tampilkan_data()
    elif pilihan == "b":
        edit_data()
    elif pilihan == "c":
        hapus_data()
    elif pilihan == "d":
        print("Program selesai.")
        break
    else:
        print("!! Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
