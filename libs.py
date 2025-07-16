import random

def welcomeMessage(title):
    style = "*" * (len(title) + 6)
    print(style)
    print(f"** {title} **")
    print(style)
    
def acakGoa():
    goaBenar = (random.randint(1,4))
    bentukGoa = "|_|"
    goa = [bentukGoa] * 4
    goaMarmut = goa.copy()
    goaMarmut[goaBenar - 1] = "|0_0|"
    
    realGoa = ' '.join(goa)
    realGoaMarmut = ' '.join(goaMarmut)
    return realGoa,realGoaMarmut,goaBenar