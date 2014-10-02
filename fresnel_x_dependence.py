import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from pylab import axes
from numpy import arange
from fresnel import Fresnel
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler

def show(tk_root, Tk, fresnel=Fresnel()):

    observer_destances = arange(500, 25000, 50)
    intensities = []
    for distance in observer_destances:
        fresnel.observer_distance = distance
        intensities.append(fresnel.calculate_intensity())

    spiral_x = []
    spiral_y = []
    fresnel.observer_distance = 2000
    fresnel.calculate_spiral(spiral_x, spiral_y)
    spiral_x.append(0)
    spiral_y.append(0)

    figure = plot.figure(1)
    plot.subplots_adjust(left=0.15, bottom=0.3)

    plot.subplot2grid((1, 3), (0, 0), colspan=2)
    #plt.subplot (121)

    plot.title('Зависимость интенсивности от расстояния до отверстия')
    plot.xlabel('Расстояние до отверстия (Нм)')
    plot.ylabel('Интенсивность (Вт/м2)')
    plot.grid(True)

    plot.plot(observer_destances, intensities, linewidth=2)

    canvas = FigureCanvasTkAgg(figure, master=tk_root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg(canvas, tk_root)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    axcolor = 'lightgoldenrodyellow'
    axfreq = axes([0.15, 0.1, 0.48, 0.04], axisbg=axcolor)

    sfreq = Slider(axfreq, 'Расстояние до отверсия (х)', 500, 25000, valinit=2000)

    #span = matplotlib.widgets.SpanSelector (sbplt, onselect, 'horizontal')

    subp = plot.subplot2grid((1, 3), (0, 2), colspan=1)
    #plt.subplot (122)
    spp, = plot.plot(spiral_x, spiral_y, color='r', linewidth=2)
    plot.grid(True)


    def update(val):
        fresnel.observer_distance = sfreq.val

        spiral_x = []
        spiral_y = []
        fresnel.calculate_spiral(spiral_x, spiral_y)
        spiral_x.append(0)
        spiral_y.append(0)

        spp.set_xdata(spiral_x)
        spp.set_ydata(spiral_y)

        #subp.canvas.draw_idle()
        #spp.draw()

    sfreq.on_changed(update)