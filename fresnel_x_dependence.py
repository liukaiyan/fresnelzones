import fresnel_spiral
import matplotlib.pyplot as plot
from numpy import arange

lowest = 500
highest = 60000
default = 2000
step = 100

def show(model):
    observer_destances = arange(lowest, highest, step)
    intensities = []
    for distance in observer_destances:
        model.observer_distance = distance
        intensities.append(model.calculate_intensity())

    model.observer_distance = default
    figure = plot.figure(1)
    plot.subplots_adjust(left=0.15, bottom=0.3)

    plot.subplot2grid((1, 3), (0, 0), colspan=2)
    #plt.subplot (121)

    plot.title('Зависимость интенсивности от расстояния до отверстия')
    plot.xlabel('Расстояние до отверстия (нм)')
    plot.ylabel('Интенсивность (Вт/м2)')
    plot.grid(True)

    plot.plot(observer_destances, intensities, linewidth=2)
    fresnel_spiral.show(model)

    model.draw(figure)
