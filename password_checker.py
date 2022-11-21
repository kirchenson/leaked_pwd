import requests
import hashlib

#создаем функцию для хеширования пароля
def hash_func(w):
    encoded_str = w.encode()
    hash_obj = hashlib.sha1(encoded_str)
    hex_value = hash_obj.hexdigest()
    return hex_value

#
def leaked_or_not(w):
    #в url пишем путь до ресурса поиска хеша в утёкших базах данных и 5 первых символов хеша обрабатываемого слова
    BASE_URL = f'https://api.pwnedpasswords.com/range/{hash_func(w)[0:5]}'
    ost = hash_func(w)[5:]#весь остальной хеш сохраняем и будем искать его на результирующей странице
    response = requests.get(f"{BASE_URL}")#get-запрос до ресурса
    a = str(response.content)
    a = a[1:].split("\\r\\")#из результата делаем список с хешами

    for i in range(len(a)):#перебор на совпадение хеша из результата и из программы
        x = a[i][1:36] #убираем лишние символы из результата
        if x == ost.upper():#сравниваем результат с остатком хеша обрабатываемого слова
            return f'{w} : LEAKED!'
    return f'{w} : NOT LEAKED!'


f = open('text.txt')
s = f.read().split('\n')
for i in s:
    print(leaked_or_not(i))
