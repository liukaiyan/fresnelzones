import fresnel_spiral
import matplotlib.pyplot as plot
from numpy import arange

lowest = 0.1
highest = 20
default = 5
step = 0.1


def show(model):
    hole_radiuses = arange(lowest, highest, step)
    current_hole_radius = model.hole_radius
    intensities = []
    for radius in hole_radiuses:
        model.hole_radius = radius
        intensities.append(model.calculate_intensity())

    model.hole_radius = current_hole_radius
    figure = plot.figure(1)
    plot.subplots_adjust(left=0.15, bottom=0.3)
    plot.subplot2grid((1, 3), (0, 0), colspan=2)

    plot.title('Зависимость интенсивности от радиуса отверстия')
    plot.xlabel('Радиус отверстия (нм)')
    plot.ylabel('Интенсивность (Вт/м2)')
    plot.grid(True)

    plot.plot(hole_radiuses, intensities, linewidth=2)
    fresnel_spiral.show(model)

    model.draw(figure)