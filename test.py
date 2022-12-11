# print(eval(input('>>>>')))
# exec("a =" + input('>>>') + "\nprint(a)")
var_num = input(">>>")
mas_var = var_num.split()
# count = []
for x in reversed(range(len(mas_var))):
    if x == '(':
        for n in range(len(mas_var)):
            if n == ')':
                count = mas_var[x:n]
                break
print(count)
