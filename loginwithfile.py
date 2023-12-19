import csv

print("---QUICK CLEAN---")
print("=====================\n")

data_user = {}

def login():
    email_us = input("Email :")
    password_us = input("Password :")

    try:
        with open("data_user.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Email"] == email_us and row["Password"] == password_us:
                    print("Selamat Datang di QUICK CLEAN")
                    return
    except FileNotFoundError:
        print("Data Tidak Ditemukan, Silahkan Registrasi!")
    
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

    try:
        with open("data_user.csv", "a", newline="") as csvfile:
            fieldnames = ["Email", "Password", "Nama Pengguna", "Nomor HP", "Nama Lengkap", "Tanggal Lahir"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the file is empty and write the header if needed
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({
                "Email": input_email,
                "Password": input_password,
                "Nama Pengguna": input_username,
                "Nomor HP": input_nomor,
                "Nama Lengkap": input_namaLengkap,
                "Tanggal Lahir": input_tl
            })

        print("SELAMAT DATANG DI QUICK CLEAN")
        print("================================\n")

    except Exception as e:
        print(f"Error writing to CSV: {e}")


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