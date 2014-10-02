import fresnel_spiral
import matplotlib.pyplot as plot
from pylab import axes
from numpy import arange
from matplotlib.widgets import Slider

def show(model):
    lowest = 10
    highest = 20000
    default = 3000
    step = 400

    hole_radiuses = arange(lowest, highest, step)
    intensities = []
    for radius in hole_radiuses:
        model.hole_radius = radius
        intensities.append(model.calculate_intensity())

    figure = plot.figure(1)
    plot.subplot2grid((1, 3), (0, 0), colspan=2)

    plot.title('Зависимость интенсивности от радиуса отверстия')
    plot.xlabel('Радиус отверстия (нм)')
    plot.ylabel('Интенсивность (Вт/м2)')
    plot.grid(True)

    plot.plot(hole_radiuses, intensities, linewidth=2)

    axcolor = 'lightgoldenrodyellow'
    axfreq = add_axes([0.15, 0.1, 0.48, 0.04], axisbg=axcolor)
    sfreq = Slider(axfreq, 'Радиус отверсия (х)', lowest, highest, valinit=default)

    fresnel_spiral.show(model)

    def update(val):
        fresnel_spiral.show(model)

    sfreq.on_changed(update)

    model.draw(figure)