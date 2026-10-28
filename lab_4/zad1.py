import hashlib
import os

with open('SHA256SUMS.txt', 'r', encoding='utf-8') as plik:
    for linia in plik:
        oczekiwany_skrot = linia[:64]
        sciezka_pliku = linia[66:].strip()
        
        if not os.path.exists(sciezka_pliku):
            print(f"{sciezka_pliku}: brak")
        else:
            with open(sciezka_pliku, 'rb') as plik_we:
                aktualny_skrot = hashlib.sha256(plik_we.read()).hexdigest()
                if aktualny_skrot == oczekiwany_skrot:
                    print(f"{sciezka_pliku}: ok")
                else:
                    print(f"{sciezka_pliku}: blad")
ala = hashlib.sha256(b"Ala ma kota.").digest()
ola = hashlib.sha256(b"Ola ma kota.").digest()

rozne_bity = 0

for i in range(len(ala)):
    b1 = ala[i]
    b2 = ola[i]
    tekst_binarny = bin(b1 ^ b2)
    count_roznica = tekst_binarny.count('1')
    
    rozne_bity = rozne_bity + count_roznica

print(f"Rozni sie o {rozne_bity} bitow")