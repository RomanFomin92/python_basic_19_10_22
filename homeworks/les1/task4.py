# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = abs(int(input("Введите число:\n")))
max = n % 10
n = n // 10
while n > 0:
    if n % 10 > max:
        max = n % 10
    n = n // 10
print(max)
