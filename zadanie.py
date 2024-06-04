import stegano
from PIL import Image
import time
import os
def ukryj(sciezka_in, sciezka, message):
        image = Image.open(sciezka_in)
        print("Obraz został pomyślnie otwarty.")
        
        x = stegano.lsbset.hide(sciezka_in, message, stegano.lsbset.generators.fibonacci())

        x.save(sciezka)


def odkryj(sciezka):
        image = Image.open(sciezka)
        print("Obraz został pomyślnie otwarty.")

        y = stegano.lsbset.reveal(sciezka, stegano.lsbset.generators.fibonacci())
        print("Wiadomość została pomyślnie odkryta.")
        return y



def sprawdz(sciezka_in,sciezka_out,message):
      
        waga_bajty1 = os.path.getsize(r'c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/test2.png')

        start_time = time.time()
        ukryj(sciezka_in, sciezka_out, message)
        end_time = time.time()
        waga_bajty2 = os.path.getsize(r'c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/test3.png')
        time_final = end_time - start_time

        revealed_message = odkryj(sciezka_out)


        if revealed_message:
                waga = waga_bajty2 - waga_bajty1
                return waga,time_final
        else:
                print("Nie udało się odkryć wiadomości.")

sciezka_in = [r"c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/test2.png",r"c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/obrazug1.png",r"c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/obrazug2.png"]
sciezka_out = [r"c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/test3.png",r"c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/obrazug3.png",r"c:/Users/a.jarzab/OneDrive - PIRXON SA/Desktop/obrazug4Y.png"]
nazwa = ["test3.png"]

wyniki_czas = []
wyniki_waga = []
for i in range(len(sciezka_in)):
    print(i)
    wiadomosc = ["1","11","111"]
    zdjecie_waga = []
    zdjecie_czas = []
    for j in range(3):
        x,y = sprawdz(sciezka_in[i],sciezka_out[i],wiadomosc[j])
        zdjecie_waga.append(x)
        zdjecie_czas.append(y)
    wyniki_czas.append(zdjecie_czas)
    wyniki_waga.append(zdjecie_waga)
print(wyniki_czas)
print(wyniki_waga)