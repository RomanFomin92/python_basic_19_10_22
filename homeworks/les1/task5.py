# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
# — издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
# выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
# расчете на одного сотрудника.

profit = float(input("Введите выручку:\n"))
costs = float(input("Введите издержки:\n"))

if profit > costs:
    print(f"Рентабельность компании составляет:  { profit / costs:.2f}")
    workers = int(input("Введите количество сотрудниковЖ:\n"))
    print(f"прибыль в расчете на одного сторудника сотавила {(profit - costs)  / workers:.2f}")
elif profit == costs:
    print("Нулевая доходность")
else:
    print(f"Фирма работает в убыток, сумма убытка: {profit - costs:.2f}")
