from blb import true_namber


def range_var():
    # Генератор чисел
    my_string = '0123456789'
    my_range = [int(x + n) for x in my_string for n in my_string]
    print(*my_range, sep='\n')


def delta_a():
    # Малюємо пустий трикутник, це було важко підбирати числа
    var_nam = int(true_namber('Введіть величину трикутника_A: '))
    for i in range(var_nam + 1):
        for j in range(2 * var_nam + 1):
            if var_nam - j == i or j - var_nam == i or i == var_nam:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def delta_b():
    var_nam = int(true_namber('Введіть величину трикутника_B: '))
    for i in range(1,var_nam*2,2):
        print(('*' * i).center(var_nam * 2))


def delta_c():
    var_nam = int(true_namber('Введіть величину трикутника_C: '))
    mass_l_u = [ [' '] * var_nam for i in range(var_nam)]
    mass_r_u = [ [' '] * var_nam for i in range(var_nam)]
    mass_l_d = [ [' '] * var_nam for i in range(var_nam)]
    mass_r_d = [ [' '] * var_nam for i in range(var_nam)]
    x = '*'
    y = ' '
    for i in range(var_nam):
        for j in range(var_nam):
            if i >= var_nam - 1 -j:
                mass[i][j]= x
    for x in mass:
        print(*x)

def delta_d():
    pass

delta_c()
