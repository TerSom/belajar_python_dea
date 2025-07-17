import random
import socket
from time import sleep

PC_NAME = socket.gethostname()



def welcomeMessage():
    style = "*" * (len(PC_NAME) + 6)
    print(style)
    print(f"** {PC_NAME} **")
    print(style)
    
def exitProgaram():
    print("program akan di hentikan")
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('program berhasil di berhentikan ')
    
if __name__ == "__main__":
    welcomeMessage()
    exitProgaram()
    
def acakGoa():
    goaBenar = (random.randint(1,4))
    bentukGoa = "|_|"
    goa = [bentukGoa] * 4
    goaMarmut = goa.copy()
    goaMarmut[goaBenar - 1] = "|0_0|"
    
    realGoa = ' '.join(goa)
    realGoaMarmut = ' '.join(goaMarmut)
    return realGoa,realGoaMarmut,goaBenar