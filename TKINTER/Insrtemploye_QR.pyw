from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox
from PIL import Image , ImageTk

root = Tk()
root.title('Employee')
root.geometry('400x450')
root.resizable(False,False)
root.config(bg='#f5f5f5')




def welcome():
    test = pyttsx3.init()
    test.setProperty('rate',150)
    test.setProperty('voice',test.getProperty('voices')[0].id)
    say = "Hello everyone welcome in insert employee program"
    test.say(say)
    test.runAndWait()

def Sv():
    nmaefile = e_save.get()
    name = entry1.get()
    co = entry2.get()
    job=entry3.get()
    saveinf=qrcode.make("Name : "+name + '\n' + "country : "+co +'\n'+"jobe : "+ job)
    saveinf.save('employee/'+nmaefile+'.jpg')
    messagebox.showinfo('save','save[' +nmaefile+ ']employee')



ph=Image.open(r'Designs\image.jpeg')
photo = ImageTk.PhotoImage(ph)
i_imgae=Label(root,image=photo)
i_imgae.place(x=2,y=1,width=395,height=220) 

text1 = Label(root,text="Emp Name  ",font=('Time New Roman',14))
text1.place(x=10,y=230)
entry1 = Entry(root,font=('Time New Roman',14))
entry1.place(x=130,y=230,height=30,width=200)

text2 = Label(root,text="Emp Country  ",font=('Time New Roman',14))
text2.place(x=10,y=270)
entry2 = Entry(root,font=('Time New Roman',14),
               )
entry2.place(x=130,y=270,height=30,width=200)

text3 = Label(root,text="Emp Job  ",font=('Time New Roman',14))
text3.place(x=10,y=310)
entry3 = Entry(root,font=('Time New Roman',14))
entry3.place(x=130,y=310,height=30,width=200)


l_save = Label(root,text='Save File',font=('Tajawal',14))
l_save.place(x=10,y=382)

e_save = Entry(root,font=('Tajawal',14))
e_save.place(x=100,y=382,width=190,height=30)

B_save=Button(root,text="Save💾",font=('Tajawal',12),bg='green',fg='black',command=Sv)
B_save.place(x=300,y=382,height=30,width=60)


welcome()  
root.mainloop()
