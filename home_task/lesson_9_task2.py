my_dict_1 = {
    "id": "1",
    "name": "Anton",
    "age": 18,
    "gender": "female ",
    "nationality": "Ukrainian",
    "cash": "150",
    "job": "military"
}
my_dict_2 = {
    "id": "2",
    "key": "prime",
    "gender": "male",
    "job": "military"
}
lst1 = my_dict_1.keys()
lst2 = my_dict_2.keys()
lst_key_1 = []
lst_key_2 = []
my_dict_3 = {}
my_dict_4 = {}
for i in lst1:
    if i in lst2:
        lst_key_1.append(i)
    if i not in lst2:
        lst_key_2.append(i)
for i in lst_key_1:
    my_dict_3[i] = my_dict_1[i]
my_dict_4 = my_dict_1.copy()
for i in my_dict_2:
    if i in my_dict_4:
        my_dict_4[i] = [my_dict_4[i], my_dict_2[i]]
    if i not in my_dict_4:
        my_dict_4[i] = my_dict_2[i]
print(lst_key_1)
print(lst_key_2)
print(my_dict_3)
print(my_dict_4)
