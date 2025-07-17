import random

benar = (random.randint(1,4))
bentukGoa = "|_|"
goa = [bentukGoa] * 4
goaMarmut = goa.copy()
goaMarmut[benar - 1] = "|0_0|"
realGoa = ' '.join(goa)
realGoaMarmut = ' '.join(goaMarmut)




        
        
    