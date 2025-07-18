import psycopg2
from libs import exitProgaram

def connect_db():
    return psycopg2.connect(
        dbname="warung_db",
        user="postgres",
        password="Rizky1257",
        host="localhost",
        port="5432"
    )
    
def start():
    print("== menu warung ==")
    print("1, tampilkan barang")
    print("2, tambah barang")
    print("3, kembali")
    pilihan = input("Pilih: ")
    
    if pilihan == "1":
        tampilkan_barang()
    elif pilihan == "2":
        tambah_barang()
    elif pilihan == "3":
        exitProgaram()
    else:
        print("pilih yang bener")

def tampilkan_barang():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT kode_barang, nama_barang, harga FROM barang")
    rows = cur.fetchall()
    
    print("\n=== Daftar Brang ===")
    for row in rows:
        print(f"Kode : {row[0]} | Nama {row[1]} | harga {row[2]} ")
    
    cur.close()
    conn.close()
    
def tambah_barang():
    kode = input("masukan kode barang : ")
    nama = input("masukan nama barang : ")
    harga = int(input("masukan harga barang : "))
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute (
        "INSERT INTO barang (kode_barang, nama_barang, harga) VALUES (%s, %s, %s)",
        (kode,nama,harga)
    )
    conn.commit()
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    start()
