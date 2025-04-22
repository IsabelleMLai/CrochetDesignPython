####### downloads to have:
    #rembg = strip image of background
    #simplegui = easily use pop up  windows

import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk



def MagicCircNumSt():
    #root window stays open for the whole application
    root = tk.Tk()
    root.title("Crochet Diagram")
    root.geometry('1920x1080')
    # root.withdraw()  # Hide the main window

    user_input = "1"
    while user_input is not None:
        user_input = simpledialog.askstring("Input", "Enter your value:")
        if user_input is not None:
            root.destroy() # Destroy the current window
            new_root = tk.Tk() # Create new window
            new_root.title("Crochet Diagram")
            new_root.geometry('1920x1080')
            label = ttk.Label(new_root, text="This is the new window")
            label.pack(pady=20)
            root = new_root
            print("You entered:", user_input)

            try:
                image = Image.open("./Images_clear/DC_clear.png")  # Replace "your_image.jpg" with the actual path to your image file
                photo = ImageTk.PhotoImage(image)
            except FileNotFoundError:
                print("Error: Image file not found.")
                root.destroy()
                exit()

            # Create a Label widget to display the image
            image_label = tk.Label(root, image=photo)
            image_label.pack()

            # Keep a reference to the image object to prevent garbage collection
            image_label.image = photo



        else:
            print("You cancelled the input.")

        