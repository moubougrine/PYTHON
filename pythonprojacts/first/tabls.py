from pystyle import *
from tabulate import tabulate
from prettytable import PrettyTable
print(Box.Lines('[+]Learn python with rakwan[+]'))
Write.Print('This program for good student  \n',Colors.blue_to_cyan,interval=0.1)
print(Box.DoubleCube('Example [8]'))

name = input('Enter your name  : ')
Write.Print('Welcome : ',Colors.cyan_to_blue,interval=0.03)
print(name)
Write.Print('Write your grade now\n\n',Colors.blue_to_cyan,interval=0.03)
math=float(Write.Input('Enter math grade : ',Colors.green_to_blue,interval=0.01))
arabic=float(Write.Input('Enter arabic grade : ',Colors.green_to_blue,interval=0.01))
english=float(Write.Input('Enter english grade : ',Colors.green_to_blue,interval=0.01))
sport =float(Write.Input('Enter sport grade : ',Colors.green_to_blue,interval=0.01))

head=['subject','grades']
finall_grade= [
    ['math',math],
    ["arabic",arabic],
    ['english',english],
    ['sport',sport]
]

finall=math+arabic+english+sport
n=finall/4



pl=[
    ['Toal',n]
    
]

print(tabulate(finall_grade,headers=head,tablefmt='grid'))
print(tabulate(pl,tablefmt='grid'))
def x():
    if 14<n<11 :
        print('Good')
    elif 14<n<16 :
        print('Very Good')
    elif 16<n<=20 :
        print('Exellent')
    else:
        print(000000)

print(x())

input('press any key to exit .....')
