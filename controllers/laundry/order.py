import csv
from ..files import files as fl
from ..order import order as od


def getUserNameById(id_user):
    users = fl.read_from_csv("users.csv")
    for user in users:
        if user['id'] == str(id_user):
            return user['nama']

def getLaundryFromOrder(id_order):
    orderItems = fl.read_from_csv("order_items.csv")
    washPackets = fl.read_from_csv("wash_packets.csv")
    laundries = fl.read_from_csv("laundries.csv")
    for orderItem in orderItems:
        if orderItem['id_order'] == str(id_order):
            for washPacket in washPackets:
                if washPacket['id'] == orderItem['id_items']:
                    for laundry in laundries:
                        if laundry['id'] == washPacket['id_laundry']:
                            return laundry

def lihatOrder(id_laundry):
    orders = fl.read_from_csv("orders.csv")
    orderLaundry = []

    print("\nDaftar order")
    for order in orders:
        laundry = getLaundryFromOrder(order['id'])
        if laundry['id'] == id_laundry:
            orderLaundry.append(order)

    for order in orderLaundry:
        print(f"{order['id']}. {getUserNameById(order['id_user'])} - {order['tgl_pengambilan']} - {order['status']}")

    pilihOrder = input("Pilih order (0 untuk kembali): ")
    isExist = False
    for order in orderLaundry:
        if order['id'] == pilihOrder:
            isExist = True
            break

    if (pilihOrder != '' or pilihOrder != '0'):
        if isExist == True:
            detilOrder(pilihOrder, id_laundry)
        else:
            print("Order tidak ditemukan\n")

def detilOrder(id_order, id_laundry):
    orders = fl.read_from_csv("orders.csv")
    orderItems = fl.read_from_csv("order_items.csv")
    washPackets = fl.read_from_csv("wash_packets.csv")

    for order in orders:
        if order['id'] == str(id_order):
            print(f"\nId Order: {order['id']}")
            print(f"Pelanggan: {getUserNameById(order['id_user'])}")
            print(f"Alamat: {order['alamat']}")
            print(f"Tanggal pengambilan: {order['tgl_pengambilan']}")
            if order['status'] != 'Menunggu diambil':
                print(f"Tanggal pengantaran: {order['tgl_pengantaran']}")
            print(f"Pembayaran: {order['paymentMethod']}")
            if order['status'] != 'Menunggu diambil':
                print(f"Pelunasan: {'Sudah lunas' if order['isPaid'] == 'True' else 'Belum lunas'}")
            print("Daftar item")
            for orderItem in orderItems:
                if orderItem['id_order'] == str(id_order):
                    for washPacket in washPackets:
                        if washPacket['id'] == orderItem['id_items']:
                            if order['status'] == 'Menunggu diambil':
                                print(f"{washPacket['nama']}")
                            else:
                                print(f"{washPacket['nama']} - {orderItem['quantity']} {washPacket['unit']}")

            if order['status'] == 'Menunggu diambil':
                inputQuantity(id_order, id_laundry)
            elif order['status'] == 'Sedang dicuci':
                pilih = input("Cucian selesai? (y): ")
                if pilih == 'y':
                    order['status'] = 'Menunggu diantar'
                    fl.write_to_csv("orders.csv", orders)
                    print("Cucian selesai\n")
            elif order['status'] == 'Menunggu diantar':
                if order['paymentMethod'].lower() == 'qris' and order['isPaid'] == 'False':
                    print("Menunggu pembayaran")
                    input("Tekan enter untuk kembali")
                elif (order['paymentMethod'].lower() == 'qris' and order['isPaid'] == 'True') or order['paymentMethod'].lower() == "cash":
                    pilih = input("Cucian sudah diantar? (y): ")
                    if pilih == 'y':
                        konfirmasiAntar(id_order, id_laundry)
            elif order['status'] == 'Sudah diantar':
                print("Menunggu konfirmasi customer")
                input("Tekan enter untuk kembali")

def konfirmasiAntar(id_order, id_laundry):
    orders = fl.read_from_csv("orders.csv")
    for order in orders:
        if order['id'] == str(id_order):
            order['status'] = 'Sudah diantar'
            fl.write_to_csv("orders.csv", orders)
            print("Cucian sudah diantar, tunggu konfirmasi dari customer")
            input("Tekan enter untuk kembali")

def inputQuantity(id_order, id_laundry):
    orderItems = fl.read_from_csv("order_items.csv")
    washPackets = fl.read_from_csv("wash_packets.csv")
    orders = fl.read_from_csv("orders.csv")
    print("\nMasukkan kuantitas cucian")
    for order in orders:
        if order['id'] == id_order:
            for orderItem in orderItems:
                if orderItem['id_order'] == id_order:
                    for washPacket in washPackets:
                        if washPacket['id'] == orderItem['id_items']:
                            orderItem['quantity'] = input(f"{washPacket['nama']} - Kuantitas: ")
            order['status'] = "Sedang dicuci"
            order['tgl_pengantaran'] = input(f"Masukkan tanggal pengantaran (dd-mm-yyyy): ")
    
    fl.write_to_csv("orders.csv", orders)
    fl.write_to_csv("order_items.csv", orderItems)
    print("Cucian sedang dicuci\n")
