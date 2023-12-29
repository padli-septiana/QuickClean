import csv

#Fungsi untuk menyimpan data order
def save_order_to_csv(order, nama_tempat, nama_pelanggan, id_user):
    with open('files/orders.csv', mode='w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['id', 'id_user', 'nama_tempat', 'nama_pelanggan', 'paymentMethod', 'alamat', 'tgl_pengambilan', 'tgl_pengantaran', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Menulis header jika file CSV kosong
        writer.writeheader()
        
        # Menulis data order ke dalam file CSV
        for order_id, order_data in order.items():
            writer.writerow({
                'id': order_id,
                'id_user': id_user,
                'nama_tempat': nama_tempat,
                'nama_pelanggan': nama_pelanggan,
                'paymentMethod': order_data['paymentMethod'],
                'alamat': order_data['alamat'],
                'tgl_pengambilan': order_data['tgl_pengambilan'],
                'tgl_pengantaran': order_data['tgl_pengantaran'],
                'status': order_data['status']
            })
            
# Fungsi untuk memuat data tempat laundry dari CSV
def load_tempat_laundry():
    with open('files/laundries.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        tempat_laundry = list(reader)
    return tempat_laundry

# Fungsi untuk memuat data paket laundry dari CSV
def load_paket_laundry():
    paket_laundry = {}
    with open('files/wash_packets.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        paket_laundry = list(reader)
    return paket_laundry

# Memuat data tempat laundry dan paket laundry dari CSV saat program dimulai
tempat_laundry = load_tempat_laundry()
paket_laundry = load_paket_laundry()
nama_tempat = {}

# Tabel Order
order = {} 

# Tabel Pemesanan Laundry
pemesanan = {
    "id": None,
    "id_user": None,
    "nama_pelanggan": None,
    "paymentMethod": None,
    "alamat": None,
    "tgl_pengambilan": None,
    "tgl_pengantaran": None,
    "status": "Belum Selesai",  # Default status
    "order": {}
}

def main_menu():
    print("\n--- Laundry ---")
    print("1. Pilih Laundry Menu")
    print("2. Tampilkan Pemesanan Laundry")
    print("0. Keluar")
    pilih = input("\nMasukkan pilihan: ")
    return pilih

# Fungsi untuk menampilkan opsi tempat laundry
def tampilkan_opsi_tempat_laundry():
    print("===============================")
    print("|      Pilih Tempat Laundry  |")
    print("===============================")
    # for id, nama in tempat_laundry.items():
    #     print(f"{id}. {nama}")
    for laundry in tempat_laundry:
        print(f"{laundry['id']}. {laundry['nama']}")

# Fungsi untuk menampilkan paket laundry dari tempat yang dipilih
def tampilkan_paket_laundry(nama_tempat):
    print("===============================")
    print(f"|       Menu {nama_tempat}      |")
    print("===============================")
    print(paket_laundry)

# Fungsi untuk menampilkan menu
def tampilkan_menu(nama_tempat):
    print(f"============================")
    print(f"|       Menu {nama_tempat}      |")
    print(f"============================")
    for data in paket_laundry:
        print(f"{data['id_laundry']}. {data['nama_paket']}: {data['durasi']} Hari {data['unit']}/Rp{data['harga']}")


# Fungsi untuk membuat order baru
def buat_pemesanan_dan_order():
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    alamat_pelanggan = input("Masukkan alamat pelanggan: ")
    metode_pembayaran = input("Masukkan metode pembayaran: ")
    alamat_pengambilan = input("Masukkan alamat pengambilan: ")
    tgl_pengambilan = input("Masukkan tanggal pengambilan (YYYY-MM-DD): ")
    tgl_pengantaran = input("Masukkan tanggal pengantaran (YYYY-MM-DD): ")

    pemesanan['nama_pelanggan'] = nama_pelanggan  # Inisialisasi informasi pelanggan di variabel 'pemesanan'
    pemesanan['alamat_pelanggan'] = alamat_pelanggan
    pemesanan['paymentMethod'] = metode_pembayaran
    pemesanan['alamat'] = alamat_pengambilan
    pemesanan['tgl_pengambilan'] = tgl_pengambilan
    pemesanan['tgl_pengantaran'] = tgl_pengantaran

    tampilkan_menu(nama_tempat)
    id_menu = int(input("Masukkan ID menu yang ingin dipesan: "))
    jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))

    temukan_menu = None
    for menu in paket_laundry:
        if int(menu['id_laundry']) == id_menu:
            temukan_menu = menu
            break
    
    if temukan_menu:
        total_price = int(temukan_menu['harga']) * jumlah
        order[id_menu] = {
            'nama': temukan_menu['nama_paket'],
            'harga': int(temukan_menu['harga']),
            'jumlah': jumlah,
            'total_harga': total_price,
            'id_user': pemesanan['id_user'],
            'paymentMethod': pemesanan['paymentMethod'],
            'alamat': pemesanan['alamat'],
            'tgl_pengambilan': pemesanan['tgl_pengambilan'],
            'tgl_pengantaran': pemesanan['tgl_pengantaran'],
            'status': pemesanan['status']
        }
        print("Order berhasil ditambahkan!")

        # Ambil ID user (contoh: ID user diambil dari input)
        id_user = input("Masukkan ID user: ")

        # Simpan order ke dalam file CSV setelah ditambahkan
        save_order_to_csv(order, nama_tempat, nama_pelanggan, id_user)
    else:
        print("ID menu tidak valid.")
        
# Fungsi untuk menampilkan order
def tampilkan_order():
    print("Order Laundry:")
    print("==============")
    for idx, data in order.items():
        print(f"{idx}. {data['nama']} - Rp{data['harga']} x {data['jumlah']} = Rp{data['total_harga']}")

# Fungsi untuk mengupdate order
def update_order():
    tampilkan_order()
    id_order = int(input("Masukkan ID order yang ingin diupdate: "))
    
    if id_order in order:
        jumlah_baru = int(input("Masukkan jumlah baru: "))
        total_harga_baru = order[id_order]['harga'] * jumlah_baru
        order[id_order]['jumlah'] = jumlah_baru
        order[id_order]['total_harga'] = total_harga_baru
        print("Order berhasil diupdate!")
    else:
        print("ID order tidak valid.")

# Fungsi untuk menghapus order
def hapus_order():
    tampilkan_order()
    id_order = int(input("Masukkan ID order yang ingin dihapus: "))
    
    if id_order in order:
        del order[id_order]
        print("Order berhasil dihapus!")
    else:
        print("ID order tidak valid.")
 
# Fungsi untuk menampilkan pemesanan laundry
def tampilkan_pemesanan(pemesanan, tempat_laundry, paket_laundry):
    print("Informasi Pemesanan Laundry:")
    print("===========================")
    print(f"ID Pemesanan: {pemesanan['id']}")
    print(f"ID User: {pemesanan['id_user']}")
    print(f"Status Pembayaran: {'Sudah Dibayar' if pemesanan['isPaid'] else 'Belum Dibayar'}")
    print(f"Metode Pembayaran: {pemesanan['paymentMethod']}")
    print(f"Alamat Pengambilan: {pemesanan['alamat']}")
    print(f"Tanggal Pengambilan: {pemesanan['tgl_pengambilan']}")
    print(f"Tanggal Pengantaran: {pemesanan['tgl_pengantaran']}")
    print("Detail Order:")
    
# Main program
while True:
    pilihan_utama = main_menu()
        
    if pilihan_utama == '1':
        tampilkan_opsi_tempat_laundry()
        pilihan_tempat = input("\nMasukkan ID tempat laundry: ")
    
        
        if pilihan_tempat.isdigit() and int(pilihan_tempat) in tempat_laundry:
            nama_tempat = tempat_laundry[int(pilihan_tempat)]
    
            while True:
                print("=================================")
                print(f"|         {nama_tempat}           |")
                print("=================================")
                tampilkan_paket_laundry(nama_tempat)
                break
        while True:
            print("=================================")
            print("|         QUICK CLEAN           |")
            print("=================================")
            print("|1. Buat Order Baru             |")
            print("|2. Update Order                |")
            print("|3. Hapus Order                 |")
            print("|4. Tampilkan Pemesanan Laundry |")
            print("|0. Kembali                     |")
            print("================================")
            
            pilihan = int(input("Masukkan pilihan: "))
            
            if pilihan == 1:
                buat_pemesanan_dan_order()
            elif pilihan == 2:
                update_order()
            elif pilihan == 3:
                hapus_order()  
            elif pilihan == 4:
                tampilkan_pemesanan(pemesanan, tempat_laundry, paket_laundry)
            elif pilihan == 0:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        
    elif pilihan_utama == '2':
        tampilkan_pemesanan(pemesanan, tempat_laundry, paket_laundry)
    elif pilihan_utama == '0':
        break
    else:
        print("Pilihan tidak valid. silahkan coba lagi")
        
        
    