from tkinter import *
from PIL import ImageTk, Image
import cv2

root=Tk()

root.geometry('810x700')
root.title("Employe Program")
root.resizable(width=False,height=False)
image = Image.open('Designs/image.jpeg')
#iMAGE
image = image.convert("RGBA")
data = image.getdata()
new_data = []
for item in data:
    new_data.append((item[0], item[1], item[2], int(item[3] * 0.5)))
image.putdata(new_data)
new = ImageTk.PhotoImage(image)
ma = Label(root, image=new,bg='#4F5A60')
ma.place(x=0, y=0)

ss=Label(root,text="Insert Data 🖋📊",bg='#000000',fg='white',font=('Tajawal', 20,'bold')).place(x=0,y=0,width=810,height=40)

name = Label(root,text="~📎Name ",bg=root.cget("bg"), fg="black",font=('Arisl Greek', 10,'bold'))
name.place(x=15,y=80)
e_name=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_name.place(x=90,y=80,width=170,height=23)

Cityy = Label(root,text="~📎City ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
Cityy.place(x=260,y=80)
e_Cityy=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_Cityy.place(x=320,y=80,width=170,height=23)

aage = Label(root,text="~📎DeliveryType ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
aage.place(x=500,y=80)
e_age=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_age.place(x=620,y=80,width=170,height=23)


cinn = Label(root,text="~📎CategoryName ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
cinn.place(x=15,y=120)
e_cin=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_cin.place(x=140,y=120,width=250,height=23)

jobb = Label(root,text="~📎CategoryType ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
jobb.place(x=390,y=120)
e_job=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_job.place(x=505,y=120,width=170,height=23)

jobb = Label(root,text="~📎N%",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
jobb.place(x=680,y=120)
e_job=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_job.place(x=725,y=120,width=65,height=23)

number = Label(root,text="~📎CategoryPrice",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
number.place(x=60,y=155)
e_number=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_number.place(x=185,y=155,width=120,height=23)

email = Label(root,text="~📎Email ",bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
email.place(x=320,y=155)
e_email=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold'))
e_email.place(x=445,y=155,width=210,height=23)

search = Button(root,text="Search",bg='#4F5A60',font=('Arisl Greek', 10,'bold')).place(x=570,y=295,width=170)
e_search=Entry(root,bg='#6A6A6A',font=('Arisl Greek', 10,'bold')).place(x=150,y=295,width=400,height=27)

add = Button(root,text="ADD",bg='green',font=('Arisl Greek', 10,'bold'))
add.place(x=60,y=250,width=130)

edite = Button(root,text="Edite",bg='#4F5A60',font=('Arisl Greek', 10,'bold'))
edite.place(x=220,y=250,width=130)

updet = Button(root,text="Update",bg='#4F5A60',font=('Arisl Greek', 10,'bold'))
updet.place(x=370,y=250,width=130)

delete = Button(root,text="Delete",bg='red',font=('Arisl Greek', 10,'bold'))
delete.place(x=520,y=250,width=130)

work = Button(root,text="Work Window 📈📉",bg='#4F5A60',font=('Arisl Greek', 10,'bold'))
work.place(x=670,y=250,width=130)



fram = Frame(root,bg=('#F4C4F3'),width=804,height=315)
fram.place(x=4,y=380)

root.mainloop()