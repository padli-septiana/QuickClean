import random
from ..files import files as fl

def getLaundryFromOrder(id_order):
    orders = fl.read_from_csv("orders.csv")
    orderItems = fl.read_from_csv("order_items.csv")
    washPackets = fl.read_from_csv("wash_packets.csv")
    laundries = fl.read_from_csv("laundries.csv")
    for orderItem in orderItems:
        if orderItem['id_order'] == str(id_order):
            for washPacket in washPackets:
                if washPacket['id'] == orderItem['id_items']:
                    for laundry in laundries:
                        if laundry['id'] == washPacket['id_laundry']:
                            return laundry['nama']

def getWasPacketFromId(id):
    washPackets = fl.read_from_csv("wash_packets.csv")
    for washPacket in washPackets:
        if washPacket['id'] == str(id):
            return washPacket

def countListDictId(dict, criteria, value):
    count = 0
    for item in dict:
        if item[criteria] == value:
            count += 1
    return count

def getHargaOrderItem(id_order_item):
    orderItems = fl.read_from_csv("order_items.csv")
    washPackets = fl.read_from_csv("wash_packets.csv")
    for orderItem in orderItems:
        if orderItem['id'] == str(id_order_item):
            for washPacket in washPackets:
                if washPacket['id'] == orderItem['id_items']:
                    return int(int(washPacket['harga']) * float(orderItem['quantity']))
                
def getTotalTagihan(id_order):
    orderItems = fl.read_from_csv("order_items.csv")
    washPackets = fl.read_from_csv("wash_packets.csv")
    total = 0
    for orderItem in orderItems:
        if orderItem['id_order'] == str(id_order):
            for washPacket in washPackets:
                if washPacket['id'] == orderItem['id_items']:
                    total += int(int(washPacket['harga']) * float(orderItem['quantity']))
    return total

def menu(user_id):
    laundries = fl.read_from_csv("laundries.csv")
    print("Menu order")
    print("0. Kembali")
    print("1. Cuci sekarang")
    print("2. Lihat riwayat")
    menu = input("Masukkan menu: ")
    if menu == '1':
        for laundry in laundries:
            print(f"{laundry['id']}. {laundry['nama']} - {laundry['wilayah']}")
        selectLaundry = input("Pilih laundry: ")
        order(selectLaundry, user_id)
    elif menu == '2':
        history(user_id)

def order(id_laundry, id_user):
    orders = fl.read_from_csv("orders.csv")

    id = max([int(order['id']) for order in orders]) + 1 if orders else 1
    while True:
        alamat = input("Masukkan alamat anda: ")
        if alamat == "":
            print("Alamat tidak boleh kosong")
        else:
            break
    while True:
        tgl_pengambilan = input("Masukkan tanggal pengambilan (dd-mm-yyyy): ")
        if tgl_pengambilan == "":
            print("tanggal pengambilan tidak boleh kosong")
        else:
            break
    while True:
        paymentMethod = input("Pilih metode pembayaran (qris/cash): ")
        if paymentMethod == "":
            print("metode pembayaran tidak boleh kosong")
        else:
            break

    order = {
        'id': id,
        'id_user': id_user,
        'isPaid': False,
        'paymentMethod': paymentMethod,
        'alamat': alamat,
        'tgl_pengambilan': tgl_pengambilan,
        'tgl_pengantaran': '',
        'status': 'Menunggu diambil'
    }
    
    orderItems = addOrderItems(order, id_laundry, id_user)
    jmlpaket = countListDictId(orderItems, 'id_order', order['id'])
    
    if input(f"Konfirmasi cucian dengan {jmlpaket} paket? (y/n): ") == 'y':
        orders.append(order)
        fl.write_to_csv("orders.csv", orders)
        fl.write_to_csv("order_items.csv", orderItems)
        print("Berhasil menambahkan order")
        print("Silahkan tunggu konfirmasi dari mitra laundry")
        menu(id_user)
    else:
        print("Order dibatalkan")
        menu(id_user)

def printWashPackets(id_laundry):
    washPackets = fl.read_from_csv("wash_packets.csv")
    for washPacket in washPackets:
        if washPacket['id_laundry'] == id_laundry:
            print(f"{washPacket['id']}. {washPacket['nama']} - {washPacket['harga']}")

def addOrderItems(order, id_laundry, id_user):
    orderItems = fl.read_from_csv("order_items.csv")
    wash_packets = fl.read_from_csv("wash_packets.csv")
    while True:
        print("\nPilih paket cuci")
        printWashPackets(id_laundry)
        item = input("Masukkan paket cuci (0 untuk kembali): ")
        isExist = False
        for paket in wash_packets:
            if paket['id'] == item and paket['id_laundry'] == id_laundry:
                isExist = True
        if item == '' or isExist == False:
            print("Paket cuci tidak ditemukan")
            continue
        
        id = max([int(orderItem['id']) for orderItem in orderItems]) + 1 if orderItems else 1
        orderItem = {
            'id': id,
            'id_order': order['id'],
            "id_items": item,
            'quantity': 0
        }
        orderItems.append(orderItem)
        tambah = input("Tambah paket lainnya? (n): ")
        if tambah == 'n':
            return orderItems
        else:
            continue

def detilOrder(id_order, id_user):
    orders = fl.read_from_csv("orders.csv")
    orderItems = fl.read_from_csv("order_items.csv")
    for order in orders:
        if order['id'] == id_order:
            jmlhPaket = countListDictId(orderItems, 'id_order', order['id'])
            print(f"\nAlamat: {order['alamat']}")
            print(f"Pengambilan: {order['tgl_pengambilan']}")
            print(f"Pengantaran: {order['tgl_pengantaran'] if order['tgl_pengantaran'] != '' else 'Belum dibuat'}")
            print(f"Pembayaran: {order['paymentMethod']}")
            print(f"Pelunasan: {order['isPaid'] if order['isPaid'] != 'False' else 'Belum dibayar'}")
            print(f"Status: {order['status']}")
            print(f"Jumlah paket: {jmlhPaket}")
            if order['status'] != 'Menunggu diambil': print(f"Tagihan: Rp.{getTotalTagihan(order['id'])}\n")
            print("Paket cuci:")
            
            for orderItem in orderItems:
                packet = getWasPacketFromId(orderItem['id_items'])
                if order['status'] == "Menunggu diambil":
                    print(f'{packet["nama"]} - Rp.{packet["harga"]}/{packet["unit"]}')
                else:
                    print(f'{packet["nama"]} - {orderItem["quantity"]} {packet["unit"]} - Rp.{getHargaOrderItem(orderItem["id"])}')

            if order['status'] == "Menunggu diambil":
                print("\nSilahkan tunggu cucian anda diambil laundry")
                input("Tekan enter untuk melanjutkan...\n")
            elif order['status'] == "Sedang dicuci" or order['status'] == "Menunggu diantar":
                if order['paymentMethod'] == "cash" or order['isPaid'] == 'True':
                    print("\nSilahkan tunggu cucian anda selesai dicuci")
                    input("Tekan enter untuk melanjutkan...\n")
                elif order['paymentMethod'].lower() == "qris" and order['isPaid'] == 'False':
                    print("\nSilahkan lakukan pembayaran melalui qris")
                    print(f"Total Tagihan: Rp.{getTotalTagihan(order['id'])}")
                    print(f"Nomor Pembayaran: {random.randint(10**12, 10**13 - 1)}")

                    print("0. Kembali")
                    print("1. Konfirmasi pembayaran")
                    menuPembayaran = input("Masukkan menu: ")
                    if menuPembayaran == '1':
                        order['isPaid'] = 'True'
                        fl.write_to_csv("orders.csv", orders)
                        print("Pembayaran berhasil")
                        input("Tekan enter untuk melanjutkan...\n")
                    else:
                        print('')
            elif order['status'] == "Sudah diantar":
                pilih = input("Konfirmasi pesanan selesai? (y): ")
                if pilih == 'y':
                    order['status'] = 'Selesai'
                    fl.write_to_csv("orders.csv", orders)
                    print("Pesanan selesai")
                    input("Tekan enter untuk melanjutkan...\n")
                else:
                    print('')
            elif order['status'] == "Selesai":
                input("Tekan enter untuk melanjutkan...\n")

    menu(id_user)

def history(id_user):
    orders = fl.read_from_csv("orders.csv")
    for order in orders:
        if order['id_user'] == str(id_user):
            print(f'\n{order["id"]}. {getLaundryFromOrder(order["id"])} - {order["tgl_pengambilan"]} - {order["status"]}')

    id_order = input("Pilih order (0 untuk kembali): ")
    if id_order != '' or id_order != '0':
        detilOrder(id_order, id_user)
    else:
        menu(id_user)