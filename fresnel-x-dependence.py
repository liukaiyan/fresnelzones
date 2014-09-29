# -*- coding: utf-8 -*-

from pylab import *
from math  import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

#-----------------------------------------------------------------------------------------------------------------------

# HoleRadius > x > HoleRadius^2 / WaveLength

I0         = 1      # интенсивность открытой 0-й зоны
WaveLength = 400    # nM
HoleRadius = 3000   # nM

#-----------------------------------------------------------------------------------------------------------------------

def K (alpha):
    return cos (alpha)

def vectorIntensity (x, h, theta=+inf):
    n = 100

    phi_m = (2*pi * (sqrt (h*h + x*x) - x)) / WaveLength

    deltaAngle = pi / n
    deltaR = h / n

    summX = 0
    summY = 0

    halfLambda = WaveLength / 2
    pi_x_4 = 4 * pi * x

    phi = deltaAngle
    r = 0
    pr = 0
    while phi < phi_m and phi < theta:
        L = x + phi * halfLambda / pi
        #phi = 2*pi*(L - x) / WaveLength

        alpha = arcsin (x / L)
        amp = I0 / L

        #phi_lambda = phi * WaveLength
        #amp = amp * (pi / ((sqrt (abs (phi_lambda * (pi_x_4 - phi_lambda)))) * (4*pi*x*WaveLength - 2*phi*WaveLength*WaveLength) / 4*pi*pi))
        #amp = amp * deltaAngle

        r = sqrt (L*L - x*x)
        #dr = r - pr
        #amp = 1 / n
        #pr = r
        amp = amp * deltaAngle
        amp = amp * pi
        amp = amp / WaveLength

        #amp = amp / n

        summY += amp * sin (phi)
        summX += amp * cos (phi)

        phi = phi + deltaAngle
        #r = r + deltaR

    return (summX, summY)


def intensity (x, h):
    (rx, ry) = vectorIntensity (x, h)
    return ((rx*rx + ry*ry)) * 3*10**8 / 8*pi


def spiral (spiralX, spiralY, x):
    for theta in arange (0.0, 8.0*pi, 0.4):
        (rx, ry) = vectorIntensity (x, HoleRadius, theta)
        spiralX.append (rx * 1000)
        spiralY.append (ry * 1000)

#-----------------------------------------------------------------------------------------------------------------------

X = arange (500, 25000, 50)
S = [intensity (x, HoleRadius) for x in X];

spiralX = []
spiralY = []
spiral (spiralX, spiralY, 2000)
spiralX.append (0)
spiralY.append (0)

plt.figure (1)
plt.subplots_adjust (left=0.15, bottom=0.3)

plt.subplot2grid ((1, 3), (0, 0), colspan=2)
#plt.subplot (121)

plt.title ('Зависимость интенсивности от расстояния до отверстия')
plt.xlabel ('Расстояние до отверстия (Нм)')
plt.ylabel ('Интенсивность (Вт/м2)')
plt.grid (True)

plt.plot (X, S, linewidth=2)

axcolor = 'lightgoldenrodyellow'
axfreq = axes([0.15, 0.1, 0.48, 0.04], axisbg=axcolor)

sfreq = Slider (axfreq, 'Расстояние до отверсия (х)', 500, 25000, valinit=2000)

#span = matplotlib.widgets.SpanSelector (sbplt, onselect, 'horizontal')

subp = plt.subplot2grid ((1, 3), (0, 2), colspan=1)
#plt.subplot (122)
spp, = plt.plot (spiralX, spiralY, color='r', linewidth=2)
plt.grid (True)


def update(val):
    xx = sfreq.val

    spiralX = []
    spiralY = []
    spiral (spiralX, spiralY, xx)
    spiralX.append (0)
    spiralY.append (0)

    spp.set_xdata (spiralX)
    spp.set_ydata (spiralY)

    #subp.canvas.draw_idle()
    #spp.draw()
    print ('replot')

sfreq.on_changed (update)

plt.show()
