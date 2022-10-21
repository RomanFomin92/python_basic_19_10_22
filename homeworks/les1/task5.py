# Практическое задание 5

profit = float(input("Введите выручку:\n"))
costs = float(input("Введите издержки:\n"))

if profit > costs:
    print(f"Прибыль компании составила { profit / costs:.2f}")
    workers = int(input("Введите количество сотрудниковЖ:\n"))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Нулевая доходность")
else:
    print(f"Фирма работает в убыток, сумма убытка: {profit - costs:.2f}")
