import os


class Directory:
    def __init__(self, directory):
        self.directory = directory

    def create_directory_dict(self):
        # Створити списки файлів та директорій
        files = []
        dirs = []
        # Проітерувати всі записи в директорії та додати імена файлів та директорій до відповідних списків
        for entry in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, entry)):
                files.append(entry)
            elif os.path.isdir(os.path.join(self.directory, entry)):
                dirs.append(entry)

        # Створити словник, що містить списки імен файлів та директорій
        directory_dict = {'filenames': files, 'dirnames': dirs}
        return directory_dict

    def sort_directory_dict(self, reverse=False):
        # Створити словник з іменами файлів та директорій та відсортувати їх відповідно до значення параметра reverse
        directory_dict = self.create_directory_dict()
        sorted_dict = {}
        for key in directory_dict:
            sorted_dict[key] = sorted(directory_dict[key], reverse=reverse)
        return sorted_dict

    def create_file_or_directory(self):
        # Запит на ввід імені файлу чи директорії
        user_input = input("Enter a file or directory name: ")

        if '.' in user_input:
            # Створення файлу, якщо введене ім'я містить крапку (ознака файлу)
            file_path = os.path.join(self.directory, user_input)
            with open(file_path, 'w') as f:
                f.write('')
        else:
            # Створення директорії, якщо введене ім'я не містить крапку (ознака директорії)
            dir_path = os.path.join(self.directory, user_input)
            os.mkdir(dir_path)

        # Оновлення словника директорії
        self.directory_dict = self.create_directory_dict()
        print(self.directory_dict)

# Створення об'єкту класу Directory для роботи з вказаною директорією
directory_obj = Directory('C:/Users/Glo/PycharmProjects/Py_school')
# Створення словника імен файлів та директорій для вказаної директорії
directory_dict = directory_obj.create_directory_dict()
print(directory_dict)
# Створення об'єкту класу Directory та відсортування імен файлів та директорій у порядку зрозтання
dir = Directory('C:/Users/Glo/PycharmProjects/Py_school')
sorted_dict = dir.sort_directory_dict()
print(sorted_dict)
# Створення об'єкту класу Directory та відсортування імен файлів та директорій у порядку REVER
sorted_dict = dir.sort_directory_dict(reverse=True)
print(sorted_dict)

# Створення об'єкту класу Directory з оновленим словником на новим об'єктом
directory = Directory('.')
directory.create_file_or_directory()
