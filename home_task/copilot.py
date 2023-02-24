import os


class Directory:
    def __init__(self, directory):
        self.directory = directory

    def create_directory_dict(self):
        files = []
        dirs = []
        for entry in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, entry)):
                files.append(entry)
            elif os.path.isdir(os.path.join(self.directory, entry)):
                dirs.append(entry)

        directory_dict = {'filenames': files, 'dirnames': dirs}
        return directory_dict

    def sort_directory_dict(self, reverse=False):
        directory_dict = self.create_directory_dict()
        sorted_dict = {}
        for key in directory_dict:
            sorted_dict[key] = sorted(directory_dict[key], reverse=reverse)
        return sorted_dict

    def create_file_or_directory(self):
        user_input = input("Enter a file or directory name: ")
        if '.' in user_input:
            # Create a file
            file_path = os.path.join(self.directory, user_input)
            with open(file_path, 'w') as f:
                f.write('')
        else:
            # Create a directory
            dir_path = os.path.join(self.directory, user_input)
            os.mkdir(dir_path)

        # Update the directory dictionary
        self.directory_dict = self.create_directory_dict()
        print(self.directory_dict)


directory_obj = Directory('C:/Users/Glo/PycharmProjects/Py_school')
directory_dict = directory_obj.create_directory_dict()
print(directory_dict)

dir = Directory('C:/Users/Glo/PycharmProjects/Py_school')
sorted_dict = dir.sort_directory_dict()
print(sorted_dict)

sorted_dict = dir.sort_directory_dict(reverse=True)
print(sorted_dict)


directory = Directory('.')
directory.create_file_or_directory()
