import csv
import os

def write_to_csv(filename, data):
    filename = os.path.dirname(__file__) + "/../../files/" + filename
    with open(filename, mode='w', newline='', encoding="utf-8-sig") as file:
        fieldnames = data[0].keys() if data else []  # Mengambil nama kolom dari keys dictionary pertama (jika ada)
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # Menulis header (nama kolom)
        writer.writerows(data)  # Menulis baris-baris data

def read_from_csv(filename):
    data = []
    filename = os.path.dirname(__file__) + "/../../files/" + filename
    try:
        with open(filename, mode='r', encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        pass  # File belum ada, atau kosong

    return data

def get_max_id(filename):
    data = read_from_csv(filename)
    max_id = None
    try:
        for row in data:
            current_id = int(row['id'])
            if max_id is None or current_id > max_id:
                max_id = current_id
        return max_id
    except (ValueError, IndexError):
        return 0