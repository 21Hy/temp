from tkinter import *

def slide(event):
    num = en1.get() # Get whatever is entered in the entry
    if num.isdigit(): # Checks if it is an integer
        num = int(num) # Convert string to integer
        # Change the values on the scale
        C1.set(num) # Why no if statement?? Automatically snaps to the max or min value
        # Optional at the bottom if you also want the value in the entry changed:
        # on_change(None)

def on_change(event): # Change the value of entry
    en1.delete(0, END)
    en1.insert(0, C1.get())

win=Tk()
win.geometry('1000x550')

C1 = IntVar()
C1.set(250) # Sets the value of the scale
en1 = Entry(win, width=10)
en1.place(x=67, y=60)
en1.insert(0, "250") # Setting the value of the entry
sc1 = Scale(win, from_=100, to=530, length=200, variable = C1, resolution = 1, orient = 'horizontal')
sc1.place(x=300, y=40)

# Use bindings individually
en1.bind("<KeyRelease>", slide) # This sends an event to the slide function whenever you type something in the entry
sc1.bind("<ButtonRelease-1>", on_change) # This sends an event to the on_change function whenever you change the value on the scale

win.mainloop()