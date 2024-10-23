from pystyle import *
import emoji 
import random
from playsound import playsound 
from gtts import gTTS
import webbrowser

print(Box.Lines('[+]Learn python with rakwan[+]'))
Write.Print('This program for chating with emoji \n',Colors.blue_to_cyan,interval=0.1)
print(Box.DoubleCube('Example [7]'))
e1 =  emoji.emojize(':yellow_heart:')
e2 = emoji.emojize(':blue_heart:')
e3 = emoji.emojize(':green_heart:')
e4 = emoji.emojize(':red_heart:')
e5 = emoji.emojize(':purple_heart:')

#======List======
emoj = [e1 ,e2 ,e3 ,e4 ,e5 ]
hi = ['welcome','hello','hi','welcome dear ']
name = ['moughit','mohamed','morad','mohsin']
while True :
    chat=input('Enter your massage : ')
    if chat == 'hello':
        answer = random.choice(hi)
        answer_emo= random.choice(emoj)
        print(answer + ' '+ answer_emo)
    else:
        print('prolem')
    
    Q=Write.Input('Sorry can I ask your name : ',Colors.blue_to_cyan,interval=0.03)
    if Q == 'moughit':
        Ql='We missing you a lot Mr '+Q
        pll=gTTS(text=Ql)
        pll.save('welcome.mp3')
        playsound('welcome.mp3')
        f=Write.Input("What do you looking for Mr moughit : ",Colors.blue_to_cyan,interval=0.03)
        webbrowser.open('https://www.google.com/search?q='+f)
        break
    else : 
        print('Sorry we didn`t know you ')
        

input('\n\n\n press any key to exit .....')


            
