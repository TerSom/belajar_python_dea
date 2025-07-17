import random
from libs import welcomeMessage
from libs import acakGoa


goaBenar = int(random.randint(1,4))

welcomeMessage("WELCOME DI GAME DARMAN")
        
namaPlayer = input("masukan nama anda : ")
while namaPlayer == "":
    namaPlayer = input("masukan nama yang benar : ")

bentukGoa = "|_|"
goa = [bentukGoa] * 4
goaMarmut = goa.copy()
goaMarmut[goaBenar - 1] = "|0_0|"
        
realGoa = ' '.join(goa)
realGoaMarmut = ' '.join(goaMarmut)
    
while True:
    realGoa,realGoaMarmut,goaBenar = acakGoa()
    print (f'''
    halo {namaPlayer} sekrang kamu pilih goa yang benar ya
    
    {realGoa}
    ''')
    
    pilihanUser = int(input("menurut kamu goa yang benar yang mana ya [1/2/3/4] : "))
    
    while pilihanUser not in [1,2,3,4]:
        pilihanUser = int(input("menurut kamu goa yang benar yang mana ya [1/2/3/4] : "))
    
    confirmasiUser = input(f"apakah kamu yakin memilih angka {pilihanUser} (y/n) : ")
    if confirmasiUser == "y":
        if pilihanUser == goaBenar:
            print(f''' 
    {realGoaMarmut}
                  ''')
            print(f"selamat {namaPlayer} pilihan kamu benar pilihin kamu {pilihanUser}. angka yaitu adalah {goaBenar}")
        else:
            print(f''' 
    {realGoaMarmut}
                  ''')
            print(f"yah {namaPlayer} sayang sekali kamu salah pilihan kamu {pilihanUser}. ankga yang benar adalah {goaBenar}")
    elif confirmasiUser == "n":
        exit
    else:
        print("masukin yang benar")
    
    isDone = input("apakah mau lanjut (y/n) :").lower()
    if isDone == "n":
        break
    
print("Program selesai")
        
