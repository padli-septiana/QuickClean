# Daftar/Tambah data laundry

data_laundry = []

print(">>> Tambah Data Laundry <<<")
def tambah_data():
    nama = input("-> Masukkan nama laundry: ")
    harga = int(input("-> Masukkan harga per kilo: "))
    unit = input("-> Masukkan jumlah berat laundry (dalam kg): ")
    durasi = int(input("-> Masukkan durasi pengerjaan (dalam hari): "))

    data = {
        'nama': nama,
        'harga': harga,
        'unit': unit,
        'durasi': durasi
    }

    data_laundry.append(data)
    print(">>> Data Berhasil Ditambahkan <<<\n")

def tampilkan_data():
    print("->> Data Laundry:")
    for i, data in enumerate(data_laundry, start=1):
        print(f"{i}. Nama Laundry: {data['nama']}, Harga: {data['harga']}, Unit: {data['unit']}, Durasi: {data['durasi']} hari")

# Contoh penggunaan
tambah_data()
tampilkan_data()
