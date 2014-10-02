import matplotlib.pyplot as plot
from pylab import axes
from numpy import arange
from matplotlib.widgets import Slider

def show(model):
    spiral_x = []
    spiral_y = []
    model.calculate_spiral(spiral_x, spiral_y)
    spiral_x.append(0)
    spiral_y.append(0)

    figure = plot.figure(1)
    plot.subplot2grid((1, 3), (0, 2), colspan=1)
    plot.plot(spiral_x, spiral_y, color='r', linewidth=2)
    plot.grid(True)

    model.draw(figure)