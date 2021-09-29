def one():
  count = 0
  for i in num:
    if i.isdigit() == True:
      i = int(i)
      count += i
    else:
      pass
  print(count)
  print()

def two():
  count = 0 
  for i in num:
    if i.isdigit() == True:
      i = int(i)
      if count < i:
        count = i
    else:
      pass
  print(count)
  print()

def three():
  count = int(num)
  for i in num:
    if i.isdigit() == True:
      i = int(i)
      if count > int(i):
        count = i
    else:
      pass
  print(count)
  print()

try:
  while True:
    num = input('Введите число: ')
    act = int(input('Что делаем с числом: 1 - суммируем его цифры, 2 - находим максимальную цифру, 3 - находим минимальную цифру? '))
    if act == 1:
      one()
    elif act == 2:
      two()
    elif act == 3:
      three()
    else:
      print('Для выбора действия введите число от 1 до 3')
      print()
except ValueError:
  print('Ошибка ввода')
