print("---QUICK CLEAN---")
print("=====================\n")

data_user = {}
def login():
    email_us = input("Email :")
    password_us = input("Password :")
    if email_us in data_user and data_user[email_us]["password"] == password_us:
        print("Selamat Datang di QUICK CLEAN")
    else:
        print("Username atau Password Salah")

def regist():
    print("Daftar")
    print("=========\n")
    input_email = input("Email:")
    input_password = input("Password: ")
    input_username = input("Nama Pengguna: ")
    input_nomor = input("Nomor HP: ")
    input_namaLengkap = input("Nama Lengkap: ")
    input_tl = input("Tanggal Lahir: ")

    data_user[input_email] = {
        "password" : input_password,
        "Nama Pengguna" : input_username,
        "Nomor HP" : input_nomor,
        "Nama Lengkap" : input_namaLengkap,
        "Tanggal Lahir" : input_tl
    }   

    print("SELAMAT DATANG DI QUICK CLEAN")
    print("================================\n")

def main():
    while True:
        print("SUDAH PUNYA AKUN?")
        print("1. Login")
        print("2. Daftar")
        pilihan = input("Masukan Opsi: ")

        if pilihan == "1":
            login()
        elif pilihan == "2":
            regist()
        else:
            print("Opsi Tidak ditemukan, silahkan pilih kembali")  


if __name__ == "__main__":
    main()