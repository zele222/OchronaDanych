from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

dane_jawne = b"0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
klucz = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

# Brak funkcji pad() bo dane mają 64 bajty
szyfr_ecb = AES.new(klucz, AES.MODE_ECB)
kryptog_ecb = szyfr_ecb.encrypt(dane_jawne)

iv = get_random_bytes(16)
szyfr_cbc = AES.new(klucz, AES.MODE_CBC, iv)
kryptog_cbc = szyfr_cbc.encrypt(dane_jawne)

fragmenty_ecb = []
for i in range(0, 64, 16):
    blok = kryptog_ecb[i:i+16]
    fragmenty_ecb.append(blok.hex())

fragmenty_cbc = []
for i in range(0, 64, 16):
    blok = kryptog_cbc[i:i+16]
    fragmenty_cbc.append(blok.hex())

print(fragmenty_ecb)
print(fragmenty_cbc)

szyfr_ecb_odszyfruj = AES.new(klucz, AES.MODE_ECB)
odszyfrowane_ecb = szyfr_ecb_odszyfruj.decrypt(kryptog_ecb)

szyfr_cbc_odszyfruj = AES.new(klucz, AES.MODE_CBC, iv)
odszyfrowane_cbc = szyfr_cbc_odszyfruj.decrypt(kryptog_cbc)

print(dane_jawne == odszyfrowane_ecb)
print(dane_jawne == odszyfrowane_cbc)