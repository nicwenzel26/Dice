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
heading = tkinter.Label(root, text='Roll the Dice!', fg = 'black', bg = 'light blue', font = 'Helvetica 20 bold')
heading.pack()

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# Selecting a random image to display on screen
dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Constructing a label widget for the image
image_label = tkinter.Label(root, image= dice_image)
image_label.image = dice_image

image_label.pack(expand = True)

# This keeps the windo open
root.mainloop()