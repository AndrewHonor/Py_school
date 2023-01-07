from random import randint

cash = 'qwertyuiopasdfghjklzxcvbnm'
my_str_1 = ''
my_str_2 = ''
new_str =""
for x in range(randint(10, 15)):
    my_str_1 += cash[randint(1, len(cash) - 1)]
for x in range(randint(10, 15)):
    my_str_2 += cash[randint(1, len(cash) - 1)]
print(my_str_1, my_str_2, sep='\n')
########
for ent in my_str_1:
    if my_str_1.count(ent)==1 and my_str_2.count(ent) ==1:
        new_str+=ent
print(new_str)