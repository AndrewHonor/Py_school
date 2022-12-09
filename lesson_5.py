from blb import true_namber


def range_var():
    # Генератор чисел
    my_string = '0123456789'
    my_range = [int(x + n) for x in my_string for n in my_string]
    print(*my_range, sep='\n')


def delta_a():
    # Малюємо пустий трикутник, це було важко підбирати числа
    var_nam = int(true_namber('введіть величину трикутника: '))
    for i in range(var_nam + 1):
        for j in range(2 * var_nam + 1):
            if var_nam - j == i or j - var_nam == i or i == var_nam:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def delta_b():
    pass
def delta_c():
    pass
def delta_d():
    pass

delta_a()
