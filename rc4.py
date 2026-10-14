import itertools
import time
import math
from collections import Counter

def rc4(dane, klucz):
    S = bytearray(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + klucz[i % len(klucz)]) % 256
        S[i], S[j] = S[j], S[i]
    
    wynik = bytearray()
    i = 0
    j = 0
    for bajt in dane:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        wynik.append(bajt ^ K)
    
    return bytes(wynik)

def oblicz_entropie(dane):
    if not dane:
        return 0.0
    dlugosc = len(dane)
    histogram = Counter(dane)
    entropia = 0.0
    for ilosc in histogram.values():
        prawdopodobienstwo = ilosc / dlugosc
        entropia -= prawdopodobienstwo * math.log2(prawdopodobienstwo)
    return entropia



with open('rc4.bin', 'rb') as f:
    kryptogram = f.read()

start_czas = time.perf_counter()

alfabet = [ord(c) for c in 'abcdefghijklmnopqrstuvwxyz']
wyniki = []
liczba_prob = 0

for kombinacja in itertools.product(alfabet, repeat=3):
    liczba_prob += 1
    klucz = bytes(kombinacja)
    odszyfrowana_probka = rc4(kryptogram[:512], klucz)
    entropia = oblicz_entropie(odszyfrowana_probka)
    wyniki.append((entropia, klucz))

wyniki.sort(key=lambda x: (x[0], x[1]))
czas_szukania = time.perf_counter() - start_czas

najlepszy_klucz = wyniki[0][1]
odszyfrowana_calosc = rc4(kryptogram, najlepszy_klucz)

with open('rc4.txt', 'wb') as f:
    f.write(odszyfrowana_calosc)

print(f"Wybrany klucz: {repr(najlepszy_klucz)}")
print("Ranking pięciu najlepszych:")
for i in range(5):
    print(f"{i+1}. {repr(wyniki[i][1])} - Entropia: {wyniki[i][0]:.4f}")
print(f"Liczba prób: {liczba_prob}")
print(f"Czas przeszukiwania: {czas_szukania:.4f} s")
print(f"Entropia kryptogramu: {oblicz_entropie(kryptogram):.4f}")
print(f"Entropia odszyfrowania: {oblicz_entropie(odszyfrowana_calosc):.4f}")