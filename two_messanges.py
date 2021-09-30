first = input('1я строка: ')
second = input('2я строка: ')

first_count = first.count('!') + first.count('?')
second_count = second.count('!') + second.count('?')

if first_count > second_count:
    print(first, second)
elif second_count > first_count:
    print(second, first)
else:
    print('Ой')