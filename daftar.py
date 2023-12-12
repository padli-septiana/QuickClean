## AS USER

data_laundries = []
wash_packets = []

# FUNCTION DATA LAUNDRY SAAT REGIST LAUNDRY
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

# SAAT MELAKUKAN REGIST LAUNDRY, MITRA HARUS MENAMBAHKAN/INPUT SATU PAKET CUCI
def paket_cuci(id):
    print(">>> Masukkan Paket Laundry <<<")
    id_laundry = len(wash_packets) + 1
    nama_paket = input("Masukkan nama paket cuci => ")
    durasi_paket = input("Masukkan durasi pengerjaan paket cuci (dalam hari) => ")
    unit_paket = str(input("Masukkan jumlah unit paket cuci (satuan/pasang/kg) => "))
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




# Contoh penggunaan
data_laundry()
