# -*- coding: cp1252 -*-
import json
from main import *

dummyData = {
    'car1' :{
            1: '12'
    }
}

def main():
    pHus = PHus()
    
    while True:
        print('Välkommen till P-huset!\n')

        print('I  Inpassage/Utpassage...\n' +
              'F  Läs in fil med historik\n' +
              'N  Lägg till ny bil\n' +
              'P  Räkna ut parkeringskostnad för en bil\n' +              
              'V  Visa parkeringshistorik för en bil\n' +          
              'S  Avsluta\n'
              )

        choice = raw_input('Val: ').lower()

        if choice == 'i':
            print('Inpassage/Utpassage!')
            reg = raw_input('Ange regsitreringsnummer: ')
            start = raw_input('Ange starttid: ')
            end = raw_input('Ange sluttid: ')

            parkering = {
                "reg" : reg,
                "start" : start,
                "end" : end
                }

            for bil in pHus.bilar:
                if reg == bil.reg:
                    bil.addParkering((start,end))

            for bil in pHus.bilar:
                print(bil.parkeringar)
            
            
        elif choice == 'f':
            print('Hämta data från fil!')
            fil = 'data.txt' #raw_input('Ange filnamn: ')

            with open(fil, 'r') as _file:  
                parkeringar = json.load(_file)

                for key, value in parkeringar.items():
                    bil = Bil(key, value["typ"], value["parkeringar"])
                    pHus.addBil(bil)

            print(pHus.bilar)
            
        elif choice == 'n':
            print('Lägg till ny bil!')
            reg = raw_input('Ange registreringsnummer: ')
            typ = raw_input('Ange biltyp (liten, mellan, stor): ')

            newBil = Bil(reg, typ)

            pHus.addBil(newBil)
            
        elif choice == 'p':
            print('Räkna Kostnad')
            
        elif choice == 'v':
            print('Historik')
            
        elif choice == 's':
            data = []
            for bil in pHus.bilar:
                for park in bil.parkeringar:
                    toAdd = {
                        "reg" : bil.reg,
                        "park" : park
                        }
                    data.append(toAdd)
            
            with open('parking_data.txt', 'w') as outfile:
                json.dump(data, outfile)
            break
        
        else:
            print('Inte ett giltigt val!\n \n')

if __name__ == '__main__' : main()

