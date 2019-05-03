##PARKERINGS HUS
class Bil:
    def __init__(self, reg, typ, parkeringar = []):
        self.reg = reg #Bilens registrerings nummer
        self.typ = typ #Bilens typ (liten, mellan, stor)
        self.parkeringar = parkeringar #Bilens alla parkeringar

    def addParkering(self,parkering):
        self.parkeringar.append(parkering)

class PHus:
    def __init__(self, bilar = []):
        self.bilar = bilar #P-husets alla bilar

        #Parkerings priser
        self.prisStor = 30
        self.prisMellan = 25
        self.prisLiten = 20

    
    def addBil(self, bil):
        self.bilar.append(bil)
                

    

    
