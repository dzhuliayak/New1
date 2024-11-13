from gc import set_debug
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

window=Tk()
window.title("напоминание")
label=Label(text="установите напоминание")
label.pack(pady=10)
set_button=Button(text="установить напоминание", command=set)
set_button.pack()

window.mainloop()

