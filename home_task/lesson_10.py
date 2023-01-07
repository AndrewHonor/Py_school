import random
import string


def gen_lst(x):
    rand_string = []
    if x == 1:
        letters = string.ascii_lowercase
        rand_string = [''.join(random.choice(letters) for _ in range(3)) for _ in range(1, random.randint(3, 20))]
        print("Згенерований список:", rand_string)
    if x == 2:
        tick = random.randint(10, 20)
        while tick > 0:
            tick = tick - 1
            coin = random.randint(1, 2)
            if coin == 1:
                letters = string.ascii_lowercase
                rand_string.append(''.join(random.choice(letters) for _ in range(3)))
            if coin == 2:
                rand_string.append(random.randint(100, 999))
        print("Згенерований список:", rand_string)

    return rand_string


def fun_revers_lst_01(lst):
    ret_lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            ret_lst.append(lst[i])
        else:
            ret_lst.append(''.join(reversed(lst[i])))

    return ret_lst


def fun_pars_lst_first_a(lst):
    ret_lst = []


    return ret_lst


def fun_pars_lst_in_a(lst):
    pass


def fun_pars_lst_str(lst):
    pass


def fun_transformation_str_lst_uniq(lst):
    pass


print(fun_revers_lst_01(gen_lst(1)))
