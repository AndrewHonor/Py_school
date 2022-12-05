from blb import true_Namber


def calc_supper():
    # Написать калькулятор для простых операций(+,-,*,/,**),
    print("Супер калькулятор")
    var_num = input('Введіть що там потрібно обрахувати: ')
    var_num = eval(var_num)
    print(var_num)

def calc_mini ():
    print("Міні калькулятор")
    var_num = input('Введіть що там потрібно обрахувати: ')


def square():
    print("Генератор квадратних чисел.")
    var_num = int(true_Namber('Введіть границю квадратних натуральних чисел: '))
    for x in range(1, var_num):
        if x ** 2 >= var_num:
            break
        print(x ** 2, end=" ")


def simple_Num():
    print('Перевірка числа на простоту')
    var_num = int(true_Namber('Введіть число: '))
    if var_num % 2 == 0:
        return var_num == 2
    count = 3
    while count * count <= var_num and var_num % count != 0:
        count += 2
    return count * count > var_num


def masha():
    mas_mushrm = ['', 'ів', 'а']
    var_num = int(true_Namber('Введіть кількість грибів: '))
    count = 0
    if var_num == 0 or 5 <= var_num <= 19 or int(str(var_num)[-1]) == 0 or 4 < int(str(var_num)[-1]) <= 9:
        count = 1
    elif 2 <= int(str(var_num)[-1]) <= 4:
        count = 2
    else:
        count = 0
    print(f'Маша нашла в лісі {var_num} гриб{mas_mushrm[count]}')


#print("Число просте" if simple_Num() else "число не просте")
calc_supper()
#square()
#masha()
