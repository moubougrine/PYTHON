from customtkinter import *
from PIL import Image
from tkinter import messagebox
from customtkinter import CTk, CTkImage, CTkLabel
from tkinter import ttk
import cv2
import os
from datetime import datetime
import sqlite3

class Databs:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS LUXCAFTANBASE (
            id INTEGER PRIMARY KEY,
            date TEXT,
            CIN TEXT TEXT,
            e_number TEXT,
            lname TEXT,
            Days INTEGER,
            Price INTEGER,
            adress TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, date, CIN, e_number, lname, Days, price, adress):
        self.cur.execute("INSERT INTO LUXCAFTANBASE (date, CIN, e_number, lname, Days, price, adress) VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (date, CIN, e_number, lname, Days, price, adress))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM LUXCAFTANBASE")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM LUXCAFTANBASE WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, date, CIN, e_number, lname, Days, price, adress):
        self.cur.execute("UPDATE LUXCAFTANBASE SET date=?, CIN=?, e_number=?, lname=?, Days=?, price=?, adress=? WHERE id=?",
                         (date, CIN, e_number, lname, Days, price, adress, id))
        self.con.commit()

    def Searcho(self, CIN):
        self.cur.execute("SELECT * FROM LUXCAFTANBASE WHERE CIN=?", (CIN,))
        return self.cur.fetchall()

    def close(self):
        self.con.close()

root = CTk()
root.geometry('500x600')
root.title("LUX CAFTAN LOGING")
root.resizable(width=False, height=False)
set_appearance_mode('dark')
img = Image.open(r'\Projact\\images\\lux.jpeg') 
img_tk = CTkImage(light_image=img,size=(500,600))
img_label = CTkLabel(root, image=img_tk)
img_label.place(x=0, y=0)

fram =CTkFrame(root,width=260,height=140,
        corner_radius=22,
        bg_color='#c9cad1',
        fg_color='#d19e8a').place(x=115,y=240)
name=CTkLabel(fram,text="𝐿𝒰𝒳 𝒞𝒜𝐹𝒯𝒜𝒩 𝒜𝒟𝑀𝐼𝒩",
        bg_color='#d19e8a',
        font=('Tajawal',25)).place(x=135,y=240)
e_name = CTkEntry(fram, bg_color='#d19e8a', text_color='black', 
                  corner_radius=32, fg_color='#c9cad1', 
                  border_color='#d19e8a', font=('Tajawal', 16), width=150)
e_name.place(x=220, y=270)

p_name = CTkEntry(fram, bg_color='#d19e8a', show="*", 
                  text_color='black', corner_radius=32, 
                  fg_color='#c9cad1', border_color='#d19e8a', 
                  font=('Tajawal', 16), width=150)
p_name.place(x=220, y=300)
lablname=CTkLabel(fram,text="UserName",bg_color='#d19e8a',
        font=('Tajawal',17)).place(x=125,y=270)
lablPas=CTkLabel(fram,text="Password",bg_color='#d19e8a',
        font=('Tajawal',17)).place(x=125,y=300)


def Red():
    password = p_name.get() 
    pas = e_name.get()
    if password == "admin" and pas=="admin": 
        p_name.delete(0,END)
        e_name.delete(0,END)
        messagebox.showinfo('Hi',"Hello man how are you ")
        root.geometry('900x700')
        img = Image.open('\Projact\\images\\\luux.jpg') 
        img_tk = CTkImage(light_image=img, size=(500, 700))
        # Create a label to hold the image
        img_label = CTkLabel(root,text="", image=img_tk)
        img_label.place(x=0, y=0)
        fram= CTkFrame(root,fg_color='#c9cad1',width=400,height=600)
        fram.place(x=500,y=0)
        fram1= CTkFrame(root,fg_color='#6da177',bg_color='#6da177',width=420,height=600)
        fram1.place(x=500,y=535)
  
        db=Databs(r'\Projact\data\LUXbase.db')

        date=StringVar()
        cin=StringVar()
        name=StringVar()
        number=StringVar()
        day=StringVar()
        prix=StringVar()
        adress=StringVar()
        search=StringVar()


        def delete():
            db.remove(row[0])
            clear()
            displayall()
        def getData(event):
                select_row = tv.focus()
                data = tv.item(select_row)
                global row
                row = data['values']
                date.set(row[1])
                cin.set(row[2])
                number.set(row[3])
                name.set(row[4]) 
                day.set(row[5])
                prix.set(row[6])
                adress.set(row[7])
                displayall()

        def displayall():
            tv.delete(*tv.get_children())
            for row in db.fetch() :
                tv.insert("",END,values=row)

        def clear():
                date.set("")
                cin.set("")
                name.set("")
                number.set("")
                day.set("")
                prix.set("")
                adress.set("")

        def Rred():
              iim=adress.get()
              img=cv2.imread(iim)
              cv2.imshow('LUX CAFTAN',img)
              cv2.waitKey(0)

        def Open():
                file = filedialog.askopenfile(mode='rb',filetypes=[('files','*.jpg'),
                                                                   ('files','*.png'),
                                                                   ('files','*.jpeg')])

                if file:
                        filepath = os.path.abspath(file.name)
                        dirctoryNam = os.path.dirname(filepath)
                        filename = os.path.basename(filepath) 
                        adress.set("")
                        adress.set(f"{dirctoryNam}\\{filename}")

        def Add():
            if  cin.get() == ""or number.get() == ""or name.get()== ""or prix.get() == "":
                    messagebox.showerror("ERROR","Plese Fill all the Entry")
                    return
            date_format =  "%d-%m-%Y"
            time = date.get()
            if time== "":
                date.set(datetime.today().strftime(date_format))
            db.insert(
                date.get(),
                cin.get(),
                number.get(),  
                name.get(),
                day.get(),
                prix.get(),
                adress.get()
            )
            clear()
            displayall()
        def Search():
            search_value = search.get().strip()

            if search_value:
                tv.delete(*tv.get_children())

                search_results = db.Searcho(search_value)
                for row in search_results:
                    tv.insert("", "end", values=row)

                search.set("")

                if not search_results:
                    displayall()
            else:
                displayall()

        def Update():
                if date.get() == "" or cin.get() == ""or number.get() == ""or name.get()== ""or prix.get() == "":
                    messagebox.showerror("ERROR","Plese Fill all the Entry")
                    return
                db.update(row[0],
                        date.get(),
                        cin.get(),
                        number.get(),  
                        name.get(),
                        day.get(),
                        prix.get(),
                        adress.get()
                )
                clear()
                displayall()

            
        tr=CTkTabview(fram,width=380,height=245,fg_color='#6da177',corner_radius=30)
        tr.pack(padx=10,pady=10)
        ldate=CTkLabel(tr,text="Date : ",font=('tajawal',16,'bold')).place(x=20,y=20)
        e_date=CTkEntry(tr,bg_color='#6da177',textvariable=date,
                text_color='black',
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=250).place(x=90,y=50)

        lcin=CTkLabel(tr,text="CIN   : ",font=('tajawal',16,'bold')).place(x=20,y=80)
        e_cin=CTkEntry(tr,bg_color='#6da177',textvariable=cin,
                text_color='black',
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=250).place(x=90,y=100)

        lnumber=CTkLabel(tr,text="PhoneNumber : ",font=('tajawal',16,'bold')).place(x=20,y=130)
        e_number=CTkEntry(tr,bg_color='#6da177',textvariable=number,
                text_color='black',
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=250).place(x=90,y=160)
        
        lname=CTkLabel(tr,text="Name : ",font=('tajawal',16,'bold')).place(x=20,y=185)
        ename=CTkEntry(tr,bg_color='#6da177',textvariable=name,
                text_color='black',
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=250).place(x=90,y=210)

        style = ttk.Style()
        style.theme_use("clam")  # نقدر نخليها أو نبدلها بـ "alt", "default", الخ

# خلفية عامة خفيفة وتكست واضح
        style.configure("Custom.Treeview",
                background="#f9f9f9",
                foreground="#333333",
                rowheight=45,
                fieldbackground="#f9f9f9",
                font=('Segoe UI', 10))

# رأس الجدول – لون جذاب وغامق، مع خط أنيق
        style.configure("Custom.Treeview.Heading",
                background="#4a7a8c",
                foreground="white",
                font=('Segoe UI Semibold', 12),
                relief="flat")

# border & selected row
        style.map("Custom.Treeview",
          background=[("selected", "#c0e4ff")],
          foreground=[("selected", "#000000")])

# إنشاء Treeview باستعمال الستايل
        tv = ttk.Treeview(fram1, columns=(1, 2, 3, 4, 5, 6, 7), style="Custom.Treeview")

        tv.heading("1", text="ID", anchor="w")
        tv.column("1", width=50, anchor="w")

        tv.heading("2", text="Date", anchor="w")
        tv.column("2", width=80, anchor="w")
        
        tv.heading("3", text="CIN", anchor="w")
        tv.column("3", width=90, anchor="w")
        
        tv.heading("4", text="Number", anchor="w")
        tv.column("4", width=100, anchor="w")
        
        tv.heading("5", text="Name", anchor="w")
        tv.column("5", width=120, anchor="w")
        
        tv.heading("6", text="Day", anchor="w")
        tv.column("6", width=60, anchor="w")
        
        tv.heading("7", text="Prix", anchor="w")
        tv.column("7", width=70, anchor="w")
        
        tv['show'] = 'headings'
        tv.tag_configure("colored", foreground="#1a73e8")
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill="both", expand=True)
        
                
        
        

        tr2=CTkTabview(fram,width=380,height=260,fg_color='#6da177',corner_radius=30)
        tr2.pack(padx=10,pady=12)

        lday=CTkLabel(tr2,text="Days : ",font=('tajawal',16,'bold')).place(x=20,y=20)
        e_day=CTkEntry(tr2,bg_color='#6da177',textvariable=day,
                text_color='black',
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=100).place(x=80,y=50)

        lprix=CTkLabel(tr2,text="Prix   : ",font=('tajawal',16,'bold')).place(x=200,y=20)
        e_prix=CTkEntry(tr2,bg_color='#6da177',textvariable=prix,
                text_color='black',
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=100).place(x=250,y=50)

        ladress=CTkLabel(tr2,text="LUX CAFTAN : ",font=('tajawal',16,'bold')).place(x=20,y=85)
        e_adress=CTkEntry(tr2,bg_color='#6da177',textvariable=adress,
                text_color='black',
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=250).place(x=40,y=110)
        OpeN=CTkButton(tr2,text="Open",
                       text_color='black',
                       font=('Tajawal',13,'bold'),
                       corner_radius=10,bg_color='#6da177',
                       fg_color="#e3d496",
                       hover_color="green",
                       border_color="#6da177",
                       border_width=2,width=80,command=Open).place(x=290,y=90)
        red=CTkButton(tr2,text="Read",
               text_color='black',
               font=('Tajawal',13,'bold'),
               corner_radius=10,bg_color='#6da177',
               fg_color="#e3d496",
               hover_color="green",
               border_color="#6da177",
               border_width=2,width=80,command=Rred).place(x=290,y=125)
        e_search=CTkEntry(tr2,bg_color='#6da177',
                text_color='black',textvariable=search,
                corner_radius=32,
                fg_color='#c9cad1',
                border_color='#6da177',
                font=('Tajawal',14),width=250).place(x=40,y=170)
        searrch=CTkButton(tr2,text="Search",
                       text_color='black',
                       font=('Tajawal',13,'bold'),
                       corner_radius=10,bg_color='#6da177',
                       fg_color="#e3d496",
                       hover_color="green",
                       border_color="#6da177",
                       border_width=2,width=80,command=Search).place(x=290,y=170)
        add=CTkButton(tr2,text="Add",
                       text_color='black',
                       font=('Tajawal',13,'bold'),
                       corner_radius=10,bg_color='#6da177',
                       fg_color="#498f5d",
                       hover_color="green",
                       border_color="#6da177",
                       border_width=2,width=110,command=Add).place(x=5,y=200)

        Edit=CTkButton(tr2,text="Edit",
                       text_color='black',
                       font=('Tajawal',13,'bold'),
                       corner_radius=10,bg_color='#6da177',
                       fg_color="#498f5d",
                       hover_color="#12373d",
                       border_color="#6da177",
                       border_width=2,width=110,command=Update).place(x=136,y=200)

        Delete=CTkButton(tr2,text="Delete",
                       text_color='black',
                       font=('Tajawal',13,'bold'),
                       corner_radius=10,bg_color='#6da177',
                       fg_color="#498f5d",
                       hover_color="red",
                       border_color="#6da177",
                       border_width=2,width=110,command=delete).place(x=265 ,y=200)
        Clear=CTkButton(tr2,text="Clear",
                       text_color='black',
                       font=('Tajawal',13,'bold'),
                       corner_radius=10,bg_color='#6da177',
                       fg_color="#498f5d",
                       hover_color='#6da177',
                       border_color="#6da177",
                       border_width=2,width=110,command=clear).place(x=135 ,y=229)
        displayall()
    else:
        messagebox.showerror("Your password or Name is incorect")
def Res():
        root.destroy()

add = CTkButton(fram,text="Loging",text_color='#c9cad1',font=('Tajawal',13,'bold'),corner_radius=10,bg_color='#d19e8a',fg_color="#d19e8a",hover_color="green",border_color="#d19e8a",border_width=2,width=100,command=Red).place(x=240,y=340)
rest = CTkButton(fram,text="Rest",text_color='#c9cad1',font=('Tajawal',13,'bold'),corner_radius=10,bg_color='#d19e8a',fg_color="#d19e8a",hover_color="red",border_color="#d19e8a",border_width=2,width=100,command=Res).place(x=130,y=340)
root.bind('<Return>', lambda event: Red())


import os
import sys

def resource_path(relative_path):              
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    
image_path = resource_path(r'\Projact\\images\\luux.jpg')
image_path = resource_path(r'\Projact\\images\\lux.jpeg')
data_path = resource_path(r'\Projact\\LUXbase.db')

root.mainloop()