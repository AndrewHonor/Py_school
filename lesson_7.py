from random import randint


def task_3():
    print(">>> task_3 - об'єднати два списки в один, почергово")
    my_list_1 = [randint(1, 120) for _ in range(20)]
    my_list_2 = [randint(1, 120) for _ in range(20)]
    my_result = [0 for _ in range(40)]
    for x in range(20):
        my_result[x * 2 + 1] = my_list_1[x]
    print(f"my_list_1 = {my_list_1}\nmy_list_2 = {my_list_2}\nmy_result = {my_result}")
    for x in range(20):
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


def task_6():
    print(">>> task_6 - вивести суму чисел у наданій строці")
    st_1 = "43 больше чем 34, но меньше чем 56"
    print(st_1)
    st_2 = ''
    cash = '1234567890 '
    for x in st_1:
        if x in cash:
            st_2 += x
    mas_1 = [int(x) for x in st_2.split()]
    print(sum(mas_1))
    print()


def task_7():
    print(">>> task_7 - вивести зріз списку по заданим критеріям")
    my_str = "My long string"
    l_limit = "o"
    r_limit = "g"
    sub_str = ''
    my_str = my_str[:my_str.index(l_limit):-1]
    sub_str = my_str[:my_str.index(r_limit):-1]
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


def task_9():
    pass


def task_10():
    pass


def task_11():
    pass


def task_12():
    pass


# task_3()
# task_4()
# task_5()
# task_6()
# task_7()
task_8()
# task_9()
# task_10()
# task_11()
# task_12()
