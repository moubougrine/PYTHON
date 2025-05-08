from customtkinter import *

root=CTk()
root.geometry('600x500')
root.title("Employe Program")
root.resizable(width=False,height=False)
set_appearance_mode("dark")

tabview=CTkTabview(master=root,width=590,height=490)
tabview.pack(padx=1,pady=1)
tabview.add("Frame 1")
tabview.add("Frame 2")



root.mainloop()