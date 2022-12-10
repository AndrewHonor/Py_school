from random import randint


def task_1():
    my_list = [randint(1, 120) for _ in range(100)]
    return print([x for x in my_list if x > 100])


def task_2():
    my_list = [randint(1, 120) for _ in range(100)]
    my_results = [x for x in my_list if x > 100]
    return print(my_results)


def task_3():
    my_list = [randint(1, 120) for _ in range(randint(1, 5))]
    if len(my_list) > 2:
        my_list.append(my_list[-1] + my_list[-2])
    else:
        my_list.append(0)
    return print(my_list)


def task_4():
    my_list = [randint(10, 99) for _ in range(randint(5, 25))]
    k_id_ml = randint(0, len(my_list) - 1)
    print(k_id_ml)
    count = ' '
    print('Дано список чисел: \t', *my_list[:k_id_ml], f'[{my_list[k_id_ml]}]', *my_list[k_id_ml + 1:])
    print(f'Дано індекс K: {k_id_ml}\t {count * k_id_ml * 3} ^  -- Ось він')
    print(f'Ми його обережно забрали [[{my_list[k_id_ml]}]]')
    for x in range(len(my_list)):
        if x > k_id_ml:
            my_list[x - 1] = my_list[x]
    my_list.pop()  ###
    print()
    print(f'Тепер список без K:\t', *my_list)


def task_5():
    my_list = [randint(10, 99) for _ in range(randint(5, 25))]
    k_id_ml = randint(0, len(my_list) - 1)
    var_num = randint(10, 99)
    count = '_'
    print('Дано список чисел: \t', *my_list)
    print(
        f'Ось в це місце: ___{count * k_id_ml * 3} ^ {count * (len(my_list) * 3 - k_id_ml * 3 - 2)}За індексом [{k_id_ml}]')
    print(f'Вставити ось це: {var_num} число')
    my_list.append(0)
    for x in reversed(range(len(my_list))):
        if x > k_id_ml:
            my_list[x] = my_list[x - 1]
        elif x == k_id_ml:
            my_list[x] = var_num
    print(f'Тепер список:\t\t', *my_list)


def task_6():
    my_list_1, my_list_2 = [randint(10, 99) for _ in range(50)], [randint(10, 99) for _ in range(50)]
    print('Список_1', my_list_1, 'Унікальних значень: ', len(set(my_list_1)), 'Список_2', my_list_2,
          'Унікальних значень: ', len(set(my_list_2)), sep='\n')
    print()
