print(eval('(1 + 2) * (2 + ( 4 + 5 ) )+ 6'))
# exec("a =" + input('>>>') + "\nprint(a)")
# var_num = input(">>>")
ver_test = '0123456789'
oper_test = '()*/+-'
var_num = '1+2+10+(1+2)+1+(12+12)'
# var_num = '( 1 + 2 ) * ( 2 + ( 4 + 5 ) ) + 6'



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
    return tm_variable


# count = []
def calculation(xxx):
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


def alternation(xxx):
    while "(" in xxx:
        for x in reversed(range(len(xxx))):
            if xxx[x] == '(':
                cut_xxx = xxx[x:]
                for n in range(len(cut_xxx)):
                    if cut_xxx[n] == ')':
                        t_x = x
                        t_n = n + len(xxx[:x])
                        coun = xxx[t_x + 1:t_n]
                        xxx = xxx[:t_x] + calculation(coun) + xxx[t_n + 1:]
                        break
                break

    return xxx


# mas_var = alternation(mas_var)
# print(mas_var)
mas_var = pars(var_num.split())
print(calculation(mas_var))
#print(pars(var_num))
