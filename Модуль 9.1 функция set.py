from gc import set_debug
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set():
    rem=sd.askstring("время напоминания","введите время напоминания в формате ЧЧ:ММ")
    if rem:
        try:
            hour = int(rem.split(":")[0])#берем первую часть
            minute=int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute)
            print(dt)
            t=dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("ошибка!", f"произошла ошибка {e}")


window=Tk()
window.title("напоминание")
label=Label(text="установите напоминание")
label.pack(pady=10)
set_button=Button(text="установить напоминание", command=set)
set_button.pack()

window.mainloop()