import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk

from Back_end_code.PrepareImage import *
import math

#get the number of pixels the circumference of the magic circle is
#ARGS:
    #num_st =  number of stitches in the magic circle
    #image_path = path of image to use
def GetCircumf_MagicCirc(num_st, image_path):
    image = Image.open(image_path)
    width, height = image.size

    #because image is centered, width = widest part of that stitch image
        # =should be the circumference of the magic circle
    circum1 = num_st * width
    #if image is really long/tall in one dimension, might need to use a difference
        #circumference calculation
    circum2 = 2*height+width
    circumference = circum1
    if circum1 < circum2:
        circumference = circum2
    return circumference

    
# def GetAngles_MagicCircle(num_st, image_path):




#display the final magic circle on a pop  up window
def ShowMagicCirc(num_st):
    window = tk.Tk() # Create new window
    window.title("Crochet Diagram")
    window.geometry('1920x1080')
    
    image_path = "./Images_center/DC_center.png"
    circumf = GetCircumf_MagicCirc(num_st, image_path)
    print(circumf)

    # image = Image.open("./Images_center/DC_center.png")  # Replace "your_image.jpg" with the actual path to your image file
    # photo = ImageTk.PhotoImage(image)
    
    # # Create a Label widget to display the image
    # image_label = tk.Label(window, image=photo)
    # image_label.pack()

    # # Keep a reference to the image object to prevent garbage collection
    # image_label.image = photo

    # window.mainloop()

