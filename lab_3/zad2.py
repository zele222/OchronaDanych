from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def szyfruj_haslem(dane, haslo):
    sol = get_random_bytes(16)
    iv = get_random_bytes(16)
    klucz = PBKDF2(haslo.encode('utf-8'), sol, dkLen=32, count=200000, hmac_hash_module=SHA256)
    szyfr = AES.new(klucz, AES.MODE_CBC, iv)
    dane_z_wyrownaniem = pad(dane, 16)
    kryptog = szyfr.encrypt(dane_z_wyrownaniem)
    return kryptog, sol, iv

def odszyfruj_haslem(kryptog, haslo, sol, iv):
    klucz = PBKDF2(haslo.encode('utf-8'), sol, dkLen=32, count=200000, hmac_hash_module=SHA256)
    szyfr = AES.new(klucz, AES.MODE_CBC, iv)
    odszyfrowane_z_wyrownaniem = szyfr.decrypt(kryptog)
    return unpad(odszyfrowane_z_wyrownaniem, 16)

haslo_testowe = "aiosandsjaslcoasjknalwnoqpwij1jxqpmwk"

dane_puste = b""
kryptog_puste, sol_puste, iv_puste = szyfruj_haslem(dane_puste, haslo_testowe)
odszyfrowane_puste = odszyfruj_haslem(kryptog_puste, haslo_testowe, sol_puste, iv_puste)
print(dane_puste == odszyfrowane_puste, len(kryptog_puste))

dane_ascii = b"0123456789ABCDEF" 
kryptog_ascii, sol_ascii, iv_ascii = szyfruj_haslem(dane_ascii, haslo_testowe)
odszyfrowane_ascii = odszyfruj_haslem(kryptog_ascii, haslo_testowe, sol_ascii, iv_ascii)
print(dane_ascii == odszyfrowane_ascii, len(kryptog_ascii))

with open('wiadomosc.txt', 'rb') as f:
    dane_plik = f.read()

kryptog_plik1, sol_plik1, iv_plik1 = szyfruj_haslem(dane_plik, haslo_testowe)
odszyfrowane_plik = odszyfruj_haslem(kryptog_plik1, haslo_testowe, sol_plik1, iv_plik1)
print(dane_plik == odszyfrowane_plik, len(kryptog_plik1))

kryptog_plik2, sol_plik2, iv_plik2 = szyfruj_haslem(dane_plik, haslo_testowe)
print(kryptog_plik1 == kryptog_plik2)