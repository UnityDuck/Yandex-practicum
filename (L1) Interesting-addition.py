# Интересное сложение
# Один малыш из детского сада услышал от старшей сестры о некоем действии с числами — сложении.
# И как это часто бывает — он не до конца разобрался, как работает сложение. Например, не совсем понял, как произвести перенос разряда.
# Теперь он хочет научить сложению остальных ребят и просит написать программу, которая поможет ему в качестве наглядного материала.

# Формат ввода
# В первой и второй строках записаны натуральные числа меньше 1000.

# Формат вывода
# Одно число — результат сложения введённых чисел без учёта переносов.

number = list(map(int, input().rjust(3, '0')))
number2 = list(map(int, input().rjust(3, '0')))
number3 = str((number[0] + number2[0]) % 10)
number4 = str((number[1] + number2[1]) % 10)
number5 = str((number[2] + number2[2]) % 10)
print((number3 + number4 + number5).lstrip('0'))