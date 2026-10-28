Aleksander Żelechowski 337804
Python
https://github.com/zele222/OchronaDanych 

# Zad 1
## wyniki:
```text
dokumenty/budzet.csv: blad
dokumenty/dane.bin: ok
dokumenty/harmonogram.txt: brak
dokumenty/kontakt.txt: ok
dokumenty/regulamin.txt: ok
Rozni sie o 131 bitow
```

Suma kontrolna nie chroni przed celową podmianą, ponieważ atakujący może w tym samym czasie
podmienić plik oraz przypisaną mu jawną sumę kontrolną. Trzeba zastosować kryptograficzne funkcje
skrótu z kluczem (np. HMAC) lub podpis cyfrowy.

# Zad 2
## wyniki:
```text
anna, Kasztan-2026: True
anna, kasztan-2026: False
piotr, Żółw na łące: True
kasia, Kasztan-2026: False
test1: sol: 18a8d221b4cdc10df6b0811244c15dd9 skrot: 214dc507256fc32eb35e
test2: sól: f29f67ce28a8cd01cafc87260e45b4e0 skrot: 2cf9e1066f84fa02a421
True
True
```

Zastosowanie soli dla każdego konta sprawia, że dwa takie same hasła uzyskują po zaszyfrowaniu
inny skrót, a 600 000 iteracji algorytmu obciąża moc obliczeniową maszyny, spowalniając
i utrudniając ataki brute-force lub metodą słownikową.

# Zad 3
## wyniki:
```text
Para: h24: aac6b9 (v_oryginał: 7282, v_zmieniony: 1761)
Liczba wariantow zmienionego o h24 równym v=0 oryginału: 0
```

Znalezienie dowolnej pary jest znacznie łatwiejsze, ponieważ zderzamy ze sobą dwie duże pule
wygenerowanych skrótów (każdy z każdym), co znacznie zwiększa liczbę kombinacji względem szukania
dopasowania tylko do jednego, z góry ustalonego skrótu.