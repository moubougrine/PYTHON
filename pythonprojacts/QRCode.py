import pyqrcode
import os
from PIL import Image
from pystyle import *

print(Box.Lines("This program for convert to QrCode"))
Qr=Write.Input("Enter what you want to convert to Qrcode : " , Colors.blue_to_cyan,interval=0)
p=pyqrcode.create(Qr)
p.png('Qrcode.png',scale=15)
Image.open('Qrcode.png')