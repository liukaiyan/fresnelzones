import fresnel_spiral
import matplotlib.pyplot as plot
from pylab import axes
from numpy import arange
from matplotlib.widgets import Slider

def show(model):
    lowest = 500
    highest = 10000
    default = 2000
    step = 100

    observer_destances = arange(lowest, highest, step)
    intensities = []
    for distance in observer_destances:
        model.observer_distance = distance
        intensities.append(model.calculate_intensity())

    figure = plot.figure(1)
    plot.subplots_adjust(left=0.15, bottom=0.3)

    plot.subplot2grid((1, 3), (0, 0), colspan=2)
    #plt.subplot (121)

    plot.title('Зависимость интенсивности от расстояния до отверстия')
    plot.xlabel('Расстояние до отверстия (нм)')
    plot.ylabel('Интенсивность (Вт/м2)')
    plot.grid(True)

    plot.plot(observer_destances, intensities, linewidth=2)

    axcolor = 'lightgoldenrodyellow'
    axfreq = figure.add_axes([0.15, 0.1, 0.48, 0.04], axisbg=axcolor)

    sfreq = Slider(axfreq, 'Расстояние до отверсия (х)', lowest, highest, valinit=default)
    fresnel_spiral.show(model)

    def update(val):
        fresnel_spiral.show(model)
        print('update')

    sfreq.on_changed(update)
    model.draw(figure)
