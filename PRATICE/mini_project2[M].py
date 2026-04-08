# A BASIC CLOCK
import tkinter as tk # for allowing th edisplay positioning and buikding the widgets
from time import strftime#convert the structred time object into the formated strings

root = tk.Tk()#to create or manage the main applocation window or the root window
root.title('Digital Clock')

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root,font=('latin',45,'bold'),background='cyan',foreground='black',border=10,borderwidth=10)
label.pack(anchor='center')# aligns in the center of the windows
time()
root.mainloop()


