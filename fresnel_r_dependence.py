import fresnel_spiral
import matplotlib.pyplot as plot
from numpy import arange

lowest = 10
highest = 20000
default = 3000
step = 400


def show(model):
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
    fresnel_spiral.show(model)

    model.draw(figure)