import tkinter
from PIL import Image, ImageTk 
import random

# Widgit that represents the main window for the application
root = tkinter.Tk("Test screen")
root.title('Dice Rolling')
# Setting the screen size in px
root.geometry('400x400')

blankline = tkinter.Label(root, text='')
blankline.pack()

# Adding a header in the box
Heading = tkinter.Label(root, text='Roll the Dice!', fg = 'black', bg = 'light blue', font = 'Helvetica 20 bold')
Heading.pack()


# This keeps the windo open
root.mainloop()