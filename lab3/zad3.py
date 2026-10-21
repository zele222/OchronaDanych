import math
from collections import Counter
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def licz_entropie(dane):
    if not dane:
        return 0.0
    dlugosc = len(dane)
    histogram = Counter(dane)
    entropia = 0.0
    for ilosc in histogram.values():
        prawdopodobienstwo = ilosc / dlugosc
        entropia -= prawdopodobienstwo * math.log2(prawdopodobienstwo)
    return entropia

with open('slaby_ecb.bin', 'rb') as f:
    kryptog = f.read()

probka = kryptog[:4096]
alfabet = "abcdefghijklmnopqrstuvwxyz0123456789"
wyniki = []

for znak in alfabet:
    klucz = (znak * 16).encode('ascii')
    szyfr = AES.new(klucz, AES.MODE_ECB)
    odszyfrowana_probka = szyfr.decrypt(probka)
    entropia = licz_entropie(odszyfrowana_probka)
    wyniki.append((znak, entropia))

wyniki.sort(key=lambda x: x[1])

for znak, entropia in wyniki[:5]:
    print(f"{znak}: {entropia:.4f}")

najlepszy_znak = wyniki[0][0]
najlepszy_klucz = (najlepszy_znak * 16).encode('ascii')
szyfr_docelowy = AES.new(najlepszy_klucz, AES.MODE_ECB)
odszyfrowane_pelne = unpad(szyfr_docelowy.decrypt(kryptog), 16)

linie = odszyfrowane_pelne.decode('utf-8').splitlines()
print(najlepszy_znak)
print(linie[0])