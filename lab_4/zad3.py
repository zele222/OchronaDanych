import hashlib

def pobierz_h24(dane):
    return hashlib.sha256(dane).hexdigest()[:6]

def pobierz_warianty(nazwa_pliku):
    with open(nazwa_pliku, 'rb') as plik:
        linie = plik.readlines()
    
    warianty_dokumentu = {}
    for numer_wariantu in range(8192):
        zmodyfikowane_linie = []
        for indeks, linia in enumerate(linie):
            if indeks < 13 and ((numer_wariantu >> indeks) & 1):
                if linia.endswith(b'\n'):
                    zmodyfikowane_linie.append(linia[:-1] + b' \n')
                else:
                    zmodyfikowane_linie.append(linia + b' ')
            else:
                zmodyfikowane_linie.append(linia)
                
        tresc = b''.join(zmodyfikowane_linie)
        skrot_h24 = pobierz_h24(tresc)
        
        if skrot_h24 not in warianty_dokumentu:
            warianty_dokumentu[skrot_h24] = numer_wariantu
            
    return warianty_dokumentu

warianty_oryginal = pobierz_warianty('oryginal.txt')
warianty_zmieniony = pobierz_warianty('zmieniony.txt')

for skrot_h24, numer_zmienionego in warianty_zmieniony.items():
    if skrot_h24 in warianty_oryginal:
        print(f"Para: h24: {skrot_h24} (v_oryginał: {warianty_oryginal[skrot_h24]}, v_zmieniony: {numer_zmienionego})")
        break

with open('oryginal.txt', 'rb') as plik:
    bazowy_skrot_oryginalu = pobierz_h24(plik.read())
    
liczba_takich_samych = sum(1 for skrot_h24 in warianty_zmieniony.keys() if skrot_h24 == bazowy_skrot_oryginalu)
print(f"Liczba wariantow zmienionego o h24 równym v=0 oryginału: {liczba_takich_samych}")