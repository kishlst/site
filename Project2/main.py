'''
Напишите метод, который принимает на вход массив последовательных (возрастающих) букв и возвращает недостающую букву в массиве.

Вы всегда получите действительный массив. И всегда будет отсутствовать ровно одна буква. Длина массива всегда будет не менее 2.
Массив всегда будет содержать буквы только в одном регистре.

Пример:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# функция может принимать много значений, аргументов.
def find_missing_letter(chars):

    charsZero = chars[0]

    for i in range(len(chars)):
        if charsZero != alphabet[i]:
            print(alphabet[i])

    for i in range(len(chars)):
        chars[i] = chars[i].lower()

    voli = alphabet[:len(chars) + 1]

    for i in range(len(chars)):
        if voli[i] != chars[i]:
            print(alphabet[i])


find_missing_letter(['O','Q','R','S'])