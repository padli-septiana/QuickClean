data_laundries = []
wash_packets = []


def data_laundry():
    print(">>> Masukkan Data Laundry <<<")
    id = len(data_laundries) + 1
    nama_laundry = input("Masukkan nama laundry: ")
    wilayah_laundry = input("Masukkan wilayah laundry: ")

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
    nama_paket = input("Masukkan nama paket cuci: ")
    durasi_paket = input("Masukkan durasi pengerjaan paket cuci (dalam hari): ")
    harga_paket = int(input("Masukkan harga paket cuci per unit: "))
    unit_paket = int(input("Masukkan jumlah unit paket cuci: "))

    paket_cuci = {
        "id_laundry": id_laundry,
        "id": id,
        "nama_paket": nama_paket,
        "durasi": durasi_paket,
        "harga": harga_paket,
        "unit": unit_paket,
    }

    wash_packets.append(paket_cuci)
    print(f"=== Paket Cuci {nama_paket} berhasil ditambahkan ===\n")




# Contoh penggunaan
data_laundry()

# Menampilkan data laundry dan paket cuci
#print("Data Laundries:")
#for laundry in data_laundries:
#    print(laundry)

#print("\nData Wash Packets:")
#for wash_packet in wash_packets:
#    print(wash_packet)
