from pystyle import *
import webbrowser
import pwinput
from playsound import playsound
from gtts import gTTS
import emoji
import time

# Print a box with the specified text
print(Box.Lines('[+] Learn Python with Rakwan [+]'))

# Print a colored message
Write.Print('{+} This program is for a login page {+}\n\n', Colors.blue_to_cyan, interval=0.1)

# Print a double cube with the specified text
print(Box.DoubleCube('Example 1\n\n'))

# Define the welcome message
pl = 'Welcome Mr Abdo Bougrine'

# Get user input for username and password
name = input('Enter username: ')
password = pwinput.pwinput('Enter password: ')

# Check if the entered username and password match specific values
while True :
    if (name == 'moughit' or name == 'mohamed') and (password == '0614MM' or password == '22001122MM'):

    # Generate and save an audio file with the welcome message
        pll = gTTS(text=pl)
        pll.save('welcome.mp3')
    # Play the welcome audio
        playsound('welcome.mp3')
    # Print the welcome message
        Write.Print(pl, Colors.blue_to_cyan, interval=0.1)
        break
    else:

        print('You have a problem ')
        break

# Wait for user input before exiting
input('\n\n\nPress any key to exit ...')




