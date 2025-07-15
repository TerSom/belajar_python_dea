import random


while True:
    welcome_message = "WELCOME TO CUYCP GAME"
    goaBenar = random.randint(1,4)

    print("*****************************")
    print(f"*** {welcome_message} ***")
    print("*****************************")

    namaPlayer = input("masukan nama anda : ")

    print (f'''
    halo {namaPlayer} sekrang kamu pilih goa yang benar ya

    |_| |_| |_| |_|
    ''')
    pilihanUser = int(input("menurut kamu goa yang benar yang mana ya [1/2/3/4] : "))
    
    confirmasiUser = input(f"apakah kamu yakin memilih angka {pilihanUser} (y/n) : ")
    if confirmasiUser == "y":
        if pilihanUser == goaBenar:
            print(f"selamat {namaPlayer} pilihan kamu benar pilihin kamu {pilihanUser}. angka yaitu adalah {goaBenar}")
        else:
            print(f"yah {namaPlayer} sayang sekali kamu salah pilihan kamu {pilihanUser}. ankga yang benar adalah {goaBenar}")
    
    
    isDone = input("apakah mau lanjut (y/n) :").lower()
    if isDone == "n":
        break
    
        
        
    