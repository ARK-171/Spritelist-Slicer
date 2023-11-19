import os, sys
from PIL import Image
import tkinter as tk

win = tk.Tk()

win.title("SpriteSliser")

t_put = tk.Label(win, text="путь до файла: ")
t_name = tk.Label(win, text="имя файла: ")
t_width = tk.Label(win, text="ширина спрайта: ")
t_height = tk.Label(win, text="высота спрайта: ")
t_number = tk.Label(win, text="номет строки: ")
t_length = tk.Label(win, text="длина строки в спрайтах: ")
t_numbers = tk.Label(win, text="количество строк: ")
t_save = tk.Label(win, text="путь сохранения: ")

in_put = tk.Entry()
in_name = tk.Entry()
in_width = tk.Entry()
in_height = tk.Entry()
in_number = tk.Entry()
in_length = tk.Entry()
in_numbers = tk.Entry()
in_save = tk.Entry()

t_put.grid(row=0, column=0); in_put.grid(row=0, column=1)
t_name.grid(row=1, column=0); in_name.grid(row=1, column=1)
t_width.grid(row=2, column=0); in_width.grid(row=2, column=1)
t_height.grid(row=3, column=0); in_height.grid(row=3, column=1)
t_number.grid(row=4, column=0); in_number.grid(row=4, column=1)
t_length.grid(row=5, column=0); in_length.grid(row=5, column=1)
t_numbers.grid(row=6, column=0); in_numbers.grid(row=6, column=1)
t_save.grid(row=7, column=0); in_save.grid(row=7, column=1)


def S_func():
    name = in_put.get() + "\\" + in_name.get()
    im = Image.open(name)
    if not in_numbers.get():
        for i in range(int(in_length.get())):
            img = im.crop((int(in_width.get()) * i, int(in_height.get()) * (int(in_number.get())-1), int(in_width.get()) * (i+1), int(in_height.get()) * (int(in_number.get()))))
            save = in_save.get() + "\\" + str(i) + ".png"
            img.save(save)
    else:
        for i in range(int(in_numbers.get())):
            for j in range(int(im.width/int(in_width.get()))):
                print((int(in_width.get()) * j, int(in_height.get()) * i, int(in_width.get()) * (j+1), int(in_height.get()) * (i+1)))
                img = im.crop((int(in_width.get()) * j, int(in_height.get()) * i, int(in_width.get()) * (j+1), int(in_height.get()) * (i+1)))
                save = in_save.get() + "\\" + str(i) + "_" + str(j) + ".png"
                img.save(save)


s_btn = tk.Button(text="Start", command=S_func)
s_btn.grid(row=8, column=0)

win.mainloop()
