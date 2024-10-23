from pystyle import *
from geopy.distance import geodesic
print(Box.Lines('[+] Learn python with rakwan'))
Write.Print('[+]this program for space between citys:\n',Colors.blue_to_purple,interval=0.1)
print(Box.DoubleCube('Example 6'))
Write.Print('[+] Space between city is :\n',Colors.blue_to_purple,interval=0.1)
first_place= (33.53333,-7.58333)
second_place=(31.63000,-8.00889)
dis=int(geodesic(first_place,second_place).km)

print(dis,'km')
input('\n press any key to exit ....')
