my_list = []
num = 1
N = int(input('Введите кол-во человек: '))
K = int(input('Введите кол-во человек в команде: '))

if N % K == 0:
    for _ in range(N//K):
        my_list.append(list(range(num, num + K)))
        num += K
    print(my_list)
else:
    print('Кол-во человек не делится поровну')