import time
import csv
import numpy as np

#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####
#Дополнительная задача находится в файле Animation.py

def esc(code):
    return f'\u001b[{code}m'


RED = esc(41)
BLUE = esc(44)
WHITE = esc(40)
END = esc(0)
BLACK = esc(107)


def Flag():

    width = 30
    height = 9

    red = "\033[48;2;255;0;0m  \033[m" 
    white = "\033[48;2;255;255;255m  \033[m" 
    blue = "\033[48;2;0;0;255m  \033[m" 

  
    for row in range(height):
        for col in range(width):
         
            if row == 0:
                print(red, end="")
            elif row in [1, 2]:
                print(white, end="")
            elif row in [3, 4, 5]:
                print(blue, end="")
            elif row in [6, 7]:
                print(white, end="")
            elif row == 8:
                print(red, end="")
        print()


def Pattern():

    print(WHITE + '  ' * (2) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (
        3) + BLACK + '  ' * (
              1) + WHITE + '  ' * (2) + END)
    print(WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (
        1) + BLACK + '  ' * (1) + WHITE + '  ' * (1)
          + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (
              1) + WHITE + '  ' * (1) + END)
    print(BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (
        1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + END)


def Graph():

    x = np.arange(0.1, 5.0, 0.1)
    y = 1 / x
    graph = ""
    for i in range(40):
        for j in range(len(x)):
            if int(y[j] * 10) == i:
                graph += "."
            elif j == len(x) - 1:
                graph += "|"
            elif i == 39:
                graph += "-"
            else:
                graph += " "
        graph += "\n"

    print(graph)
    print('', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def BooksCalc(n): #Books above 50 rubles

    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        books = csv.reader(csvfile, delimiter=';')

        big = 0
        small = 0
        z = -1
        for row in list(books)[1:]:
            price = row[10][:2]

            if int(price) >= n:
                small += 1
            else:
                big += 1

    all = big + small

    a = small * 100 // all
    b = big * 100 // all + 1

    print("Less Than 50 Rubles    " + RED + '  ' * a + END + ' ' + str(a) + '%')
    print()
    print("More Than 50 Rubles  " + RED + '  ' * b + END + ' ' + str(b) + '%')
    print()


Flag()  #1st Task
Pattern() #2nd Task 
BooksCalc(50) #3rd Task
Graph()  #4th Task


time.sleep(1)
time.sleep(1)