def is_film_exist(movie, films_list): #можно короче: if movie in films_list
    #for i in films_list:
        #if i == movie:
           # return True
    if movie in films_list:
        return True
    return False

films = [
    'Крепкий орешек', 'Назад в будущее', 'Такси',
    'Богемская рапсодия', 'Город грехов', 'Матрица'
]
my_list = []

while True:
    print('Ваш текущий список фильмов:', my_list)
    new_movie = input('Название фильма: ')
    if is_film_exist(new_movie, films):
        print('Команды: добавить, удалить, вставить.')
        command = input('Введите команду: ')
        if command == 'добавить':
            my_list.append(new_movie)
        elif command == 'удалить':
            if is_film_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print('Такого фильма нет в нашем рейтинге.')
        elif command == 'вставить':
            index = int(input('На какое место? '))
            my_list.insert(index - 1, new_movie)
    else:
        print('Такого фильма нет на сайте')



