import tkinter as tk
import time
from PIL import Image, ImageTk

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %B %d, %Y")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, update_clock)  


root = tk.Tk()
root.title("Digital Clock")


background_image = Image.open("background_img.jpg")  
background_image = background_image.resize((800, 600), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)


canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")


clock_label = tk.Label(root, font=("Helvetica", 48, "bold"), fg="cyan", bg="black")
clock_label.place(relx=0.5, rely=0.4, anchor="center") 


date_label = tk.Label(root, font=("Helvetica", 24), fg="white", bg="black")
date_label.place(relx=0.5, rely=0.5, anchor="center") 

update_clock()  


def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)
root.mainloop()
