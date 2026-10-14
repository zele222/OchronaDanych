with open('cezar.bin', 'rb') as f:
    kryptog = f.read()

wyniki = []

for k in range(256):
    odszyfrowane = bytes([(c - k) % 256 for c in kryptog])
    drukowalne = 0

    for b in odszyfrowane:
        if 32 <= b <= 126 or b in (9, 10, 13):
            drukowalne += 1

    udzial = drukowalne / len(kryptog) if len(kryptog) > 0 else 0
    wyniki.append((-udzial, k, odszyfrowane))

wyniki.sort()

for i in range(5):
    udzial, k, odszyfrowane = wyniki[i]
    print(f"k: {k:3}, ocena: {-udzial:.4f}, {repr(odszyfrowane[:50])}")

najlepszy_tekst = wyniki[1][2]
with open('cezar.txt', 'wb') as f:
    f.write(najlepszy_tekst)

# Uzasadnienie wyboru przesunięcia:
# Poprawne przesunięcie (233) to takie dla którego ocena jest najwyższa, a początek 
# odszyfrowanego tekstu jest czytelny.

# Dlaczego sama entropia nie rozstrzygnie przesunięcia:
# Kształt histogramu pozostaje identyczny - zmieniają się jedynie przypisane bajtom pozycje.
# Wzór na entropię zależy tylko od samego zbioru prawdopodobieństw.