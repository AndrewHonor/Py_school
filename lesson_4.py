from blb import true_Namber
def calc_supper():
    text01 = 'Введіть що там обрахувати потрібно: '
    # Написать калькулятор для простых операций(+,-,*,/,**),
    print("Супер калькулятор")
    var_char = true_Namber(text01)
    var_char = eval(var_char)
    print(var_char)


# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
def square():
    var_char = int(input(""))
    for x in range(1,var_char):
        if x ** 2 >= var_char:
            break
        print(x ** 2, end=" ")

def simple_Num():
    pass


#calc_supper()
square()
simple_Num()