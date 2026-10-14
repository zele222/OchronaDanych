def v_szyfr(dane, klucz):
    if not klucz:
        return dane
    m = len(klucz)
    wynik = bytearray()
    for i in range(len(dane)):
        wynik.append((dane[i] + klucz[i % m]) % 256)
    return bytes(wynik)

def v_odszyfr(dane, klucz):
    if not klucz:
        return dane
    m = len(klucz)
    wynik = bytearray()
    for i in range(len(dane)):
        wynik.append((dane[i] - klucz[i % m]) % 256)
    return bytes(wynik)

with open('tekst_pl.txt', 'rb') as f:
    dane_jawne = f.read()

klucz = b"ZAMEK"
kryptog = v_szyfr(dane_jawne, klucz)

with open('vigenere.bin', 'wb') as f:
    f.write(kryptog)

#testy
odszyfrowane = v_odszyfr(kryptog, klucz)
print(dane_jawne == odszyfrowane)

puste = b""
print(v_szyfr(puste, klucz) == puste)

skrajne = bytes([0, 255])
zaszyfrowane_skrajne = v_szyfr(skrajne, klucz)
odszyfrowane_skrajne = v_odszyfr(zaszyfrowane_skrajne, klucz)
print(odszyfrowane_skrajne == skrajne)
print(repr(odszyfrowane_skrajne))

tekst = b"BRAMABRAMABRAMA"
klucz_szyfr = b"SZYFR"
klucz_kod = b"KOD"

kryptog_szyfr = v_szyfr(tekst, klucz_szyfr)
kryptog_kod = v_szyfr(tekst, klucz_kod)

hex_szyfr = kryptog_szyfr.hex()
hex_kod = kryptog_kod.hex()

fragmenty_szyfr = []
for i in range(0, len(hex_szyfr), 10):
    fragmenty_szyfr.append(hex_szyfr[i:i+10])

fragmenty_kod = []
for i in range(0, len(hex_kod), 10):
    fragmenty_kod.append(hex_kod[i:i+10])

print(fragmenty_szyfr)
print(fragmenty_kod)


# Powtarzające się fragmenty kryptogramu powstają w pierwszym przypadku, 
# ponieważ długość słowa BRAMA jest wielokrotnością długości klucza SZYFR,
# wiec każde wystąpienie tego słowa jest szyfrowane tym samym fragmentem cyklu klucza.
# W przypadku klucza KOD występuje przesunięcie, więc każde słowo BRAMA
# trafia na inny układ liter klucza i generuje inny wynik. 
# Dla atakującego takie powtórzenia zdradzają, że długość klucza
# to najpewniej największy wspólny dzielnik odległości między tymi powtórzeniami.