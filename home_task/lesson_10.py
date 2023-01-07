import random
import string


def gen_lst(x):
    '''
    ГЕНЕРАТОР СПИСКІВ
    :param x: 1- визначає генерувати тільки строки
              2- визначає генерувати строки та числа в випадкомову порядку
    :return: повертає згенерований список
    '''
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


def gen_str():
    '''
    ГЕНЕРАТОР СТРОК
    :return: повертає згенеровану строку випадкової [15-44] довжини
    '''
    letters = string.ascii_lowercase
    rt_str = ''.join(random.choice(letters) for _ in range(1, random.randint(15, 45)))
    print("Згенерована строка:", rt_str)
    return rt_str


def fun_revers_lst_01(lst):
    '''
    Ф-ція реверсить кожен парний str(елемент) списку
    :param lst: приймає список str(елементів)
    :return: повертає видозмінений список
    '''
    ret_lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            ret_lst.append(lst[i])
        else:
            ret_lst.append(''.join(reversed(lst[i])))

    return ret_lst


def fun_pars_lst_first_a(lst):
    '''
    Ф-ція створює новий список з str(елементів) які мають перший індекс елементу "a"
    :param lst: приймає список str(елементів)
    :return: повертає видозмінений список
    '''
    ret_lst = []
    for element in lst:
        if 'a' in element[0]:
            ret_lst.append(element)
    if len(ret_lst) == 0:
        ret_lst = "У списку елементів не має входжень [0]-індекс яких є 'а'"
        return ret_lst
    return ret_lst


def fun_pars_lst_in_a(lst):
    '''
    Ф-ція створює новий список з str(елементів) які мають смвол "a"
    :param lst: приймає список str(елементів)
    :return: повертає видозмінений список
    '''
    ret_lst = []
    for element in lst:
        if 'a' in element:
            ret_lst.append(element)
    if len(ret_lst) == 0:
        ret_lst = "У списку елементів не має входжень з будь яким індексом яких є 'а'"
        return ret_lst
    return ret_lst


def fun_pars_lst_str(lst):
    '''
    Ф-ція створює новий список з елементів які є str-типу
    :param lst: приймає список str(елементів) та чисел
    :return: повертає видозмінену строку
    '''
    ret_lst = []
    for element in lst:
        if isinstance(element, str):
            ret_lst.append(element)
    if len(ret_lst) == 0:
        ret_lst = "У списку елементів не має входжень строкового типу"
        return ret_lst
    return ret_lst


def fun_transformation_str_lst_uniq(lst):
    '''
    Ф-ція створює новий список з унікальних елементів які зустрічаються лише раз
    :param lst: приймає список str(елементів)
    :return: повертає видозмінену строку
    '''
    rt_lst = []
    for i in lst:
        if lst.count(i) == 1:
            rt_lst.append(i)
    return rt_lst


def fun_transformation_dblw_str_lst(lst_01, lst_02):
    '''
    Ф-ція створює новий список з елементів які є в обох строках хоча б один раз
    :param lst_01, lst_02: приймає список str(елементів)
    :return: повертає видозмінену строку
    '''
    cash_01 = set(lst_01)
    cash_02 = set(lst_02)
    rt_lst = [x for x in cash_01 if x in cash_02]
    return rt_lst


def fun_transformation_dblw_str_lst_uniq(lst_01, lst_02):
    '''
    Ф-ція створює новий список з елементів які є в обох строках лише один раз
    :param lst_01, lst_02: приймає список str(елементів)
    :return: повертає видозмінену строку
    '''
    rt_lst = []
    cach = [lst_01, lst_02]
    for i in lst_01:
        if lst_01.count(i) == 1:
            if sum(map(lambda x: 1 if i in x else 0, cach)) == 2:
                rt_lst.append(i)
    return rt_lst


def fun_gen_e_mail(name, domains):
    '''
    ГЕНЕРАТОР ПОЧТОВИХ АДРЕС
    :param name: приймає список імен
    :param domains: приймає список доменних імен
    :return: повертає список почтових адрес
    '''
    gen_e_mail = []
    for name in name:
        for i in range(100,1000):
            for domain in domains:
                gen_e_mail.append(name+"."+str(i)+"@"+domain)
    return gen_e_mail

