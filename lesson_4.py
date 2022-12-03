def calc_supper():
    # Написать калькулятор для простых операций(+,-,*,/,**),
    print("Супер калькулятор")
    var_char = input()
    var_char = eval(var_char)
    print(var_char)


# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
def square():
    var_char = int(input(""))
    for x in range(1,var_char):
        if x ** 2 >= var_char:
            break
        print(x ** 2, end=" ")



#calc_supper()
square()
