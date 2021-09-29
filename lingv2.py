#замена двоеточий на точку с запятой

my_string = []
count = 0

print('Введите строку:', end = ' ')
string = input()
my_string = list(string)
my_string2 = ''

sym1 = str(input('Что нужно заменить? '))
sym2 = str(input('На что нужно заменить? '))

for j in my_string:
    if j != sym1:
        my_string2 += j
    else:
        my_string2 += sym2
        count += 1

print(my_string2)
print('К-во замен:', count)