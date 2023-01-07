from random import randint


def task_3():
    print(">>> task_3 - об'єднати два списки в один, почергово")
    my_list_1 = [randint(1, 120) for _ in range(10)]
    my_list_2 = [randint(1, 120) for _ in range(10)]
    my_result = [0 for _ in range(20)]
    for x in range(10):
        my_result[x * 2 + 1] = my_list_1[x]
    print(f"my_list_1 = {my_list_1}\nmy_list_2 = {my_list_2}\nmy_result = {my_result}")
    for x in range(10):
        my_result[x * 2] = my_list_2[x]
    print(f"my_result = {my_result}")
    print()


def task_4():
    print(">>> tast_4 - створити новий список з існуючого, із зсувом ліворуч на один елемент зрізом")
    my_list = [randint(1, 120) for _ in range(20)]
    new_list = my_list.copy()
    new_list = new_list[1:] + new_list[:1]
    print(f"my_list =\t{my_list}\nnew_list =\t{new_list}")
    print()


def task_5():
    print(">>> tast_5 - створити новий список з існуючого, із зсувом ліворуч на один елемент через метод pop")
    my_list = [randint(1, 120) for _ in range(20)]
    print(f"my_list =\t{my_list}")
    my_list.append(my_list.pop(0))
    print(f"my_list =\t{my_list}")
    print()


def task_6():
    print(">>> task_6 - вивести суму чисел у наданій строці")
    st_1 = "'43 больше чем 34, но меньше чем 56'"
    print(st_1)
    st_2 = ''
    cash = '1234567890 '
    for x in st_1:
        if x in cash:
            st_2 += x
    mas_1 = sum([int(x) for x in st_2.split()])
    print(mas_1)
    print()


def task_7():
    print(">>> task_7 - вивести зріз списку по заданим критеріям")
    my_str = "My long string"
    l_limit = "o"
    r_limit = "g"
    sub_str = ''
    my_str = my_str[:my_str.index('o'):-1]
    sub_str = my_str[:my_str.index('g'):-1]
    print(sub_str)
    print()


def task_8():
    print(">>> task_8 - вивести масив створений із розбитої строки по два елементи")
    cash = 'qwertyuiopasdfghjklzxcvbnm'
    my_str = ''.join([cash[randint(0, len(cash) - 1)] for _ in range(randint(10, 20))])
    print(my_str)
    if len(my_str) % 2 == 0:
        my_mas = [my_str[i - 2:i] for i in range(2, len(my_str) + 1, 2)]
    else:
        my_mas = [my_str[i:i + 2] for i in range(0, len(my_str), 2)]
        my_mas[-1] = my_mas[-1] + '_'
    print(*my_mas)
    print()


def task_9():
    coin = 0
    max_list = []
    print(">>> task_9 - вивести кількість чисел більші суми сусідів")
    my_list = [randint(1, 99) for _ in range(randint(10, 20))]
    print("my_list =", *my_list)
    for x in range(1, len(my_list) - 1):
        if my_list[x] > my_list[x - 1] + my_list[x + 1]:
            max_list.append(my_list[x])
            coin += 1
    print('більші = ', *max_list)
    print("Сума чисел = ", coin)
    print()


def task_10():
    print(">>> task_10 Вивести вибірку з масиву по 'строковому' типу")
    my_list = []
    my_str_list = []
    for _ in range(randint(10, 20)):
        intOrStr = randint(1, 99)
        my_list.append(str(randint(1, 99)) if intOrStr > 50 else randint(1, 99))
    print("my_list =", my_list)
    for x in my_list:
        if isinstance(x, str):
            my_str_list.append(x)
    print("my_str_list = ", my_str_list)
    print()


def task_11():
    print(">>> task_11 Вивести вибірку унікальних символів")
    cash = 'qwertyuiopasdfghjklzxcvbnm'
    my_str = ''
    for x in range(randint(20, 50)):
        my_str += cash[randint(1, len(cash) - 1)]
    print("Рандомна строка =", my_str)
    print("Str унікальних едементів = ", *set(my_str), sep='')
    print()


def task_12():
    print(">>> task_12 Вивести вибірку унікальних символів з двох рядків")
    cash = 'qwertyuiopasdfghjklzxcvbnm'
    my_str_1 = ''.join([cash[randint(1, len(cash) - 1)] for _ in range(randint(20, 50))])
    my_str_2 = ''.join([cash[randint(1, len(cash) - 1)] for _ in range(randint(20, 50))])
    print(f'my_str_1 - {my_str_1}', f'my_str_2 - {my_str_2}', sep='\n')
    print('unique_sign = ', *{*my_str_1, *my_str_2}, sep='')
    print()


def task_13():
    print(">>>task_13 Вивести список унікальних елементів наявних в двох рядках")
    cash = 'qwertyuiopasdfghjklzxcvbnm'
    my_str_1 = ''.join([cash[randint(1, len(cash) - 1)] for _ in range(randint(10, 20))])
    my_str_2 = ''.join([cash[randint(1, len(cash) - 1)] for _ in range(randint(10, 20))])
    uniq_sign = ''
    print(f'my_str_1 - {my_str_1}', f'my_str_2 - {my_str_2}', sep='\n')
    for x in my_str_1:
        if x in my_str_2:
            uniq_sign += x
    print(uniq_sign)
    print()


task_3()
task_4()
task_5()
task_6()
task_7()
task_8()
task_9()
task_10()
task_11()
task_12()
task_13()
