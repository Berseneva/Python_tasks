fruits = [['яблоки', 50], ['апельсины', 190], ['груши', 100], ['нектарины', 200], ['бананы', 77]]
new_fruit = []
print('Текущий ассортимент:', fruits)

fruit = input('Новый фрукт: ')
price = int(input('Цена: '))
new_fruit.append(fruit)
new_fruit.append(price)

fruits.append(new_fruit)

print('Новый ассортимент:', fruits)

for i in fruits:
    i[1] *= 1.08
    i[1] = float('{:.2f}'.format(i[1])) #сокращение float  2х знаков после запятой

print()
print('Новый ассортимент с увел. ценой:', fruits)