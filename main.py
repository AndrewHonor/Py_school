import blb

list_of_letters = "abcdefghijklmnopqrstuvwxyzабвгдеєжзиіїйклмнопрстуфхцчшщьюя "
output_letter = input('Яким символом малювати ім\'я: ')
my_name = input('Введіть ім\'я: ')
my_name = my_name.lower()
number_of_letters = len(my_name)

star_name = []
for x in range(5):
    for i in my_name:
        index_letter = list_of_letters.find(i)
        string_part = ''.join(blb.star_letters[index_letter][x])
        print(string_part.replace('*', output_letter), end='')
    print('')
print('')

print('import antigravity', 'import __hello__', 'from __future__ import braces', sep='\n')

print('Escape sequences',
        "\\a      Bell (alert)",
        "\\b      Backspace",
        "\\n      New line",
        "\\t      Horizontal tab",
        "\\\      Backslash \\",
        '\\"      Double quotation mark "',
        "\\'      Single quotation mark '",sep='\n')