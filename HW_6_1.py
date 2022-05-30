import csv
import os
import json

os.chdir('E:\\')

with open('text_file.json', 'w+') as h:
    h.write('Hello!'+'\n')

with open('text_file.csv', 'w+', encoding='utf-8', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=' ',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    wr.writerow(['Hello!'])

final_dic = {}
name_list = []
age_list = []

print('Hello!')

name = input('What is your name?')
age = input('How old are you?')

while name:
    name_list.append(name)
    age_list.append(age)
    dic = {'Name': name_list, 'Age': age_list}
    final_dic.update(dic)

    with open('text_file.json', 'a') as f:
        f.write(repr({'Name': name, 'Age': age}) + '\n')

    with open('text_file.csv', 'a', encoding='utf-8', newline='') as csvfile:
        wr = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(['Name:', name] + ['Age:', age])

    name = input('What is your name?')
    if name:
        age = input('How old are you?')

import pandas as pd
x = pd.DataFrame(final_dic)

import os
os.chdir('E:\\')
x.to_excel('./Data_List.xlsx', sheet_name='Data', index=False)