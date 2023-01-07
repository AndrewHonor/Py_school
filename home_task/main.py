from lesson_10 import *
lst_name = ["Abraham", "Ada", "Adalbert", "Adam", "Adela", "Adeline", "Adolf", "Adrian", "Adriane", "Agatha",
                "Agnes", "Alan", "Alban", "Albert", "Alen", "Alex", "Alexander", "Alexandra", "Alexis", "Alfred",
                "Alice", "Alicia", "Alison", "Alistair", "Allan", "Allen", "Alvin", "Alvina", "Alwin", "Amanda",
                "Amberly", "Ambros", "Amelie", "Amice", "Amos", "Amy", "Anabel", "Andrew", "Andy", "Angela", "Angelika",
                "Anna", "Annabel", "Anselm", "Anstruther", "Badger", "Baldwin", "Balthasar", "Baptist", "Barbara",
                "Barbi", "Barnabas", "Barry", "Bartholomew", "Barton", "Daphne", "Darlene", "David", "Deborah", "Delia",
                "Denis", "Derek", "Elroy", "Elsa", "Elton", "Elwin", "Emily", "Emma", "Emmanuel", "Emmeline",
                "Emmerich", "Emmi", "Enoch", "Eric", "Erik", "Erika", "Erin", "Gilbert", "Giles", "Ginger", "Ginnie",
                "Gladys", "Glenn", "Gloria", "Godwin", "Gordon", "Gore"
                ]
lst_domains = ["ukr.net", "i.ua","meta.ua","online.ua","bigmir.ua","gmail.com"]

print()
print(fun_revers_lst_01(gen_lst(1)))
print()
print(fun_pars_lst_first_a(gen_lst(1)))
print()
print(fun_pars_lst_in_a(gen_lst(1)))
print()
print(fun_pars_lst_str(gen_lst(2)))
print()
print(fun_transformation_str_lst_uniq(gen_str()))
print()
print(fun_transformation_dblw_str_lst(gen_str(), gen_str()))
print()
print(fun_transformation_dblw_str_lst_uniq(gen_str(), gen_str()))
print()
input('Нажміть Enter, щоб продовжити')
print(fun_gen_e_mail(lst_name,lst_domains))
print()
