# 1) Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе

type_list = [1, 2/3, complex(4, 5), "шесть", True, [7,8], {"девять": "десять", "одинадцать": "двенадцать"},(13,14), set("двенадцать"), frozenset('abrakadabra')
, (bytes('text', encoding = 'utf-8')), (bytearray(b"some text")), (type(None))]
print(type_list)
for i in range (len(type_list)) :
    print(f"Тип переменной в списке: {type(type_list[i])}")