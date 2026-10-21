# Zad 1

# wyniki:

```text
['a5ba2b6280d433bccfe6a0461cb88c4e', 'a5ba2b6280d433bccfe6a0461cb88c4e', 'a5ba2b6280d433bccfe6a0461cb88c4e','a5ba2b6280d433bccfe6a0461cb88c4e']
['16a9e10b5b2c1a48835bdafc85db6848', 'dc5feb77fba7474e0892d03258fe2f73', '3d6a9d698587f22c2bd5141b196be8c8','e0d5f805f83264d0cfe6a798cc69ea4e']
True
True
```

W trybie ECB wszystkie cztery bloki kryptogramu były identyczne
W trybie CBC wszystkie cztery bloki były różne

Oba porównania zwróciły True, więc dane po odszyfrowaniu w obu trybach są zgodne z tekstem pierwotnym.

W trybie ECB identyczne bloki tekstu są zawsze szyfrowane na ten sam wynik, a w CBC każdy 
blok tekstu przed zaszyfrowaniem jest modyfikowany operacją XOR z poprzednim blokiem kryptogramu 
(na początku z IV), co ukrywa powtarzalne fragmenty.

# Zad 2
## wyniki:
```text
True 16
True 32
True 256
False
```

Podwójne zaszyfrowanie tych samych danych, tym samym 
hasłem zwraca False - kryptogramy są różne

Sól modyfikuje klucz tworzony z hasła, by chronić przed atakami słownikowymi, a wektor IV zmienia pierwszy blok w CBC, żeby identyczne wiadomości dawały zupełnie różne kryptogramy.

# Zad 3
## wyniki:
```text
m: 4.4536
b: 7.9472
x: 7.9490
o: 7.9493
2: 7.9502
m
Record 000. The archive contains laboratory notes about symmetric encryption and careful handling of binary files.
```

Wszystkich kluczy jest 36 bo zadanie ogranicza nas do znakow alfabetu i cyfr (26 + 10), a hasło ma być jednym znakiem powtarzającym się 16 razy.
Ranking zawiedzie dla danych skompresowanych, ponieważ algorytmy kompresji usuwają nadmiarowość tych samych znaków, zwiększając entropię całości tekstu.

