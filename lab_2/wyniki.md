# Zadanie 1

## Wyniki:

```text
k: 230, ocena: 1.0000, b'Wkh#Qljkw#Ihuu|\r\rWkh#qljkw#ihuu|#ohiw#wkh#kduerxu#'
k: 233, ocena: 1.0000, b'The Night Ferry\n\nThe night ferry left the harbour '
k: 228, ocena: 0.9948, b'Ymj%Snlmy%Kjww~\x0f\x0fYmj%snlmy%kjww~%qjky%ymj%mfwgtzw%'
k: 229, ocena: 0.9948, b'Xli$Rmklx$Jivv}\x0e\x0eXli$rmklx$jivv}$pijx$xli$levfsyv$'
k: 231, ocena: 0.9948, b'Vjg"Pkijv"Hgtt{\x0c\x0cVjg"pkijv"hgtt{"nghv"vjg"jctdqwt"'
```

### Uzasadnienie wyboru przesunięcia:
Poprawne przesunięcie (233) to takie dla którego ocena jest najwyższa, a początek odszyfrowanego tekstu jest czytelny.

### Dlaczego sama entropia nie rozstrzygnie przesunięcia:
Kształt histogramu pozostaje identyczny - zmieniają się jedynie przypisane bajtom pozycje.
Wzór na entropię zależy tylko od samego zbioru prawdopodobieństw.


# Zadanie 2

## Wyniki:

```text
True
True
True
b'\x00\xff'
['95ac9a9393', '95ac9a9393', '95ac9a9393']
['8da1859890', '869d90918c', '91968c9c85']
```

Powtarzające się fragmenty kryptogramu powstają w pierwszym przypadku, ponieważ długość słowa BRAMA jest wielokrotnością długości klucza SZYFR, wiec każde wystąpienie tego słowa jest szyfrowane tym samym fragmentem cyklu klucza.

W przypadku klucza KOD występuje przesunięcie, więc każde słowo BRAMA trafia na inny układ liter klucza i generuje inny wynik. 

Dla atakującego takie powtórzenia zdradzają, że długość klucza to najpewniej największy wspólny dzielnik odległości między tymi powtórzeniami.


# Zadanie 3

## Wyniki:

```text
Wybrany klucz: b'tat'
Ranking pięciu najlepszych kandydatów:
1. b'tat' - Entropia: 4.3910
2. b'neg' - Entropia: 7.4304
3. b'mcn' - Entropia: 7.4512
4. b'oxo' - Entropia: 7.4536
5. b'tnx' - Entropia: 7.4592
Liczba prób: 17576
Czas przeszukiwania: 13.3598 s
Entropia całego kryptogramu: 7.9271
Entropia całego odszyfrowania: 4.3259
```

Ponowne zaszyfrowanie odszyfrowanego pliku z błędnym kluczem odtworzy kryptogram, ponieważ RC4 szyfruje dane za pomocą operacji XOR - dwukrotne nałożenie tego samego, nawet niepoprawnego strumienia klucza na dowolne dane powoduje powrót do ich pierwotnej postaci.

Ranking oparty na entropii mógłby zawieść, jeśli próbka danych byłaby krótka lub gdyby sam tekst posiadał wysoką entropię (np kompresja). W takich przypadkach prawidłowy klucz dałby wynik o  wysokiej entropii, który zgubiłby się wśród błędnych wyników sprawiających wrażenie szumu.
