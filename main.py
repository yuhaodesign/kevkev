##PARKERINGS HUS
from datetime import datetime

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

    def calculate(self, start, end, typ):
        #calculate time difference
        start = datetime.strptime(start, '%H:%M')
        end = datetime.strptime(end, '%H:%M')

        delta = (end - start).seconds

        #Runda
        time = round(delta/1800) / 2

        cost = 0
        
        if typ == "stor":
            cost = time*self.prisStor
        elif typ == "mellan":
            cost = time*self.prisMellan
        elif typ == "liten":
            cost = time*self.prisLiten

        return cost
    
    

    
