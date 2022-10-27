# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {название: компьютер, цена: 20000, количество: 5, eд: шт.}),
# (2, {название: принтер, цена: 6000, количество: 2, eд: шт.}),
# (3, {название: сканер, цена: 2000, количество: 7, eд: шт.})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# название: [компьютер, принтер, сканер],
# цена: [20000, 6000, 2000],
# количество: [5, 2, 7],
# ед: [шт.]
# }

shop_id_dict = [
(1, {'HP': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'HP': 'принтер', 'цена' : 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'HP': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
(4, {'Lenovo': 'компьютер', 'цена': 25000, 'количество': 3, 'eд': 'шт.'}),
(5, {'Lenovo': 'принтер', 'цена': 7000, 'количество': 4, 'eд': 'шт.'}),
(6, {'Lenovo': 'сканер', 'цена': 3000, 'количество': 9, 'eд': 'шт.'}),
(7, {'ASUS': 'компьютер', 'цена': 27000, 'количество':75, 'eд': 'шт.'}),
(8, {'ASUS': 'принтер', 'цена': 6700, 'количество': 4, 'eд': 'шт.'}),
(9, {'ASUS': 'сканер', 'цена': 2700, 'количество': 70, 'eд': 'шт.'}),
(10, {'Samsung': 'компьютер', 'цена': 35000, 'количество': 37, 'eд': 'шт.'}),
(11, {'Samsung': 'принтер', 'цена': 9000, 'количество': 46, 'eд': 'шт.'}),
(12, {'Samsung': 'сканер', 'цена': 6000, 'количество': 97, 'eд': 'шт.'}),
]
print(shop_id_dict[1:5])
