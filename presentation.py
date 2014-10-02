#!/usr/bin/env python3

import matplotlib
import sys
import fresnel_x_dependence

matplotlib.use('TkAgg')

if sys.version_info[0] < 3:
    print("Python 3 required")
    quit()
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Зоны Френеля")


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def _x_dependence():
    fresnel_x_dependence.show(root, Tk)

x_dependence_button = Tk.Button(master=root, text='Зависимость от расстояния до отверстия', command=_x_dependence)
x_dependence_button.pack(side=Tk.BOTTOM)

quit_button = Tk.Button(master=root, text='Закрыть', command=_quit)
quit_button.pack(side=Tk.BOTTOM)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.