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
