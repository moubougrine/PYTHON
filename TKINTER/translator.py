from googletrans import Translator, LANGUAGES
from tkinter import *
from tkinter import ttk

def change(text = "type",src="English",dest = "Hindi"):
    text1=text
    src1 = src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb1.get()
    d = comb2.get()
    masg = sor_Txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    sor_Txt2.delete(1.0,END)
    sor_Txt2.insert(END,textget)




root = Tk()
root.title("TRANSLSTOR")

root.geometry("500x600")
root.resizable(width=False,height=False)
root.config(bg='#f5f5f5')

lab_text = Label(root, text="🌐 Language Translator", font=('Helvetica', 20, 'bold'), bg='#f5f5f5', fg='#4A90E2')
lab_text.place(x=50,y=10,height=50,width=400)

frame = Frame(root).pack(side=BOTTOM)

lab_text = Label(frame, text="Source Text", font=('Arial', 14), bg='#ffffff')
lab_text.place(x=100,y=70,height=30,width=300)

sor_Txt = Text(frame, font=('Arial', 12), bg="#e8f0fe", wrap=WORD)
sor_Txt.place(x=10,y=110,height=200,width=480)

list_text = list(LANGUAGES.values())
comb1 = ttk.Combobox(frame,value=list_text)
comb1.place(x=10,y=320,height=25,width=150)
comb1.set("English")

button_chang = Button(frame,text="Translate",relief=RAISED,bg='#4A90E2',command=data)
button_chang.place(x=165,y=320,height=25,width=180)

comb2 = ttk.Combobox(frame,value=list_text)
comb2.place(x=350,y=320,height=25,width=140)
comb2.set("English")

lab_text = Label(root,text="Dest Text",font=('Arial', 14), bg='#ffffff')
lab_text.place(x=100,y=350,height=30,width=300)

sor_Txt2= Text(frame, font=('Arial', 12), bg="#e8f0fe", wrap=WORD)
sor_Txt2.place(x=10,y=390,height=200,width=480)



root.mainloop()
""" from googletrans import Translator, LANGUAGES
from tkinter import *
from tkinter import ttk

def change(text = "type",src="English",dest = "Hindi"):
    text1=text
    src1 = src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb1.get()
    d = comb2.get()
    masg = sor_Txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    sor_Txt2.delete(1.0,END)
    sor_Txt2.insert(END,textget)



root = Tk()
root.title("Modern Translator")
root.geometry("700x550")
root.resizable(False, False)
root.config(bg='#f5f5f5')

# عنوان التطبيق
title_label = Label(root, text="🌐 Language Translator", font=('Helvetica', 26, 'bold'), bg='#f5f5f5', fg='#4A90E2')
title_label.pack(pady=30)

# إطار للمدخلات
frame = Frame(root, bg='#ffffff', padx=20, pady=20, bd=2, relief=GROOVE)
frame.pack(pady=20)

# نص المصدر
source_label = Label(frame, text="Source Text", font=('Arial', 14), bg='#ffffff')
source_label.grid(row=0, column=0, sticky=W)

sor_Txt = Text(frame, font=('Arial', 12), bg="#e8f0fe", wrap=WORD, height=10, width=50)
sor_Txt.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# قوائم اللغات
list_text = list(LANGUAGES.values())
comb1 = ttk.Combobox(frame, value=list_text, width=20)
comb1.grid(row=2, column=0, padx=10, pady=5)
comb1.set("English")

comb2 = ttk.Combobox(frame, value=list_text, width=20)
comb2.grid(row=2, column=1, padx=10, pady=5)
comb2.set("Hindi")

# زر الترجمة
button_chang = Button(frame, text="Translate", relief=RAISED, command=data, bg='#4A90E2', fg='white', font=('Arial', 14))
button_chang.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# نص الهدف
dest_label = Label(frame, text="Translated Text", font=('Arial', 14), bg='#ffffff')
dest_label.grid(row=4, column=0, sticky=W)

sor_Txt2 = Text(frame, font=('Arial', 12), bg="#e8f0fe", wrap=WORD, height=10, width=50)
sor_Txt2.grid(row=5, column=0, padx=10, pady=10, columnspan=2)



root.mainloop() """