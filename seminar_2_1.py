# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
real_number = input('вход вещественное число  ')
# print(type(real_number))
list_number = list(real_number)
# print("лист цифр", list_number)
# amount_number = len(list_number)
# print("кол цифр", amount_number)
# print("кол цифр", type(amount_number))
number = range(10)
number = list(number)
number = str(number)
# print("цифр", number)
sum = 0
for i in list_number:
    # print("I= ",type(i),i)
    for j in number:
        # print("j= ", j)
        # print(type(j))
        if i == j:
            k = int(i)
            # print('k= ', k)
            sum = sum + k
            # print('sum= ', sum)
print('сумма= ',sum)
