import json
import csv

lst_censor = ["English",
              "world",
              "the",
              "little",
              "have",
              ]
symbols = ".,"
js_list = {}
name_file = 'Блокнот.txt'
censor_file = "good_file.txt"
with open(name_file, encoding='ASCII') as my_file:
    text_file = my_file.read()
    mas_file = text_file.split()


def fun_censor(file, censor):
    js_list.update([("Name file", censor_file)])
    for word in range(len(file)):
        for word_censor in censor:
            if word_censor in file[word]:
                if file[word][-1] in symbols:
                    file[word] = ''.join(["*", symbols[symbols.find(file[word][-1])]])
                    if word_censor in js_list:
                        js_list[word_censor] = js_list[word_censor] + 1
                    else:
                        js_list.update([(word_censor, 1)])
                else:
                    file[word] = "*"
                    if word_censor in js_list:
                        js_list[word_censor] = js_list[word_censor] + 1
                    else:
                        js_list.update([(word_censor, 1)])
    with open(censor_file, "w+") as good_file:
        good_file.write(' '.join(file))
    with open('stat.json', "w+") as js_file:
        js_file.write(' '.join(json.dumps(js_list)))
    with open('stat.csv', "w+", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in js_list.items():
            writer.writerow([key, value])


fun_censor(mas_file, lst_censor)
print()
