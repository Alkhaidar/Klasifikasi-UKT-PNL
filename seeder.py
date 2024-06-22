import mysql.connector
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Fungsi untuk koneksi ke database
def connect_to_mysql():
    try:
        # Ubah parameter sesuai dengan detail koneksi MySQL Anda
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="klasifikasi"
        )
        return connection
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
        return None

def seed_data():
    try:
        # Koneksi ke database
        connection = connect_to_mysql()
        if connection:
            cursor = connection.cursor()
        
        users = [
            ('Al Khaidar', 'admin', 'admin@gmail.com', 'admin'),
        ]
        
        for user in users:
            nama, username, email, password = user
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute("INSERT INTO tbl_users (nama, email, username, password) VALUES (%s, %s, %s, %s)", (nama, email, username, hashed_password))
        
        # Commit perubahan ke database
        connection.commit()
        print("Data seeded successfully.")

        # Tutup kursor dan koneksi
        cursor.close()
        connection.close()
    except Exception as e:
        print("Error while seeding data:", e)
    
# Panggil fungsi seed_data untuk menambahkan data ke tabel
seed_data()
