from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t=0
#z=0 #глобальная переменная всплывающего напоминания
music=False# при старте проекта музыка не играет
text = sd.askstring

def set():
    global text
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
            text = sd.askstring("текст напоминания", "введите текст напоминания")
            label.config(text=f"напоминание на {hour:02}:{minute:02} c текстом {text}")# :02 - это формат отображения времени 00:00
        except Exception as e:
            mb.showerror("ошибка!", f"произошла ошибка {e}")


def check():
    global text
    global t
    if t:
        now=time.time()# другая переменная now
        if now>=t:
            play_snd()
            mb.showinfo("напоминание", f"text")
            t=0
    window.after(10000, check)


def play_snd():
    global music
    music=True
    pygame.mixer.init()
    pygame.mixer.music.load("NataliaOreiro-AlasDeLibertad.mp3")
    pygame.mixer.music.play()# воспроизводим трек


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()#выключаем музыку
        music=False
    label.config(text="Установить новое напоминание")

window=Tk()
window.title("напоминание")
label=Label(text="установите напоминание", font=("Arial", 14))
label.pack(pady=5)
set_button=Button(text="установить напоминание", command=set, bg="yellow", fg="blue")
set_button.pack(pady=5)

stop_button=Button(text="остановить музыку", command=stop_music)
stop_button.pack(pady=5)


canvas=Canvas(width=400, height=60) #создаем холст
canvas.pack(pady=10)# отступ=10






check()

window.mainloop()