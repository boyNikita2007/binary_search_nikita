# напишите программу для бинарного поиска загаданного числа

user_num=int(input('Введите целове число: '))
def binary_search(min_num,max_num):
    center=(min_num + max_num)//2
    while True:
        print(f'Ваше число {center}?')
        check=input('Если больше >, если меньше <, если равно = ')
        if check=='>':
            min_num=center
            center=(min_num + max_num)//2
        elif check=='<':
            max_num=center
            center=(min_num+max_num)//2
        elif check=='=':
            print('Я угадал')
            break
        else:
            print(' не знаю ваше число.')
binary_search(int(input('Введите минимальное число: ')),int(input('Введите максимальное число: ')))
