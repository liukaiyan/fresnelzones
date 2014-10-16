import matplotlib.pyplot as plot
from numpy import arange
from math import sqrt


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

    #d = sqrt((spiral_x[1] - spiral_x[0])**2 + (spiral_y[1] - spiral_y[0])**2)
    d = 0.01
    w = d / 3
    h_w = w * 2
    h_l = d / 3

    plot.plot(spiral_x, spiral_y, color='r', linewidth=2)
    #for i in arange(0, len(spiral_x) - 1, 1):
    #    plot.arrow(spiral_x[i], spiral_y[i], spiral_x[i + 1] - spiral_x[i], spiral_y[i + 1] - spiral_y[i],
    #    width=w, head_width=h_w, head_length=h_l, length_includes_head=True, fc='r', ec='k')

    plot.arrow(0, 0, spiral_x[-1], spiral_y[-1],
               width=w*1.5, head_width=h_w*1.5, head_length=h_l*1.5, length_includes_head=True, fc='g', ec='k')


    plot.grid(True)
    mx = max(spiral_x)
    my = max(spiral_y)
    #plot.xlim([-mx - d, mx + d])
    #plot.ylim([-d, my + d])

    model.draw(figure)