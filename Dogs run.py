#Поменять местами максимальное и минимальное числа

def turn(list, index, num):
    del list[index]
    list.insert(index, num)
    return list

nums_list = []
num_list2 = []
N = int(input('Кол-во собак: '))

for _ in range(N):
    num = int(input('Номер собаки: '))
    nums_list.append(num)
max_num = nums_list[0]
min_num = nums_list[0]
max_index = 0
min_index = 0

count_index = -1
for i in nums_list:
    count_index += 1
    if max_num < i:
        max_num = i
        max_index = count_index
    if min_num > i:
        min_num = i
        min_index = count_index

print('Максимальное число в списке:', max_num, max_index)
print('Минимальное число в списке:', min_num, min_index)
print(nums_list)

turn(nums_list, max_index, min_num)
nums_list2 = turn(nums_list, max_index, min_num)
turn(nums_list, min_index, max_num)
nums_list2 = turn(nums_list, min_index, max_num)
print(nums_list2)