# print(eval(input('>>>>')))
# exec("a =" + input('>>>') + "\nprint(a)")
# var_num = input(">>>")
var_num = '1 + 2 + ( 4 + 5 ) + 6'
mas_var = var_num.split()
print(mas_var)


# count = []
def calculation(xxx):
    tm_variable = 0
    while len(xxx) >= 3:
        if '*' in xxx:
            tm_variable = [int(xxx[xxx.index('*') - 1]) * int(xxx[xxx.index('*') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('*')] + tm_variable + xxx[xxx.index('*') + 1:]
            else:
                xxx = tm_variable
        if '/' in xxx:
            tm_variable = [int(xxx[xxx.index('/') - 1]) / int(xxx[xxx.index('/') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('/')] + tm_variable + xxx[xxx.index('/') + 1:]
            else:
                xxx = tm_variable
        if '+' in xxx:
            tm_variable = [int(xxx[xxx.index('+') - 1]) + int(xxx[xxx.index('+') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('+')-1] + tm_variable + xxx[xxx.index('+') + 1:]
            else:
                xxx = tm_variable
        if '-' in xxx:
            tm_variable = [int(xxx[xxx.index('-') - 1]) - int(xxx[xxx.index('-') + 1])]
            if len(xxx) > 3:
                xxx = xxx[:xxx.index('-')] + tm_variable + xxx[xxx.index('-') + 1:]
            else:
                xxx = tm_variable
        # for x in range(len(xxx)):
        #     if xxx[x] == '*':
        #
        #         xxx = xxx[:x] + tm_variable + xxx[x + 1:]
        #     elif xxx[x] == '/':
        #         tm_variable = int(xxx[x - 1]) / int(xxx[x + 1])
        #         xxx = xxx[:x] + xxx[x + 1:]
        #     elif xxx[x] == '+':
        #         tm_variable = int(xxx[x - 1]) + int(xxx[x + 1])
        #         xxx = xxx[:x] + xxx[x + 1:]
        #     elif xxx[x] == '-':
        #         tm_variable = int(xxx[x - 1]) - int(xxx[x + 1])
        #         xxx = xxx[:x] + xxx[x + 1:]
    return xxx


def alternation(xxx):
    while "(" or ")" in xxx:
        for x in reversed(range(len(xxx))):
            if xxx[x] == '(':
                for n in range(len(xxx)):
                    if xxx[n] == ')':
                        t_x = x
                        t_n = n
                        coun = xxx[t_x + 1:t_n]
                        xxx = xxx[:t_x] + calculation(coun) + xxx[t_n + 1:]
                        break
                break
        break
    return xxx

mas_var = alternation(mas_var)
print(mas_var)
print(calculation(mas_var))
