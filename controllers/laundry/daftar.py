import csv
from ..files import files as fl

data_laundries = fl.read_from_csv("laundries.csv")
wash_packets = fl.read_from_csv("wash_packets.csv")

def laundries(id_user):
    print("\n>>> Masukkan Data Laundry <<<")
    id = max([int(laundry['id']) for laundry in data_laundries]) + 1 if data_laundries else 1  # Hitung ID terbaru
    nama_laundry = input("Masukkan nama laundry => ")
    wilayah_laundry = input("Masukkan wilayah laundry => ")

    # Membuat objek dictionary untuk data laundry
    laundry = {
        "id": id,
        "nama": nama_laundry,
        "wilayah": wilayah_laundry,
        "id_user": id_user,
    }

    # Menambahkan data laundry ke dalam list
    data_laundries.append(laundry)

    # Mengubah role user
    users = fl.read_from_csv("users.csv")
    for user in users:
        if str(user['id']) == str(id_user):
            (user['role']) = '2'
    fl.write_to_csv("laundries.csv", data_laundries)
    fl.write_to_csv("users.csv", users)
    print(f"=== Laundry {nama_laundry} berhasil terdaftar ===\n")

    # Memanggil fungsi untuk memasukkan paket cuci terkait dengan laundry yang baru ditambahkan
    paket_cuci(id)

def paket_cuci(id):
    print(">>> Masukkan Paket Laundry <<<")
    id_paket = max([int(paket['id']) for paket in wash_packets]) + 1 if wash_packets else 1  # Hitung ID terbaru
    id_laundry = id
    nama_paket = input("Masukkan nama paket cuci => ")
    durasi_paket = input("Masukkan durasi pengerjaan paket cuci (dalam hari) => ")
    unit_paket = input("Masukkan unit paket cuci (pasang/kg) => ")
    harga_paket = input(f"Masukkan harga paket cuci per {unit_paket} => ")

    # Membuat objek dictionary untuk data paket cuci
    paket_cuci = {
        "id": id_paket,
        "id_laundry": id_laundry,
        "nama": nama_paket,
        "durasi": durasi_paket,
        "unit": unit_paket,
        "harga": harga_paket,
    }

    # Menambahkan data paket cuci ke dalam list
    wash_packets.append(paket_cuci)
    fl.write_to_csv("wash_packets.csv", wash_packets)
    print(f"=== Paket {nama_paket} berhasil ditambahkan ===\n")