# my_file = open()
lst_censor = ["Росія", "Російської"]
lst_good = ["Заболотія", "Свинособацької"]
symbols = '.,'
# mas_file = []
with open('inpt.txt', encoding='utf-8') as my_file:
    text_file = my_file.read()
    mas_file = text_file.split()


def fun_censor(file, censor, good):
    for word in range(len(file)):
        for word_censor in censor:
            if word_censor in file[word]:
                if file[word][-1] in symbols:
                    file[word] = ''.join([good[censor.index(word_censor)], symbols[symbols.find(file[word][-1])]])
                else:
                    file[word] = good[censor.index(word_censor)]
    with open("good_file.txt", "w+") as good_file:
        good_file.write(' '.join(file))
    print(file)


fun_censor(mas_file, lst_censor, lst_good)
