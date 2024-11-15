from cProfile import label
from tkinter import*
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import ttk, Label

from bottle import response
from pygame.examples.cursors import image


def show():
    global img
    #progr.stop
    image=get_link_dogs()
    if image:
        response=requests.get(image)
        img_data=BytesIO(response.content)
        img=Image.open(img_data)

        w=int(w_spinbox.get())
        h=int(h_spinbox.get())

        img.thumbnail((w,h))

        img=ImageTk.PhotoImage(img)
        label.config(image=img)
        #window.image=img

def get_link_dogs():
    try:
        response=requests.get(ur1)
        response.raise_for_status()
        print(response)
        data=response.json()
        print(data)
        return data["message"]
    except Exception as err:
        print(f"произошла ошибка {err}")


'''def progress():
    progr.config(value=0)
    prog.start(30)
    window.after(3000, show)'''

ur1="https://dog.ceo/api/breeds/image/random"

window=Tk()
window.title("собачки")
window.geometry("400x400")

label=Label()
label.pack(padx=20, pady=15)

Button(text="загрузить картинку", command=show).pack()

progr=ttk.Progressbar(mode="determinate", length=300)
progr.pack()

Label(text="ширина").pack()
w_spinbox=ttk.Spinbox(from_=200, to=600, increment=50)
w_spinbox.pack()

Label(text="высота").pack()
h_spinbox=ttk.Spinbox(from_=200, to=600, increment=50)
h_spinbox.pack()


window.mainloop()







