words = []
counts = [0, 0, 0]
count_index = -1

print('Введите строку:', end = ' ')
my_list = input().split(' ')

for k in range(3):
    print('Введите', k + 1, 'слово:', end = ' ')
    word = input()
    words.append(word)

for i in words:
    count_index += 1
    for j in my_list:
        if i == j:
            counts[count_index] += 1

print()
print('Подсчет слов в тексте')
for k in range(3):
    print(words[k] + ':', counts[k])