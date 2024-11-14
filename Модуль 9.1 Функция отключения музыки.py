from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t=0

def set():
    global t
    rem=sd.askstring("время напоминания","введите время напоминания в формате ЧЧ:ММ")
    if rem:
        try:
            hour = int(rem.split(":")[0])#берем первую часть
            minute = int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute, second=0)#музыка начнется сразу,без задержек, когда время наступит такое, какое мы указали в строке ввода
            print(dt)
            t=dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("ошибка!", f"произошла ошибка {e}")


def check():
    global t
    if t:
        now=time.time()# другая переменная now
        if now>=t:
            play_snd()
            t=0
    window.after(10000, check)


def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("NataliaOreiro-AlasDeLibertad.mp3")
    pygame.mixer.music.play()# воспроизводим трек


window=Tk()
window.title("напоминание")
label=Label(text="установите напоминание", font=("Arial", 14))
label.pack(pady=5)
set_button=Button(text="установить напоминание", command=set, bg="yellow", fg="blue")
set_button.pack(pady=15)

check()


window.mainloop()