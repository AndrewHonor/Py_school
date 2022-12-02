import math


def true_Namber(text_print):
    while True:
        print(text_print, end='')
        true_var = input()
        if true_var.isdigit(): return true_var


def aple_task():
    text01 = 'Скільки школярів? '
    text02 = 'А скільки яблук є? '
    miniPeople = int(true_Namber(text01))
    apples = int(true_Namber(text02))
    apples_on_miniPeople = apples // miniPeople
    if apples % miniPeople == 0:
        print(f'Дітям достанеться по {apples_on_miniPeople}',
              'яблуку.' if apples_on_miniPeople == 1 else (
                  'яблук.' if 4 < apples_on_miniPeople < 21 or apples_on_miniPeople % 10 == 0 or
                              str(apples_on_miniPeople)[
                                  -1] == '1' else 'яблука.'))
    else:
        print(f'Дітям достанеться по {apples_on_miniPeople}',
              'яблуку,' if apples_on_miniPeople == 1 else (
                  'яблук,' if 4 < apples_on_miniPeople < 21 or apples_on_miniPeople % 10 == 0 or
                              str(apples_on_miniPeople)[
                                  -1] == '1' else 'яблука,'), f'і {apples % miniPeople} залишиться в кошику.')


def school_desks():
    miniPeople_classrooms = ()
    while len(miniPeople_classrooms) < 3:
        miniPeople_classrooms = ()
        miniPeople_classrooms = input("Введіть скільки дітей начається в трьох класах математики через пробіл? ").split(
            " ")
        miniPeople_classrooms = ' '.join(miniPeople_classrooms).split()
    classroom = ('першого', 'другого', 'третього')
    # print(miniPeople_classrooms)
    school_desks_classrooms = []
    print("Кількість парт яку потрібно закупити для ", end='')
    for x in range(3):
        school_desks_classrooms.append(math.ceil(int(miniPeople_classrooms[x]) / 2))
        print(f'{classroom[x]} класу - {school_desks_classrooms[x]} шт.')


def revers_var():
    text01 = 'Введіть багатозначне число для проведення реверсу: '
    var_original = int(true_Namber(text01))
    var_revers = 0
    while var_original > 0:
        count = var_original % 10
        var_original = var_original // 10
        var_revers = var_revers * 10
        var_revers = var_revers + count
    print(f'Реверсне число: {var_revers}')


def oclock_t():
    text01 = 'Введіть кількість секунд які пройшли з початку дня: '
    sec_tim = int(true_Namber(text01))
    hour = sec_tim // 3600
    sec_tim = sec_tim % 3600
    minutes = sec_tim // 60
    sec_tim = sec_tim % 60
    print(f'Пройшло {hour}:{minutes}:{sec_tim} часу')


# true_Namber()
aple_task()
print()
school_desks()
print()
revers_var()
print()
oclock_t()
