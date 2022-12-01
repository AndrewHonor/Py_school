def aple_task():
    miniPeople = int(input('Скільки школярів? '))
    apples = int(input('А скільки яблук є? '))
    apples_on_miniPeople = apples // miniPeople
    if apples % miniPeople == 0:
        print(f'Дітям достанеться по {apples_on_miniPeople}',
              'яблуку.' if apples_on_miniPeople == 1 else (
                  'яблук.' if 4 < apples_on_miniPeople < 21 or apples_on_miniPeople % 10 == 0 or
                              str(apples_on_miniPeople)[
                                  -1] == '1' else 'яблука.'))
    else:
        print(f'Дітям достанеться по {apples_on_miniPeople}',
              'яблуку.' if apples_on_miniPeople == 1 else (
                  'яблук.' if 4 < apples_on_miniPeople < 21 or apples_on_miniPeople % 10 == 0 or
                              str(apples_on_miniPeople)[
                                  -1] == '1' else 'яблука.'), f'і {apples % miniPeople} залишиться в кошику.')


def school_desks():
    miniPeople_classrooms = input("Введіть скільки дітей начається в класах математики через пробіл? ").split(" ")
    classroom = ('першого', 'другого','третього')
    # print(miniPeople_classrooms)
    school_desks_classrooms = []
    for x in range(3):
        school_desks_classrooms.append(round(int(miniPeople_classrooms[x]) / 2))
    print("Потрібно закупити",end='')
    for x in range(3):
        print(f'{school_desks_classrooms[x]} парт для')


# aple_task()
school_desks()
