from pystyle import *

print(Box.Lines("[+]this program work like  calculator[+]\n"))
Write.Print(' [+]Start\n \n',Colors.blue_to_cyan,interval=0.1)
print(Box.DoubleCube('Example 2'))

while True :
    num1=int(Write.Input("Enter the first number :",Colors.blue_to_cyan,interval=0.1))
    TT2=Write.Input('Enter the Math code:',Colors.blue_to_cyan,interval=0.01)
    num2=int(Write.Input('Enter the second Number :',Colors.blue_to_cyan,interval=0.01))
    if TT2 == "+":
        Write.Print("[+] Reasult is :",Colors.green_to_blue,interval=0.1)
        print(num1+num2)
        break
    elif TT2 == '*':
        Write.Print("[+] Reasult is :",Colors.green_to_blue,interval=0.1)
        print(num1*num2)
        break
    elif TT2 == '-':
        Write.Print("[+] Reasult is :",Colors.green_to_blue,interval=0.1)
        print (num1-num2)
        break
    elif TT2 == '/':
        Write.Print("[+] Reasult is :",Colors.green_to_blue,interval=0.1)
        print(num1/num2)
        break
    else:
        Write.Print('[-] Error Try again\n\n',Colors.red,interval=0.1)

input('\n press any key to exit ...')