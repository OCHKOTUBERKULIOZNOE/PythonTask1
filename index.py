#Import module
import csv
import os


#Parse CSV file in dictionary

#https://realpython.com/python-csv/

#Разделить имя и фамилию


#Отрезать все буквы, кроме первой от имени

# Слить букву имени с фамилией


# Создать цикл (луп) по созданию папок первой буквы имени и фамилии
#https://www.w3schools.com/python/python_for_loops.asp
file=list()




with open('employeelist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        file.append(f'{row[0][0]}{row[1]}')
        line_count += 1         

os.mkdir('papka_dlya_sotrudnikov')
for x in file:
    os.mkdir("./papka_dlya_sotrudnikov/"+x)

#else if

