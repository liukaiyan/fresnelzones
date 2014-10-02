#!/usr/bin/env python3

import matplotlib
import sys
import fresnel_x_dependence
import fresnel_r_dependence
from fresnel import Fresnel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler

matplotlib.use('TkAgg')

if sys.version_info[0] < 3:
    print("Python 3 required")
    quit()
else:
    import tkinter as tk


class Model(Fresnel):
    def __init__(self, tk, tk_root, canvas=None, toolbar=None):
        Fresnel.__init__(self)
        self.canvas = canvas
        self.toolbar = toolbar
        self.tk = tk
        self.tk_root = tk_root

    def draw(self, figure):
        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(figure, master=self.tk_root)
            self.canvas.get_tk_widget().pack(side=self.tk.TOP, fill=self.tk.BOTH, expand=1)
            self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.tk_root)
            self.canvas.mpl_connect('key_press_event', on_key_event)

        self.canvas.show()
        self.toolbar.update()


root = tk.Tk()
root.wm_title("Зоны Френеля")
model = Model(tk, root)


def on_key_event(event):
    print('you pressed %s'%event.key)
    key_press_handler(event, model.canvas, model.toolbar)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def _x_dependence():
    fresnel_x_dependence.show(model)


def _r_dependence():
    fresnel_r_dependence.show(model)

x_dependence_button = tk.Button(master=root, text='Зависимость от расстояния до отверстия', command=_x_dependence)
x_dependence_button.pack(side=tk.BOTTOM)

x_dependence_button = tk.Button(master=root, text='Зависимость от радиуса отверстия', command=_r_dependence)
x_dependence_button.pack(side=tk.BOTTOM)

quit_button = tk.Button(master=root, text='Закрыть', command=_quit)
quit_button.pack(side=tk.BOTTOM)

tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.