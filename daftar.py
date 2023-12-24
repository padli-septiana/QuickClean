# Daftar Mitra & menambahkan 1 paket cuci

import csv

data_laundries = []
wash_packets = []

def laundries():
    print("\n>>> Masukkan Data Laundry <<<")
    id = len(data_laundries) + 1
    nama_laundry = input("Masukkan nama laundry => ")
    wilayah_laundry = input("Masukkan wilayah laundry => ")

    # Membuat objek dictionary untuk data laundry
    laundry = {
        "id": id,
        "nama": nama_laundry,
        "wilayah": wilayah_laundry,
    }

    # Menambahkan data laundry ke dalam list
    data_laundries.append(laundry)
    print(f"=== Laundry {nama_laundry} berhasil terdaftar ===\n")

    # Memanggil fungsi untuk memasukkan paket cuci terkait dengan laundry yang baru ditambahkan
    paket_cuci(id)

def paket_cuci(id):
    print(">>> Masukkan Paket Laundry <<<")
    id_laundry = len(wash_packets) + 1
    nama_paket = input("Masukkan nama paket cuci => ")
    durasi_paket = input("Masukkan durasi pengerjaan paket cuci (dalam hari) => ")
    unit_paket = str(input("Masukkan unit paket cuci (pasang/kg) => "))
    harga_paket = int(input(f"Masukkan harga paket cuci per {unit_paket} => "))

    # Membuat objek dictionary untuk data paket cuci
    paket_cuci = {
        "id_laundry": id_laundry,
        "id": id,
        "nama_paket": nama_paket,
        "durasi": durasi_paket,
        "unit": unit_paket,
        "harga": harga_paket,
    }

    # Menambahkan data paket cuci ke dalam list
    wash_packets.append(paket_cuci)
    print(f"=== Paket Cuci {nama_paket} berhasil ditambahkan ===\n")

def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        fieldnames = data[0].keys() if data else []  # Mengambil nama kolom dari keys dictionary pertama (jika ada)
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # Menulis header (nama kolom)
        writer.writerows(data)  # Menulis baris-baris data

def read_from_csv(filename):
    data = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        pass  # File belum ada, atau kosong

    return data

# Contoh penggunaan
data_laundries = read_from_csv('data_laundries.csv')
wash_packets = read_from_csv('wash_packets.csv')

# Memanggil fungsi untuk memasukkan data laundry
laundries()

# Menyimpan data terbaru ke dalam file CSV setelah proses penginputan
write_to_csv('data_laundries.csv', data_laundries)
write_to_csv('wash_packets.csv', wash_packets)
