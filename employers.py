salary_list = []
N = int(input('Кол-во сотрудников: '))

for i in range(N):
    print('Зарплата', i + 1, 'сотрудника, тыс. руб.:', end = ' ')
    salary = int(input())
    if salary != 0:
        salary_list.append(salary)

print('Осталось сотрудников:', len(salary_list))
print('Зарплаты:', salary_list, 'тыс. руб.')
print('Максимальная зарплата:', max(salary_list))
print('Минимальная зарплата:', min(salary_list))