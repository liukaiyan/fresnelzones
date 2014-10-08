import matplotlib.pyplot as plot
from pylab import axes
from numpy import arange
from matplotlib.widgets import Slider


def show(model):
    spiral_x = []
    spiral_y = []
    model.calculate_spiral(spiral_x, spiral_y)
    print("sp")

    figure = plot.figure(1)
    plot.subplot2grid((1, 3), (0, 2), colspan=1)
    plot.title('Комплексная амплитуда волны E')
    plot.xlabel('Re(E)')
    plot.ylabel('Im(E)')
    plot.plot(spiral_x, spiral_y, color='r', linewidth=2)
    plot.plot([0, spiral_x[-1]], [0, spiral_y[-1]], color='g', linewidth=2)
    plot.grid(True)

    model.draw(figure)