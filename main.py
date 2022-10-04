import time
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
from tkinter import messagebox


def start():

    try:
        time_to_work = int(var.get().split(' ')[0])
    except ValueError:
        text_label.grid(column=1, row=1)
    else:
        temp = time_to_work * 60
        start_timer = time.time()
        combo.pack_forget()
        start_btn.grid_forget()

        try:
            text_label.grid_forget()
        finally:
            warning_label = Label(window, text=f"You have {var.get()} to write, "
                                               f"if you stop for 5 seconds everything will be lose.", fg='red')
            warning_label.grid(columnspan=2, column=0, row=0, pady=10)
            entry_label.grid(columnspan=2, column=0, row=1)

        circle = 0
        saved_circle = 0
        saved_entry = ''
        saved = True

        while time.time() - start_timer < temp:
            saved_entry_inside = entry.get()
            window.update()
            time.sleep(0.25)

            if saved_entry_inside == entry.get() and saved:

                saved_entry = entry.get()
                saved_circle = circle
                saved = False

            if saved_entry != entry.get():

                saved = True

            if saved_circle + 5 == circle:

                if saved_entry == entry.get():

                    res = messagebox.askquestion("Game Over", "You don't write fast enough. \n "
                                                              "Would you like to try again?")

                    if res == "yes":
                        warning_label.grid_forget()
                        entry_label.grid_forget()

                        frame.grid(column=1, row=0)
                        combo.pack()
                        start_btn.grid(column=1, row=2)
                    elif res == "no":
                        window.destroy()

                    break

            circle += 0.25


window = Tk()
window.title('Disappearing Text Writing App')
window.config(pady=50, padx=50)

frame = Frame(window)
frame.grid(column=1, row=0)

vlist = ["1 minute", "2 minutes", "3 minutes", "4 minutes", "5 minutes"]

var = StringVar()
combo = ttk.Combobox(frame, values=vlist, textvariable=var)
combo.set('Pick your time')
combo.pack()

image = Image.open('images/Start-Button.png')
resized = image.resize((325, 200), Image.LANCZOS)
image_new = ImageTk.PhotoImage(resized)
start_btn = Button(window, image=image_new, borderwidth=0, command=start)
start_btn.grid(column=1, row=2)

text_label = Label(window, text="Pick tour time first!", fg="red")

entry = StringVar()
entry_label = Entry(window, textvariable=entry, width=50)


window.mainloop()
