import json


class Employee:
    variable = {'firstname': '',
                'lastname': '',
                'age': 13,
                'e_mail': '',
                'skills': [],
                'people_lang': [],
                'coding_lang': [], }

    def print_data(self):
        """
        Вивід данних на консоль
        :return: None
        """
        print(
            f'firstname = {self.variable.get("firstname")}\n'
            f'lastname = {self.variable.get("lastname")}\n'
            f'age = {self.variable.get("age")}\n'
            f'e_mail = {self.variable.get("e_mail")}\n'
            f'skills = {self.variable.get("skills")}\n'
            f'people_lang = {self.variable.get("people_lang")}\n'
            f'coding_lang = {self.variable.get("coding_lang")}\n')

    def default_varible(self):
        """
        присвоєннся дефолтних значень для змінних класу
        :param name_clas: назва класу
        :return: None
        """
        self.variable["firstname"] = 'Ivasik'
        self.variable["lastname"] = 'Telesik'
        self.variable["age"] = 13
        self.variable["e_mail"] = 'ivasik-telesik1732@izkurnanog.ua'
        self.variable["skills"] = ['ходить', "говорить", "кодить"]
        self.variable["people_lang"] = ['Україньська', "Англійська"]
        self.variable["coding_lang"] = ['Python', "C++", "lisp"]

    def js_save(self):
        """
        Збереження данних в JSon - js_varible.json
        :return: None
        """
        with open('js_varible.json', "w+", encoding="utf-8") as file:
            json.dump(self.variable, file)

    def update_people_lang(self):
        char_people_lang = input(">>> Введіть мову яку знає студент: ")
        self.variable['people_lang'].append(char_people_lang)

    def update__coding_lang(self):
        char_coding_lang = input(">>> Введіть мову програмування яку знає студент: ")
        self.variable['coding_lang'].append(char_coding_lang)


student1 = Employee()

student1.default_varible()

student1.js_save()
student1.update__coding_lang()
student1.update_people_lang()
student1.print_data()
