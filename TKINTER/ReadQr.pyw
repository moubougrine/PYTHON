import pyttsx3
from tkinter import *
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog
import os
from tkinter import messagebox

fram = Tk()
fram.title("Read Qr")
fram.geometry("300x400")
fram.resizable(False, False)

def Open():
    file = filedialog.askopenfile(mode='rb',
                                  filetypes=[
                                      ('files', '*.jpg'),
                                      ('files', '*.png')])
    if file:
        filepath = os.path.abspath(file.name)
        dirctoryNam = os.path.dirname(filepath)
        filename = os.path.basename(filepath) 
        entry1.delete(0, END) 
        entry1.insert(0, f"{dirctoryNam}\\{filename}")

def RAad():
    d = entry1.get()
    print("Image path:", d)  
    if not os.path.exists(d):
        messagebox.showerror("Error", "File not found!")
        return

    res = cv2.QRCodeDetector()
    image = cv2.imread(d)
    
    if image is None:
        messagebox.showerror("Error", "Unable to read the image.")
        return
    
    val, points, s_qr = res.detectAndDecode(image)
    
    if val:
        messagebox.showinfo('Qr-Scan', val)
    else:
        messagebox.showerror('Qr-Scan', 'No QR code found or image is invalid.')


image = Image.open('Designs/image.jpeg')
new = ImageTk.PhotoImage(image)
ma = Label(fram, image=new)
ma.place(x=0, y=2, width=300, height=400)

labl = Label(fram, text="Qrcode line", font=('Tajwal', 10), fg='white', bg='black')
labl.place(x=50, y=10, width=200, height=25)

entry1 = Entry(fram, font=('Tajwal', 7))
entry1.place(x=10, y=40, width=280, height=30)

sel_butt = Button(fram, text="Select Qrcode", font=('Tajawal', 16), bg='green', command=Open)
sel_butt.place(x=50, y=80, width=200)

read_butt = Button(fram, text="Read Qrcode", font=('Tajawal', 16), bg='cyan', command=RAad)
read_butt.place(x=50, y=130, width=200)

fram.mainloop()
