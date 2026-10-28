import hashlib
import hmac
import secrets

def weryfikuj(login, haslo):
    with open('hasla.txt', 'r', encoding='utf-8') as plik:
        for line in plik:
            podzial = line.strip().split(':')
            if len(podzial) == 4 and podzial[0] == login:
                iteracje = int(podzial[1])
                sol = bytes.fromhex(podzial[2])
                oczekiwany_skrot = bytes.fromhex(podzial[3])
                skrot = hashlib.pbkdf2_hmac('sha256', haslo.encode('utf-8'), sol, iteracje)
                return hmac.compare_digest(skrot, oczekiwany_skrot)
    return False

print("anna, Kasztan-2026:", weryfikuj('anna', 'Kasztan-2026'))
print("anna, kasztan-2026:", weryfikuj('anna', 'kasztan-2026'))
print("piotr, Żółw na łące:", weryfikuj('piotr', 'Żółw na łące'))
print("kasia, Kasztan-2026:", weryfikuj('kasia', 'Kasztan-2026'))

def dodaj(login, haslo):
    sol = secrets.token_bytes(16)
    iteracje = 600000
    wyliczony_skrot = hashlib.pbkdf2_hmac('sha256', haslo.encode('utf-8'), sol, iteracje)
    return login, iteracje, sol.hex(), wyliczony_skrot.hex()

test1 = dodaj("test1", "abcdefgh")
test2 = dodaj("test2", "abcdefgh")

print(f"test1: sol: {test1[2]} skrot: {test1[3][:20]}")
print(f"test2: sól: {test2[2]} skrot: {test2[3][:20]}")
print(hashlib.pbkdf2_hmac('sha256', b"abcdefgh", bytes.fromhex(test1[2]), test1[1]).hex() == test1[3])
print(hashlib.pbkdf2_hmac('sha256', b"abcdefgh", bytes.fromhex(test2[2]), test2[1]).hex() == test2[3])