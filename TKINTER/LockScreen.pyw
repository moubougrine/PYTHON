from tkinter import *
from tkinter import messagebox
import cv2
import os 

root=Tk()
root.title('Screen lock ')
root.geometry('300x520')
root.resizable(False,False)
root.attributes('-alpha',0.6)

###read Button ###
def Read(enent=None):
    pas = entry1.get()

    if pas != 'Moughit201A':
        messagebox.showerror('Error',"Passwor False")
        entry1.delete(0, END)
        global error1
        error1=Label(E1,text='Error Password !!',fg='red',bg='white',font=('Tajawal',10,'bold'))
        error1.place(x=105,y=105)
        s=cv2.VideoCapture(0)
        ret,image = s.read()
        cv2.imwrite('loock.png',image)
        del(s)
    else:
        os.startfile(r'C:\pythonprojacts\projact\projact1.pyw')
        os.startfile(r'C:\pythonprojacts\projact\ReadQr.pyw')
        entry1.delete(0, END)
        error1.place(x=500, y=55545)
###Clean Button##
def Clean(enent=None):
    entry1.delete(0, END)
    error1.place(x=500, y=55545)

###Number Button###
def One(enent=None):
    one = 1
    entry1.insert(END,one)
def Tow(enent=None):
    one = 2
    entry1.insert(END,one)
def Tr(enent=None):
    one = 3
    entry1.insert(END,one)
def For(enent=None):
    one = 4
    entry1.insert(END,one)
def Fiv(enent=None):
    one = 5
    entry1.insert(END,one)
def Six(enent=None):
    one = 6
    entry1.insert(END,one)
def Sev(enent=None):
    one = 7
    entry1.insert(END,one)
def Ni(enent=None):
    one = 9
    entry1.insert(END,one)
def Ei(enent=None):
    one = 8
    entry1.insert(END,one)
def Zir(enent=None):
    one = 0
    entry1.insert(END,one)

lab = Label(root,text="Screen Lock",fg='white',bg='#D82148',font=('Tajawal',21,'bold'))
lab.place(x=0,y=1,width=300,height=40)

E1=Frame(root,bg='white')
E1.place(x=0,y=41,height=500,width=300)

title = Label(E1,text="Enter Password",fg='black',bg='white',font=('Tajawal',15,'bold'))
title.place(x=75,y=10)

entry1=Entry(E1,justify=CENTER,font=('Impact',25),bd=2,relief=RIDGE,width=10,bg='white',fg='#D82148')
entry1.place(x=60,y=50)

B1=Button(E1,text="1",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=One)
B1.place(x=25,y=135)
B4=Button(E1,text="4",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=For)
B4.place(x=25,y=225)
B7=Button(E1,text="7",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Sev)
B7.place(x=25,y=315)

B2=Button(E1,text="2",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Tow)
B2.place(x=115,y=135)
B5=Button(E1,text="5",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Fiv)
B5.place(x=115,y=225)
B8=Button(E1,text="8",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Ei)
B8.place(x=115,y=315)

B3=Button(E1,text="3",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Tr)
B3.place(x=210,y=135)
B6=Button(E1,text="6",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Six)
B6.place(x=210,y=225)
B8=Button(E1,text="9",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Ni)
B8.place(x=210,y=315)

Bx=Button(E1,text="❌",font=('Impact',30,'bold'),bd=0,fg='red',bg='white',relief=GROOVE,width=3,cursor='hand2',command=Clean)
Bx.place(x=25,y=390)
B0=Button(E1,text="0",font=('Impact',30,'bold'),bd=0,bg='white',relief=GROOVE,width=3,cursor='hand2',command=Zir)
B0.place(x=115,y=390)
By=Button(E1,text="✔",font=('Impact',30,'bold'),bd=0,bg='white',fg='green',relief=GROOVE,width=3,cursor='hand2',command=Read)
By.place(x=210,y=390)

root.mainloop()