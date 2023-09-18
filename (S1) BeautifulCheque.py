# Украшение чека
# Давайте приведём в порядок чек, который печатали ранее.
# Все строки должны быть длиной в 35 символов.

# Формат ввода:
# Название товара;
# цена товара;
# вес товара;
# количество денег у пользователя.

# Формат вывода:
# Красивый чек в формате:

# ================Чек================
# Товар:                    <продукт>
# Цена:     <число>кг * <число>руб/кг
# Итого:                   <число>руб
# Внесено:                 <число>руб
# Сдача:                   <число>руб
# ===================================

# Примечание:
# В данный момент примеры ниже визуализируются неправильно.

product = input("")
cost = input("")
weight = input("")
money = input("")

itogo = int(cost) * int(weight)
change = int(money) - int(itogo)
change = str(change)

lenx = len(product)
lenb = len(cost)
lenv = len(weight)
lenc = len(money)
lenchange = len(change)

moneys = int(cost) * int(weight)
moneys = str(moneys)
lenz = len(moneys)

probel = 35 - int(lenx) - 8
probel4ik = " "
probel4ik2 = str(probel4ik) * int(probel)

# Да, названия переменных придумывал я.