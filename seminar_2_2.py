# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number = int(input('ведите целое чилсо N - '))
print('принято чило N =', number)
multipli = []
multipli_number = 1
number_1 = range(1,number+1)
for i in number_1:    
    multipli_number = multipli_number * i
    multipli.append(multipli_number)
print(multipli)