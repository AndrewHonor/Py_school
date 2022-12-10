from random import randint


def task_1():
    my_list = [randint(1, 120) for _ in range(100)]
    return [x for x in my_list if x > 100]


def task_2():
    my_list = [randint(1, 120) for _ in range(100)]
    my_results = [x for x in my_list if x > 100]
    return my_results


def task_3():
    my_list = [randint(1, 120) for _ in range(randint(1, 5))]
    if len(my_list) > 2:
        my_list.append(my_list[-1] + my_list[-2])
    else:
        my_list.append(0)
    return my_list


def task_4():
    pass


def task_5():
    pass


def task_6():
    pass
