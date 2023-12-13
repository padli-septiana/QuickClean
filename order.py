# Tabel Menu
menu = {
    1: {'nama': 'Cuci Baju', 'harga': 5000},
    2: {'nama': 'Setrika Baju', 'harga': 3000},
    3: {'nama': 'Cuci Sepatu', 'harga': 10000},
    4: {'nama': 'Cuci Karpet', 'harga': 15000},
    5: {'nama': 'Cuci Boneka', 'harga': 8000}
}

# Tabel Order
order = {}

# Tabel Pemesanan Laundry
pemesanan = {}

def main_menu():
    print("\n--- Laundry ---")
    print("1. Pilih Laundry Menu")
    print("2. Tampilkan Pemesanan Laundry")
    print("0. Keluar")
    pilih = input("\nMasukkan pilihan: ")
    return pilih

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("============================")
    print("|       Menu Laundry       |")
    print("============================")
    for id, data in menu.items():
        print(f"{id}. {data['nama']} - Rp{data['harga']}")

# Fungsi untuk membuat order baru
def buat_order():
    tampilkan_menu()
    id_menu = int(input("Masukkan ID menu yang ingin dipesan: "))
    jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
    
    if id_menu in menu:
        total_harga = menu[id_menu]['harga'] * jumlah
        order[id_menu] = {'nama': menu[id_menu]['nama'], 'harga': menu[id_menu]['harga'], 'jumlah': jumlah, 'total_harga': total_harga}
        print("Order berhasil ditambahkan!")
    else:
        print("ID menu tidak valid.")

# Fungsi untuk menampilkan order
def tampilkan_order():
    print("Order Laundry:")
    print("==============")
    for id, data in order.items():
        print(f"{id}. {data['nama']} - Rp{data['harga']} x {data['jumlah']} = Rp{data['total_harga']}")

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
def tampilkan_pemesanan():
    print("Pemesanan Laundry:")
    print("=================")
    print(f"Nama Pelanggan: {pemesanan['nama_pelanggan']}")
    print(f"Alamat Pelanggan: {pemesanan['alamat_pelanggan']}")
    print("Order:")
    for id, data in pemesanan['order'].items():
        status = "Belum Dikerjakan"  # Menambah status pesanan default

        # Ubah status jika pesanan sudah ada dalam pemesanan
        if id in pemesanan['status']:
            if pemesanan['status'][id]:
                status = "Sudah Dikerjakan"

        print(f"{id}. {data['nama']} - Rp{data['harga']} x {data['jumlah']} = Rp{data['total_harga']} ({status})")

# Fungsi untuk membuat pemesanan laundry
def buat_pemesanan():
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    alamat_pelanggan = input("Masukkan alamat pelanggan: ")
    pemesanan['nama_pelanggan'] = nama_pelanggan
    pemesanan['alamat_pelanggan'] = alamat_pelanggan
    pemesanan['order'] = order.copy()
    pemesanan['status'] = {id: False for id in order}
    print("Pemesanan berhasil dibuat!")
    
# Main program
while True:
    pilihan_utama = main_menu()
        
    if pilihan_utama == '1':
        while True:
            print("=================================")
            print("|         QUICK CLEAN           |")
            print("=================================")
            print("|1. Buat Order Baru             |")
            print("|2. Tampilkan Order             |")
            print("|3. Update Order                |")
            print("|4. Hapus Order                 |")
            print("|5. Buat Pemesanan Laundry      |")
            print("|6. Tampilkan Pemesanan Laundry |")
            print("|7. Selesaikan Pemesanan        |")
            print("|0. Kembali                     |")
            print("================================")
            
            pilihan = int(input("Masukkan pilihan: "))
            
            if pilihan == 1:
                buat_order()
            elif pilihan == 2:
                tampilkan_order()
            elif pilihan == 3:
                update_order()
            elif pilihan == 4:
                hapus_order()  
            elif pilihan == 5:
                buat_pemesanan()
            elif pilihan == 6:
                tampilkan_pemesanan()
            elif pilihan == 0:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        
    elif pilihan_utama == '2':
        tampilkan_pemesanan()
    elif pilihan_utama == '0':
        break
    else:
        print("Pilihan tidak valid. silahkan coba lagi")
