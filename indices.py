N = int(input('Кол-во чисел в списке: '))
my_list = []

for i in range(N):
    print('Введите ', i + 1, 'число:', end = ' ')
    a =int(input())
    my_list.append(a)

K = int(input('Введите делитель: '))

summ = 0
count_index = -1
for i in my_list:
    count_index += 1
    if i % K == 0:
      print('Индекс числа', str(i) + ':', count_index)
      summ += count_index
print('Сумма индексов:', summ)