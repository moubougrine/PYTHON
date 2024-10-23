import requests 
from bs4 import BeautifulSoup as bs
from pystyle import *
import arabic_reshaper
from bidi.algorithm import get_display
print(Box.Lines('[+]Learn python with rakwan[+]'))
Write.Print('This program for prayer time \n',Colors.blue_to_cyan,interval=0.1)
print(Box.DoubleCube('Example [9]'))

## if want to connect internt for long time you need to use user agent##

ua={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

r=requests.get('https://timesprayer.com/prayer-times-in-fes.html',headers=ua)
soup = bs(r.content, 'html.parser') 

all_tr_elements = soup.find(class_='prayerDes').find_all('tr')

# Now you can access each <tr> element in the list
for tr_element in all_tr_elements:
    txt=tr_element.text
    reshaped_text=arabic_reshaper.reshape(txt)
    bidi_text=get_display(reshaped_text)
    print(bidi_text)
input(' \n press any key to exit ...')