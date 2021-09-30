pack = []
decode = []
bad_packs = 0
N = int(input('К-во пакетов: '))

for i in range(N):
    print('Пакет номер', i + 1)
    for j in range(4):
        print((j + 1), 'бит:', end = ' ')
        sym = int(input())
        pack.append(sym)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете')
        bad_packs += 1
    pack = []

print('Полученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', bad_packs)

