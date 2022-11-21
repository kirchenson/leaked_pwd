import requests
import hashlib


def hash_func(w):
    encoded_str = w.encode()
    hash_obj = hashlib.sha1(encoded_str)
    hex_value = hash_obj.hexdigest()
    return hex_value


def leaked_or_not(w):
    BASE_URL = f'https://api.pwnedpasswords.com/range/{hash_func(w)[0:5]}'
    ost = hash_func(w)[5:]
    response = requests.get(f"{BASE_URL}")
    a = str(response.content)
    a = a[1:].split("\\r\\")

    for i in range(len(a)):
        x = a[i][1:36]
        ost = ost.upper()
        if x == ost:
            return f'{w} : LEAKED!'
    return f'{w} : NOT LEAKED!'


f = open('text.txt')
s = f.read().split('\n')
for i in s:
    print(leaked_or_not(i))
