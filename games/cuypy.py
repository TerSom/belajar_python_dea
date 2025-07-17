import random
import main

def start():
    while True:
        bentukGoa = "|_|"
        goa = [bentukGoa] * 4
        goaMarmut = goa.copy()
        goaBenar = int(random.randint(1,4))
        goaMarmut[goaBenar - 1] = "|0_0|"
                
        realGoa = ' '.join(goa)
        realGoaMarmut = ' '.join(goaMarmut)
        
        print (f"sekrang kamu pilih goa yang benar ya \n\n{realGoa}\n")
        
        pilihanUser = int(input("menurut kamu goa yang benar yang mana ya [1/2/3/4] : "))
        
        while pilihanUser not in [1,2,3,4]:
            pilihanUser = int(input("menurut kamu goa yang benar yang mana ya [1/2/3/4] : "))
        
        if pilihanUser == goaBenar:
                print(f''' 
            {realGoaMarmut}
                    ''')
                print(f"selamat pilihan kamu benar pilihin kamu {pilihanUser}. angka yaitu adalah {goaBenar}")
        else:
                print(f''' 
            {realGoaMarmut}
                    ''')
                print(f"yah sayang sekali kamu salah pilihan kamu {pilihanUser}. ankga yang benar adalah {goaBenar}")
        
        isDone = input("apakah mau lanjut (y/n) :").lower()
        if isDone == "n":
            main.menu()

if __name__ == "__main__":
    start()
    