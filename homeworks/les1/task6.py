# Практическое задание 6

user_a = int(input("Введите результаты пробежки первого дня в км\n"))
user_b = int(input("Введите до скольки вы хотите увеличить дальность пробежки в км\n"))
result_day = 1
while  user_b - user_a >= 0:
       user_a *= 1.1
       result_day += 1

print(f"Вы достигнете требуемых показателей на %.d день" % result_day)