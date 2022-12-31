print('>>>', eval('1+2+(10+((1+2)+(1+12))+12)'))
test_value = '1+2+(10+((1+2)+(1+12))+12)'
ver_test = '0123456789'
oper_test = '()*/+-'

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



def pars_bkt(xxx):
    sing_lft = 0
    sing_rght = 0
    for sing in xxx:
        if sing == '(':
            sing_lft +=1
        if sing == ')':
            sing_rght +=1
    if sing_rght == sing_lft:
        return True
    else:
        print("Вирадення не має однакову кількість скобок")
        return False

def pars_oprtr(xxx):
    if xxx[0] in oper_test:
        print("Вираження не може розпочинатися з із знаків '+', '-','*','/'")
        return False
    for sing in range(1,len(xxx)-1):
        if xxx[sing] in oper_test[:2]:
            if xxx[sing-1] in oper_test[:2] or xxx[sing+1] in oper_test[:2]:
                print("Вираження має декілька операндів підряд")
            return False






print(pars(test_value))
pars_oprtr(pars(test_value))