# 3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

## через list
# month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
#
# user_month = int(input('Введите порядковый номер месяца в году (от 1 до 12): '))
# if user_month in range(1, 13):
#     for i, el in enumerate(month_list):
#         if user_month in el[1:4]:
#             print(f'Введенный номер месяца относится к сезону {el[0]}')
#             break
# else:
#     print('Введен некорректный номер месяца!')
#
## через dict.
month_dict = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
user_month = int(input('Введите порядковый номер месяца в году (от 1 до 12): '))
if user_month in range(1, 13):
    for k in month_dict.keys():
        if user_month in month_dict[k]:
            print(f'Введенный номер месяца относится к сезону {k}')
else:
    print('Введен некорректный номер месяца!')