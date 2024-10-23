from pystyle import *
import webbrowser
import pyshorteners as pshort
print(Box.Lines('[+] Learn python with Rakwan'))
Write.Print('[+]this program for short urls\n',Colors.blue_to_purple,interval=0.1)
print(Box.DoubleCube('Example 4'))

url=Write.Input("[-] Write url for short:",Colors.blue_to_purple,interval=0.1)
sh=pshort.Shortener()
Write.Print(sh.tinyurl.short(url),Colors.blue_to_purple,interval=0.1)
input('\npress any key to exit ....')
