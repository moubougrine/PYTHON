from customtkinter import *

root=CTk()
root.geometry('810x680')
root.title("Employe Program")
root.resizable(width=False,height=False)
set_appearance_mode("dark")

tabview = CTkTabview(root,width=780,height=670,fg_color='thistle')
tabview.pack(padx=1,pady=1)
tabview.add("Fram 1")
tabview.add("Frame 2")

#fram=CTkFrame(tabview,border_color='red',width=790,height=660).place(x=10,y=10)
#ss=CTkLabel(master=tabview.tab("Fram 1"),text="Insert Data 🖋📊",text_color='#FF00CC',font=('Tajawal', 40,'bold')).place(relx=0.32,rely=0)

name = CTkLabel(tabview.tab("Fram 1"),text="~📎Name ", text_color='black',font=('Arisl Greek', 20))
name.place(x=8,y=80)
#e_name=CTkEntry(tabview.tab("Fram 1"),border_color="#F3904F",fg_color=4'thistle',text_color='black',font=('Arisl Greek', 16),width=150).place(x=90,y=80)
Cityy = CTkLabel(master=tabview.tab("Fram 1"),text="~📎City ",text_color=('black'),font=('Arisl Greek', 20))
Cityy.place(x=245,y=80)
e_Cityy=CTkEntry(master=tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=150)
e_Cityy.place(x=310,y=80)

dTYPE = CTkLabel(tabview.tab("Fram 1"),text="~📎DeliveryType ",text_color=('black'),font=('Arisl Greek', 20)).place(x=475,y=80)
e_dtype=CTkEntry(tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=150).place(x=620,y=80)

cN = CTkLabel(tabview.tab("Fram 1"),text="~📎CategoryName ", text_color=('black'),font=('Arisl Greek', 20))
cN.place(x=2,y=135)
e_cn=CTkEntry(tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=150)
e_cn.place(x=160,y=135)

Ctype = CTkLabel(tabview.tab("Fram 1"),text="~📎CategoryType ",text_color=('black'),font=('Arisl Greek', 20)).place(x=320,y=135)
e_Ctype=CTkComboBox(tabview.tab("Fram 1"),text_color=('black'),values=["option1","option2","optioh3"],font=('Arisl Greek', 20),width=150).place(x=470,y=135)

Num = CTkLabel(tabview.tab("Fram 1"),text="~📎N%",text_color=('black'),font=('Arisl Greek', 20)).place(x=630,y=135)
e_Num=CTkEntry(tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=75).place(x=690,y=135)

name = CTkLabel(tabview.tab("Fram 1"),text="~📎~~~ ", text_color='black',font=('Arisl Greek', 20)).place(x=6,y=200)
e_name=CTkEntry(master=tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=150).place(x=90,y=200)
Cityy = CTkLabel(master=tabview.tab("Fram 1"),text="~📎`````` ",text_color=('black'),font=('Arisl Greek', 20)).place(x=245,y=200)
e_Cityy=CTkEntry(master=tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=150).place(x=310,y=200)
dTYPE = CTkLabel(tabview.tab("Fram 1"),text="~📎~~~~~~ ",text_color=('black'),font=('Arisl Greek', 20)).place(x=475,y=200)
e_dtype=CTkEntry(tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=150).place(x=620,y=200)

search = CTkButton(master=tabview.tab("Fram 1"),text="Search 🔍",text_color='black',font=('Tajawal',13,'bold'),corner_radius=10,fg_color="transparent",hover_color="#000C40",border_color="#F3904F",border_width=2).place(relx=0.18,rely=0.53)
e_search=CTkEntry(tabview.tab("Fram 1"),text_color='black',font=('Arisl Greek', 16),width=400,border_color="#F3904F").place(x=300,rely=0.53)

add = CTkButton(master=tabview.tab("Fram 1"),text="ADD",text_color='black',font=('Tajawal',13,'bold'),corner_radius=10,fg_color="transparent",hover_color="#67B25F",border_color="#F3904F",border_width=2).place(relx=0.035,rely=0.450)

edite = CTkButton(master=tabview.tab("Fram 1"),text="EDIT",text_color='black',font=('Tajawal',13,'bold'),corner_radius=10,fg_color="transparent",hover_color="#F3904F",border_color="#F3904F",border_width=2).place(relx=0.3,rely=0.450)

updet = CTkButton(master=tabview.tab("Fram 1"),text="CLEAR",text_color='black',font=('Tajawal',13,'bold'),corner_radius=10,fg_color="transparent",hover_color="black",border_color="#F3904F",border_width=2).place(relx=0.55,rely=0.450)
delete = CTkButton(master=tabview.tab("Fram 1"),text="DELETE",text_color='black',font=('Tajawal',13,'bold'),corner_radius=10,fg_color="transparent",hover_color="red",border_color="#F3904F",border_width=2).place(relx=0.8,rely=0.450)


root.mainloop()