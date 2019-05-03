# -*- coding: cp1252 -*-
import json
from main import *

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

        choice = input('Val: ').lower()

        if choice == 'i':
            print('Inpassage/Utpassage!')
            reg = input('Ange regsitreringsnummer: ').upper()
            start = input('Ange starttid: ')
            end = input('Ange sluttid: ')

            for bil in pHus.bilar:
                if reg == bil.reg:
                    bil.addParkering((start,end))
            
            
        elif choice == 'f':
            print('Hämta data från fil!')
            fil = 'data.txt' #input('Ange filnamn: ')

            with open(fil, 'r') as _file:  
                parkeringar = json.load(_file)

                for key, value in parkeringar.items():
                    bil = Bil(key, value["typ"], value["parkeringar"])
                    pHus.addBil(bil)
            
        elif choice == 'n':
            print('Lägg till ny bil!')
            reg = input('Ange registreringsnummer: ')
            typ = input('Ange biltyp (liten, mellan, stor): ')

            newBil = Bil(reg, typ)

            pHus.addBil(newBil)
            
        elif choice == 'p':
            print('Räkna Kostnad')
            reg = input('Ange registreringsnummer: ').upper()

            index = 0
            for bil in pHus.bilar:
                i = 0
                if bil.reg == reg:
                    index = i

            bil = pHus.bilar[index]

            tot = 0

            for park in bil.parkeringar:
                tot += pHus.calculate(park[0],park[1],bil.typ)    
            
            print(tot)

            
        elif choice == 'v':
            print('Historik')
            reg = input('Ange registreringsnummer: ').upper()
            
            index = 0
            for bil in pHus.bilar:
                i = 0
                if bil.reg == reg:
                    index = i

            bil = pHus.bilar[index]

            for park in bil.parkeringar:
                print('start: ' + park[0] + ', end: ' + park[1])
            
        elif choice == 's':
            data = {}
            for bil in pHus.bilar:
                data[bil.reg] = {'parkeringar': bil.parkeringar, 'typ': bil.typ}
            
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
            break

        elif choice == 't':
            for bil in pHus.bilar:
                print(bil.reg)

        
        else:
            print('Inte ett giltigt val!\n \n')

if __name__ == '__main__' : main()

