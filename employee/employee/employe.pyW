from tkinter import *
import pyttsx3
from PIL import ImageTk , Image
import time
from tkinter import ttk ,messagebox
from datetime import datetime
from Database import Databs
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
        os.replace('C:\PYTHON\loock.png','C:\PYTHON\employee\employee\jp.jpg')
        del(s)
    else:
        entry1.delete(0, END)
        root.destroy()
        db=Databs("C:\PYTHON\employee\employee\Employee.db")


        app = Tk()
        app.geometry('850x450+350+150')
        app.title("Employe Program")
        app.configure(background='#6A6A6A')
        app.resizable(width=False,height=False)
        
        lname=StringVar()
        fname=StringVar()
        age=IntVar()
        CIN=StringVar()
        job=StringVar()
        city=StringVar()
        mobel=IntVar()
        Email=StringVar()
        searchh=StringVar()
        
        def getData(event):
            select_row = tv.focus()
            data = tv.item(select_row)
            global row
            row = data['values']
            lname.set(row[1])
            fname.set(row[2])
            age.set(row[3]) 
            CIN.set(row[4])
            job.set(row[5])
            city.set(row[6])
            mobel.set(row[7])
            Email.set(row[8])
        
        def Search():
            # الحصول على قيمة البحث من مربع الإدخال
            search_value = searchh.get().strip()

            # التأكد من عدم وجود قيمة فارغة
                # حذف جميع العناصر من الجدول قبل عرض نتائج البحث
            tv.delete(*tv.get_children())

                # البحث عن البيانات التي تطابق قيمة البحث
            search_results = db.Searchh(search_value)
            for row in search_results:
                    # إضافة نتائج البحث إلى الجدول
                tv.insert("", "end", values=row)

                # إعادة ضبط مربع البحث بعد الانتهاء
            searchh.set("")
            displayall()

        
        def Clear():
            lname.set("")
            fname.set("")
            age.set("")
            CIN.set("")
            job.set("")
            city.set("")
            mobel.set("")
            Email.set("")
        def Delete():
            db.remove(row[0])
            Clear()
            displayall()
        
        def displayall():
            tv.delete(*tv.get_children())
            for row in db.fetch() :
                tv.insert("",END,values=row)
        
        def Add():
            if e_name.get() == "" or e_fname.get() == ""or e_cin.get() == ""or e_number.get()== ""or e_email.get() == "":
                messagebox.showerror("ERROR","Plese Fill all the Entry")
                return
            db.insert(
                e_name.get(),
                e_fname.get(),
                int(e_age.get()),  
                e_cin.get(),
                e_job.get(),
                e_city.get(),
                e_number.get(),
                e_email.get()
            )
            say=f"Added new Employee Successfully"
            engin = pyttsx3.init()
            engin.setProperty('rate',180)
            engin.setProperty('voice', engin.getProperty('voices')[0].id)
            engin.say(say)
            engin.runAndWait()
            displayall()
            Clear()
        def Update():
            if e_name.get() == "" or e_fname.get() == ""or e_cin.get() == ""or e_number.get()== ""or e_email.get() == "":
                messagebox.showerror("ERROR","Plese Fill all the Entry")
                return
            db.update(row[0],
                e_name.get(),
                e_fname.get(),
                int(e_age.get()),  
                e_cin.get(),
                e_job.get(),
                e_city.get(),
                e_number.get(),
                e_email.get()
            )
            Clear()
            displayall()
        
        App_title_frame = Frame(app,width=830,height=60,bg='#4F5A60')
        App_title_frame.place(x=10,y=10)
        App_date=datetime.now()
        x_date = App_date.strftime('%d-%m-%Y\n%Hh/%Mm')
        date_label = Label(app,text=x_date,bg='#4F5A60',font=('Arisl Greek', 10,'bold'))
        date_label.place(x=70,y=18)
        
        name = Label(app,text="~📎LastName ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        name.place(x=15,y=150)
        e_name=Entry(app,textvariable=lname,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_name.place(x=110,y=150,width=170)
        
        ffname = Label(app,text="~📎FirstName ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        ffname.place(x=295,y=150)
        e_fname=Entry(app,textvariable=fname,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_fname.place(x=395,y=150,width=170)
        
        aage = Label(app,text="~📎Age ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        aage.place(x=570,y=150)
        e_age=Entry(app,textvariable=age,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_age.place(x=620,y=150,width=170)
        
        
        cinn = Label(app,text="~📎CIN ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        cinn.place(x=15,y=180)
        e_cin=Entry(app,textvariable=CIN,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_cin.place(x=110,y=180,width=170)
        
        jobb = Label(app,text="~📎Job ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        jobb.place(x=300,y=180)
        e_job=Entry(app,textvariable=job,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_job.place(x=395,y=180,width=170)
        
        cityy = Label(app,text="~📎City ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        cityy.place(x=570,y=180)
        e_city=Entry(app,textvariable=city,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_city.place(x=620,y=180,width=170)
        
        number = Label(app,text="~📎PhoneNumber ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        number.place(x=60,y=210)
        e_number=Entry(app,textvariable=mobel,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_number.place(x=185,y=210,width=210)
        
        email = Label(app,text="~📎Email ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        email.place(x=430,y=210)
        e_email=Entry(app,textvariable=Email,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
        e_email.place(x=500,y=210,width=210)
        
        search = Button(app,text="Search",bg='#4F5A60',font=('Arisl Greek', 10,'bold'),command=Search).place(x=570,y=295,width=170)
        e_search=Entry(app,textvariable=searchh,bg='#6A6A6A',font=('Arisl Greek', 10,'bold')).place(x=150,y=295,width=400,height=27)
        
        add = Button(app,text="ADD",bg='green',font=('Arisl Greek', 10,'bold'),command=Add)
        add.place(x=60,y=250,width=130)
        
        edite = Button(app,text="Edite",bg='#4F5A60',font=('Arisl Greek', 10,'bold'),command=Update)
        edite.place(x=220,y=250,width=130)
        
        updet = Button(app,text="Update",bg='#4F5A60',font=('Arisl Greek', 10,'bold'),command=Clear)
        updet.place(x=370,y=250,width=130)
        
        delete = Button(app,text="Delete",bg='red',font=('Arisl Greek', 10,'bold'),command=Delete)
        delete.place(x=520,y=250,width=130)
        
        work = Button(app,text="Work Window 📈📉",bg='#4F5A60',font=('Arisl Greek', 10,'bold'))
        work.place(x=670,y=250,width=130)
        
        
        
        fram = Frame(app,width=700,height=270)
        fram.place(x=4,y=380)
        """ image = Image.open('Designs/OIP.jpg')
        #iMAGE
        image = image.convert("RGBA")
        data = image.getdata()
        new_data = []
        for item in data:
            
            new_data.append((item[0], item[1], item[2], int(item[3] * 0.5)))
        
        image.putdata(new_data)
        new = ImageTk.PhotoImage(image)
        ma = Label(app, image=new,bg='#4F5A60')
        ma.place(x=200, y=65) """
        
        ##
        style=ttk.Style
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Tajawal', 9,'bold'), rowheight=50)
        style.configure("mystyle.Treeview.Heading", font=('Time New Roman', 13, 'bold'),anchor="w")
        
        tv = ttk.Treeview(fram, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), style="mystyle.Treeview")
        tv.heading("1",text="ID",anchor="w")
        tv.column("1",width=40 ,anchor="w")
        tv.heading("2",text="Lname",anchor="w")
        tv.column("2",width=95,anchor="w")
        tv.heading("3",text="Fname",anchor="w")
        tv.column("3",width=95,anchor="w")
        tv.heading("4",text="Age",anchor="w")
        tv.column("4",width=95,anchor="w")
        tv.heading("5",text="CIN",anchor="w")
        tv.column("5",width=90,anchor="w")
        tv.heading("6",text="JOB",anchor="w")
        tv.column("6",width=95,anchor="w")
        tv.heading("7",text="City",anchor="w")
        tv.column("7",width=70,anchor="w")
        tv.heading("8",text="PhoneN",anchor="w")
        tv.column("8",width=100,anchor="w")
        tv.heading("9",text="Email")
        tv.column("9",width=160)
        tv['show']='headings'
        tv.bind("<ButtonRelease-1>",getData)
        
        tv.pack()
        
        
        
        
        displayall()
        app.mainloop()
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