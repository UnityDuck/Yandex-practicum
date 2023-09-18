# Мухи отдельно, котлеты отдельно
# Вернёмся в магазин, хозяин которого уже привык полагаться на всемогущую автоматизацию.

# Помогите ему разобраться с одной проблемой. Далее его история: «Пару дней назад я купил две партии котлет и по случайности высыпал их на один прилавок. Общий вес котлет составил N килограмм, а ценник — M рублей за килограмм.
# Сегодня я обнаружил, что накладные на эти виды котлет потерялись, но я помню, что первый вид котлет стоил K1 рублей за килограмм, а второй — K2.

# Помогите мне вспомнить вес каждой партии котлет, чтобы поставить их на учёт.

# Формат ввода:
# В первой строке записано натуральное число N
# Во второй строке — натуральное число M
# В третьей строке — натуральное число K1 
# В четвёртой строке — натуральное число K2
# Причём доподлинно известно, что второй вид котлет стоит меньше, чем первый.

# Формат вывода:
# Два натуральных числа, записанных через пробел — вес обеих партий котлет.

n = input("")
m = input("")
K1 = input("")
K2 = input("")

first = int(n) * int(K1)
second = int(n) * int(m)
third = int(first) - int(second)
changer = int(K1) - int(K2)

x = int(third) // int(changer)
y = int(n) - int(x)

print(y, x)