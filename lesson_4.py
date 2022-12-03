from blb import true_Namber
def calc_supper():
    # Написать калькулятор для простых операций(+,-,*,/,**),
    print("Супер калькулятор")
    var_num = input('Введіть що там потрібно обрахувати: ')
    var_num = eval(var_num)
    print(var_num)


# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
def square():
    print("генератор квадратних чисел.")
    text01 = 'Введіть границю квадратних натуральних чисел: '
    var_num = int(true_Namber(text01))
    for x in range(1,var_num):
        if x ** 2 >= var_num:
            break
        print(x ** 2, end=" ")

def simple_Num():
    print('Перевірка числа на простоту')
    var_num = int(true_Namber('Введіть число: '))
    for i in range(2, (var_num // 2) + 1):
        if var_num % i == 0:
            return print('Число НЕ просте')
        else: return print("Число просте")


def masha ():
    #0- грибів
    #1 - гриб
    #2-4 - гриба
    #5-9 - грибів
    #21 - гриб
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    var_num = int(true_Namber('Введіть кількість грибів: '))
    count = 0
    if var_num ==0:
        count = 1
    else:
        if 5 <= var_num <= 19:
            count = 1
        else:
            if 2<= int(str(var_num)[-1]) <=4:
                pass
            elif:
                pass

    mas_mushrm = ['','ів','а']
    print(f'Маша нашла в лісі {var_num} гриб{mas_mushrm[count]}')
#calc_supper()
#square()
#simple_Num()
masha()