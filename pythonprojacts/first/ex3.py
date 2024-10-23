from pystyle import *
print(Box.Lines('[+] Learn python with Rakwan'))
Write.Print('[+]this program for simple cal\n',Colors.blue_to_purple,interval=0.1)
print(Box.DoubleCube('Example 3 '))
while True :
    num1=int(Write.Input('Enter the number :',Colors.blue_to_purple,interval=0.01))
    for n in range(1,11):
        print(num1,'X',n,'=',num1*n)
    break

