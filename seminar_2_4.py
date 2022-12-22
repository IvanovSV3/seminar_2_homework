# Реализуйте алгоритм перемешивания списка.
spisok = []
for i in range(10):
    spisok.append(i)
print('исходный = ',spisok)

k_1 = int(input('ведите коэ. перемешивания от 1 до 9 = '))
n = 1.123249877655456782746474747848488484884984/k_1
b = 1.232238420438213823412034820598340689580385/n
b = str(b)
# print(type(b))
# print(b)
b_1 = tuple(b)
# print(b_1)
b_2 = list(b_1)
# print(b_2)
b_2.remove(".")
# print(b_2)
for i in b_2:
    i_ = int(i)
    for j in range(10):
        r = spisok[j]
        spisok[j] = spisok[i_]
        spisok[i_] = r
        # print(r)

print('перемешаный = ',spisok)