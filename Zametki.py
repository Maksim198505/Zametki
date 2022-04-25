from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE
font_size = 12
color = "black"


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except EXCEPTION:
        messagebox.showerror("Ошибка!", "Нельзя сохранить файл!")


def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


def font_size_change(new_size):
    global font_size
    font_size = new_size


def color_change(new_color):
    global color
    color = new_color
    

zam = Tk()
zam.title("Заметки на питоне")
zam.geometry("550x550")

text = Text(zam)
text.place(x=100, y=5, width=440, height=540)

menu_bar = Menu(zam)
file_menu = Menu(menu_bar)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)
menu_bar.add_cascade(label="Файл", menu=file_menu)


btn = Button(zam, text="Красный", width=10)
btn.config(command=lambda: color_change("red"))
btn.place(x=10, y=5)

btn1 = Button(zam, text="Зеленый", width=10)
btn1.config(command=lambda: color_change("green"))
btn1.place(x=10, y=45)

btn2 = Button(zam, text="Синий", width=10)
btn2.config(command=lambda: color_change("blue"))
btn2.place(x=10, y=85)


zam.config(menu=menu_bar)
zam.mainloop()
