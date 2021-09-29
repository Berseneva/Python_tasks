my_list = []
count_num = 0

print('Введите строку:', end = ' ')
string = input()
my_list = list(string)

sym = int(input('Номер символа: '))
this_sym = ''

for j in my_list:
    count_num += 1
    if count_num == sym:
        this_sym = j
        left_sym = my_list[count_num - 2]
        right_sym = my_list[count_num]

print('Символ слева:', left_sym)
print('Символ справа:', right_sym)

if this_sym == left_sym and this_sym == right_sym:
    print('По соседству есть два таких же символа')
elif this_sym == left_sym or this_sym == right_sym:
    print('По соседству есть один такой же символ')
else:
    print('Рядом нет таких же символов')



