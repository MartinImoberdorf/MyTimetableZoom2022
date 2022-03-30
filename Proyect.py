import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Proyect_support

import os
import pyautogui as robot
import time
import webbrowser

def meet_por_web(page):
    webbrowser.open(page)
    entrar_reunion=965,539
    aceptar=1065,225


    def abrir(pos,click=1):
            robot.moveTo(pos) #.moveTo para mover a posicion
            robot.click(clicks=click)
    time.sleep(2)
    abrir(entrar_reunion)
    time.sleep(2)
    abrir(aceptar)

def meet_with_password(codigo,password):
    os.startfile(r'C:\Users\Usuario\AppData\Roaming\Zoom\bin\Zoom.exe')
    entrar=793,496
    desactivar_video=803,616
    borrar_nombre=942,537
    cambiar_nombre=807,539
    ubicacion_codigo=814,479
    ubicacion_contraseña=840,483
    time.sleep(2)

    def abrir(pos,click=1):
            robot.moveTo(pos) #.moveTo para mover a posicion
            robot.click(clicks=click)
    time.sleep(2)
    abrir(entrar)
    time.sleep(2)
    abrir(desactivar_video)
    time.sleep(2)
    abrir(borrar_nombre)
    time.sleep(2)
    abrir(cambiar_nombre)
    time.sleep(2)
    robot.typewrite("91570 ")
    time.sleep(2)
    abrir(ubicacion_codigo)
    time.sleep(2)
    robot.typewrite(codigo)
    robot.hotkey("enter")
    time.sleep(2)
    abrir(ubicacion_contraseña)
    time.sleep(2)
    robot.typewrite(password)
    robot.hotkey("enter")

def meet(codigo):
    os.startfile(r'C:\Users\Usuario\AppData\Roaming\Zoom\bin\Zoom.exe')
    entrar=793,496
    desactivar_video=803,616
    borrar_nombre=942,537
    cambiar_nombre=807,539
    ubicacion_codigo=814,479
    time.sleep(2)

    def abrir(pos,click=1):
            robot.moveTo(pos) #.moveTo para mover a posicion
            robot.click(clicks=click)

    time.sleep(2)
    abrir(entrar)
    time.sleep(2)
    abrir(desactivar_video)
    time.sleep(2)
    abrir(borrar_nombre)
    time.sleep(2)
    abrir(cambiar_nombre)
    time.sleep(2)
    robot.typewrite("91570 ")
    time.sleep(2)
    abrir(ubicacion_codigo)
    time.sleep(2)
    robot.typewrite(codigo)
    robot.hotkey("enter")
    time.sleep(2)


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("250x400+580+316")
        top.minsize(120, 1)
        top.maxsize(3004, 1920)
        top.resizable(1,  1)
        top.title("Zoom")
        top.configure(background="#000000")
        top.configure(highlightbackground="#ffffff")

        self.top = top

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.04, rely=0.075, height=55, width=47)
        self.Label2.configure(background="#0080ff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 17")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ACO''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.036, rely=0.43, height=55, width=47)
        self.Label3.configure(activeforeground="#000000")
        self.Label3.configure(background="#ff0000")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 17")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''AGA''')

        self.Label3_1 = tk.Label(self.top)
        self.Label3_1.place(relx=0.036, rely=0.253, height=55, width=47)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#00ff80")
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 17")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''ASI''')

        self.Label3_2 = tk.Label(self.top)
        self.Label3_2.place(relx=0.04, rely=0.6, height=55, width=47)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#ff80ff")
        self.Label3_2.configure(compound='left')
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 17")
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''FIS''')

        self.Label3_2_1 = tk.Label(self.top)
        self.Label3_2_1.place(relx=0.04, rely=0.788, height=54, width=47)
        self.Label3_2_1.configure(activebackground="#f9f9f9")
        self.Label3_2_1.configure(activeforeground="black")
        self.Label3_2_1.configure(background="#ff8000")
        self.Label3_2_1.configure(compound='left')
        self.Label3_2_1.configure(disabledforeground="#a3a3a3")
        self.Label3_2_1.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 17")
        self.Label3_2_1.configure(foreground="#000000")
        self.Label3_2_1.configure(highlightbackground="#d9d9d9")
        self.Label3_2_1.configure(highlightcolor="black")
        self.Label3_2_1.configure(text='''SSL''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.practico1 = tk.Button(self.top,command=lambda: meet_with_password('872 4589 0217','197481'))
        self.practico1.place(relx=0.268, rely=0.075, height=55, width=77)
        self.practico1.configure(activebackground="#ececec")
        self.practico1.configure(activeforeground="#000000")
        self.practico1.configure(background="#d9d9d9")
        self.practico1.configure(compound='left')
        self.practico1.configure(disabledforeground="#a3a3a3")
        self.practico1.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.practico1.configure(foreground="#000000")
        self.practico1.configure(highlightbackground="#d9d9d9")
        self.practico1.configure(highlightcolor="black")
        self.practico1.configure(pady="0")
        self.practico1.configure(relief="solid")
        self.practico1.configure(text='''PRACTICO''')

        self.teorico1 = tk.Button(self.top,command=lambda: meet_with_password('841 0126 7815','ACO1K822'))
        self.teorico1.place(relx=0.612, rely=0.075, height=55, width=77)
        self.teorico1.configure(activebackground="#ececec")
        self.teorico1.configure(activeforeground="#000000")
        self.teorico1.configure(background="#d9d9d9")
        self.teorico1.configure(compound='left')
        self.teorico1.configure(disabledforeground="#a3a3a3")
        self.teorico1.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.teorico1.configure(foreground="#000000")
        self.teorico1.configure(highlightbackground="#d9d9d9")
        self.teorico1.configure(highlightcolor="black")
        self.teorico1.configure(pady="0")
        self.teorico1.configure(relief="solid")
        self.teorico1.configure(text='''TEORICO''')

        self.practico2 = tk.Button(self.top,command=lambda: meet_with_password('872 4589 0217','197481'))
        self.practico2.place(relx=0.268, rely=0.253, height=55, width=77)
        self.practico2.configure(activebackground="#ececec")
        self.practico2.configure(activeforeground="#000000")
        self.practico2.configure(background="#d9d9d9")
        self.practico2.configure(compound='left')
        self.practico2.configure(disabledforeground="#a3a3a3")
        self.practico2.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.practico2.configure(foreground="#000000")
        self.practico2.configure(highlightbackground="#d9d9d9")
        self.practico2.configure(highlightcolor="black")
        self.practico2.configure(pady="0")
        self.practico2.configure(relief="solid")
        self.practico2.configure(text='''PRACTICO''')

        self.practico3 = tk.Button(self.top,command=lambda:meet_por_web('https://utn.zoom.us/j/9101918470?pwd=Z1dKSTZXaVJIbGY4UllsK1gxdDFQZz09#success'))
        self.practico3.place(relx=0.268, rely=0.43, height=55, width=77)
        self.practico3.configure(activebackground="#ececec")
        self.practico3.configure(activeforeground="#000000")
        self.practico3.configure(background="#d9d9d9")
        self.practico3.configure(compound='left')
        self.practico3.configure(disabledforeground="#a3a3a3")
        self.practico3.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.practico3.configure(foreground="#000000")
        self.practico3.configure(highlightbackground="#d9d9d9")
        self.practico3.configure(highlightcolor="black")
        self.practico3.configure(pady="0")
        self.practico3.configure(relief="solid")
        self.practico3.configure(text='''PRACTICO''')

        self.practico4 = tk.Button(self.top,command=lambda: meet_with_password('881 7790 9926','1'))
        self.practico4.place(relx=0.28, rely=0.6, height=55, width=77)
        self.practico4.configure(activebackground="#ececec")
        self.practico4.configure(activeforeground="#000000")
        self.practico4.configure(background="#d9d9d9")
        self.practico4.configure(compound='left')
        self.practico4.configure(disabledforeground="#a3a3a3")
        self.practico4.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.practico4.configure(foreground="#000000")
        self.practico4.configure(highlightbackground="#d9d9d9")
        self.practico4.configure(highlightcolor="black")
        self.practico4.configure(pady="0")
        self.practico4.configure(relief="solid")
        self.practico4.configure(text='''PRACTICO''')

        self.practico5 = tk.Button(self.top,command=lambda: meet_with_password('819 6405 2505','875739'))
        self.practico5.place(relx=0.268, rely=0.788, height=55, width=77)
        self.practico5.configure(activebackground="#ececec")
        self.practico5.configure(activeforeground="#000000")
        self.practico5.configure(background="#d9d9d9")
        self.practico5.configure(compound='left')
        self.practico5.configure(disabledforeground="#a3a3a3")
        self.practico5.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.practico5.configure(foreground="#000000")
        self.practico5.configure(highlightbackground="#d9d9d9")
        self.practico5.configure(highlightcolor="black")
        self.practico5.configure(pady="0")
        self.practico5.configure(relief="solid")
        self.practico5.configure(text='''PRACTICO''')

        self.teorico2 = tk.Button(self.top,command=lambda: meet_with_password('819 1021 4476','853835'))
        self.teorico2.place(relx=0.612, rely=0.253, height=55, width=77)
        self.teorico2.configure(activebackground="#ececec")
        self.teorico2.configure(activeforeground="#000000")
        self.teorico2.configure(background="#d9d9d9")
        self.teorico2.configure(compound='left')
        self.teorico2.configure(disabledforeground="#a3a3a3")
        self.teorico2.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.teorico2.configure(foreground="#000000")
        self.teorico2.configure(highlightbackground="#d9d9d9")
        self.teorico2.configure(highlightcolor="black")
        self.teorico2.configure(pady="0")
        self.teorico2.configure(relief="solid")
        self.teorico2.configure(text='''TEORICO''')

        self.teorico3 = tk.Button(self.top,command=lambda: meet_with_password('890 2339 1228','794613'))
        self.teorico3.place(relx=0.612, rely=0.43, height=55, width=77)
        self.teorico3.configure(activebackground="#ececec")
        self.teorico3.configure(activeforeground="#000000")
        self.teorico3.configure(background="#d9d9d9")
        self.teorico3.configure(compound='left')
        self.teorico3.configure(disabledforeground="#a3a3a3")
        self.teorico3.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.teorico3.configure(foreground="#000000")
        self.teorico3.configure(highlightbackground="#d9d9d9")
        self.teorico3.configure(highlightcolor="black")
        self.teorico3.configure(pady="0")
        self.teorico3.configure(relief="solid")
        self.teorico3.configure(text='''TEORICO''')

        self.teorico4 = tk.Button(self.top,command=lambda: meet_with_password('836 8074 3547','675579'))
        self.teorico4.place(relx=0.612, rely=0.6, height=55, width=77)
        self.teorico4.configure(activebackground="#ececec")
        self.teorico4.configure(activeforeground="#000000")
        self.teorico4.configure(background="#d9d9d9")
        self.teorico4.configure(compound='left')
        self.teorico4.configure(disabledforeground="#a3a3a3")
        self.teorico4.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.teorico4.configure(foreground="#000000")
        self.teorico4.configure(highlightbackground="#d9d9d9")
        self.teorico4.configure(highlightcolor="black")
        self.teorico4.configure(pady="0")
        self.teorico4.configure(relief="solid")
        self.teorico4.configure(text='''TEORICO''')

        self.teorico5 = tk.Button(self.top,command=lambda: meet('828 3051 3336'))
        self.teorico5.place(relx=0.612, rely=0.788, height=55, width=77)
        self.teorico5.configure(activebackground="#ececec")
        self.teorico5.configure(activeforeground="#000000")
        self.teorico5.configure(background="#d9d9d9")
        self.teorico5.configure(compound='left')
        self.teorico5.configure(disabledforeground="#a3a3a3")
        self.teorico5.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 10 -weight bold")
        self.teorico5.configure(foreground="#000000")
        self.teorico5.configure(highlightbackground="#d9d9d9")
        self.teorico5.configure(highlightcolor="black")
        self.teorico5.configure(pady="0")
        self.teorico5.configure(relief="solid")
        self.teorico5.configure(text='''TEORICO''')

def start_up():
    Proyect_support.main()

if __name__ == '__main__':
    Proyect_support.main()



