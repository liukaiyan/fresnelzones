#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plot
import sys
import fresnel_x_dependence
import fresnel_r_dependence
import fresnel_spiral
from fresnel import Fresnel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.widgets import Slider

matplotlib.use('TkAgg')

if sys.version_info[0] < 3:
    print("Python 3 required")
    quit()
else:
    import tkinter as tk


def on_key_event(event):
    print('you pressed %s'%event.key)
    key_press_handler(event, model.canvas, model.toolbar)


class WidgetSet:
    def __init__(self, widgets=[]):
        self.widgets = widgets

    def add_widget(self, widget):
        self.widgets.append(widget)


    def add_slider(self, name, val_min, val_max, val_default, on_changed, color = 'lightgoldenrodyellow'):
        slider_axes = plot.figure(1).add_axes([0.15, 0.1, 0.48, 0.04], axisbg=color)
        slider = Slider(slider_axes, name, val_min, val_max, valinit=val_default)
        slider.on_changed(on_changed)
        self.widgets.append(slider)
        return slider


    def clear_widgets(self):
        for widget in self.widgets:
            widget.drawon = False
            widget.disconnect_events()

        self.widgets = []
        plot.clf()

    def update_distance(self, val):
        model.observer_distance = val
        fresnel_spiral.show(model)

    def update_radius(self, val):
        model.hole_radius = val
        fresnel_spiral.show(model)


class Model(Fresnel):
    def __init__(self, tk, tk_root):
        Fresnel.__init__(self)

        self.tk = tk
        self.tk_root = tk_root
        self.canvas = FigureCanvasTkAgg(plot.figure(1), master=self.tk_root)
        self.canvas.get_tk_widget().pack(side=self.tk.TOP, fill=self.tk.BOTH, expand=1)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.tk_root)
        self.canvas.mpl_connect('key_press_event', on_key_event)
        self.widget_set = WidgetSet()

    def draw(self, figure):
        self.canvas.show()
        self.toolbar.update()


root = tk.Tk()
root.wm_title("Зоны Френеля")
model = Model(tk, root)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def _x_dependence():
    model.widget_set.clear_widgets()
    model.widget_set.add_slider('Расстояние до отверсия (х)',
                                fresnel_x_dependence.lowest,
                                fresnel_x_dependence.highest,
                                fresnel_x_dependence.default,
                                model.widget_set.update_distance)
    fresnel_x_dependence.show(model)


def _r_dependence():
    model.widget_set.clear_widgets()
    model.widget_set.add_slider('Радиус отверсия (х)',
                                fresnel_r_dependence.lowest,
                                fresnel_r_dependence.highest,
                                fresnel_r_dependence.default,
                                model.widget_set.update_distance)
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