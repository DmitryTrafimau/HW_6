
import os
os.chdir("E:\\")

with open('text.txt', 'w+') as f:
    f.write('Hello!'+'\n')

while True:
    name = input('What is your name?')
    age = input('How old are you?')
    with open('text.txt', 'a') as f:
        f.write(repr({name: age})+'\n')
    with open('text.txt', 'r') as f:
        for line in f:
            print(line)

