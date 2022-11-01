# Практиеское задание 4

n = abs(int(input("Введите число:\n")))
max = n % 10
n = n // 10
while n > 0:
    if n % 10 > max:
        max = n % 10
    n = n // 10
print(max)
