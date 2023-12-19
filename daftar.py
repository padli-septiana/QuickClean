import csv

data_laundries = []
wash_packets = []

def data_laundry():
    print("\n>>> Masukkan Data Laundry <<<")
    id = len(data_laundries) + 1
    nama_laundry = input("Masukkan nama laundry => ")
    wilayah_laundry = input("Masukkan wilayah laundry => ")

    laundry = {
        "id": id,
        "nama": nama_laundry,
        "wilayah": wilayah_laundry,
    }

    data_laundries.append(laundry)
    print(f"=== Laundry {nama_laundry} berhasil terdaftar ===\n")
    paket_cuci(id)

def paket_cuci(id):
    print(">>> Masukkan Paket Laundry <<<")
    id_laundry = len(wash_packets) + 1
    nama_paket = input("Masukkan nama paket cuci => ")
    durasi_paket = input("Masukkan durasi pengerjaan paket cuci (dalam hari) => ")
    unit_paket = str(input("Masukkan unit paket cuci (pasang/kg) => "))
    harga_paket = int(input("Masukkan harga paket cuci per unit => "))

    paket_cuci = {
        "id_laundry": id_laundry,
        "id": id,
        "nama_paket": nama_paket,
        "durasi": durasi_paket,
        "unit": unit_paket,
        "harga": harga_paket,
    }

    wash_packets.append(paket_cuci)
    print(f"=== Paket Cuci {nama_paket} berhasil ditambahkan ===\n")

def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(data)

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

data_laundry()

write_to_csv('data_laundries.csv', data_laundries)
write_to_csv('wash_packets.csv', wash_packets)
