print('>>>', eval('1+(2+(10+((1+2)+(1+12))+12))'))
test_value = '1+(2+(10+((1+2)+(1+12))+12))'
ver_test = '0123456789'
oper_test = '()*/+-'
test_error = False


def pars(xxx):
    tm_variable = ''
    for x in range(len(xxx)):
        if x == 0 and xxx[x] in ver_test:
            tm_variable = tm_variable + xxx[x]
        elif xxx[x] in oper_test:
            if xxx[x - 1] in oper_test:
                tm_variable = tm_variable + xxx[x] + ' '
            else:
                tm_variable = tm_variable + ' ' + xxx[x] + ' '
        else:
            if xxx[x] in ver_test:
                tm_variable = tm_variable + xxx[x]
    tm_variable = tm_variable.split()
    return tm_variable


def pars_error(xxx):
    sing_lft = 0
    sing_rght = 0
    for sing in xxx:
        if sing == '(':
            sing_lft += 1
        if sing == ')':
            sing_rght += 1
    if sing_rght != sing_lft:
        print("Вираження має не однакову кількість скобок")
        return False
    if xxx[0] in oper_test[2:]:
        print("Вираження не може розпочинатися з із оператору '+', '-','*','/'")
        return False
    for sing in range(1, len(xxx) - 1):
        if xxx[sing] in oper_test[2:] and (xxx[sing - 1] in oper_test[2:] or xxx[sing + 1] in oper_test[2:]):
            print("Вираження має декілька операторів підряд")
            return False
    for sing in range(1, len(xxx)):
        if xxx[sing] in ')' and (xxx[sing - 1] in oper_test[2:]):
            print('Перед ")" не може бути оператора')
            return False
        if xxx[sing] in '(' and (xxx[sing + 1] in oper_test[2:]):
            print('Після "(" не може бути оператора')
            return False
    return True


def bkt(xxx):
    while '(' in xxx:
        sing_lft = []
        sing_rght = []
        for sing in range(len(xxx)):
            if xxx[sing] == '(':
                sing_lft.append(sing)
            elif xxx[sing] == ')':
                sing_rght.append(sing)

        ind_lft = sing_lft.pop()
        ind_rght = 0
        for x in range(len(sing_rght)):
            if sing_rght[x] > ind_lft:
                ind_rght = sing_rght.pop(x)
                break
        coun = xxx[ind_lft + 1:ind_rght]
        xxx = xxx[:ind_lft] + operator(coun) + xxx[ind_rght + 1:]
    return xxx
    # print(sing_lft,sing_rght,sep='\n')


def operator(xxx):
    tm_variable = 0
    while len(xxx) >= 3:
        if '*' in xxx:
            tm_variable = [int(xxx[xxx.index('*') - 1]) * int(xxx[xxx.index('*') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('*') - 1] + tm_variable + xxx[xxx.index('*') + 2:]
            else:
                xxx = tm_variable
        if '/' in xxx:
            tm_variable = [int(xxx[xxx.index('/') - 1]) / int(xxx[xxx.index('/') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('/') - 1] + tm_variable + xxx[xxx.index('/') + 2:]
            else:
                xxx = tm_variable
        if '+' in xxx:
            tm_variable = [int(xxx[xxx.index('+') - 1]) + int(xxx[xxx.index('+') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('+') - 1] + tm_variable + xxx[xxx.index('+') + 2:]
            else:
                xxx = tm_variable
        if '-' in xxx:
            tm_variable = [int(xxx[xxx.index('-') - 1]) - int(xxx[xxx.index('-') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('-') - 1] + tm_variable + xxx[xxx.index('-') + 2:]
            else:
                xxx = tm_variable
    return xxx


while test_error == False:
    varchar = pars(input("Введіть обрахунки: "))
    test_error = pars_error(varchar)
varchar = bkt(varchar)
if len(varchar) > 1:
    print(*operator(varchar))
else:
    print(*varchar)
