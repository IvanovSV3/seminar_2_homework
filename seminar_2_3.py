# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('ведите целое чилсо N - '))
print('принято чило N =', number)
spisok = []
for i in range(- number, number+1):
    # print(i)
    spisok.append(i)
print(spisok)

file = open("File.txt","r")
multi = 1
list_str = file.readlines()
print(list_str)

list_num = list(map(str.strip,list_str))
print(list_num)

for i in list_num:
    multi = multi * spisok[int(i)]
    print('spisok', multi)
print("произведение = ", multi)