from pylab import *
from math import *
from numpy import arange


class Fresnel:
    # HoleRadius > x > HoleRadius^2 / WaveLength

    def __init__(self,
                 initial_intensity=1,
                 wave_length=500e-6,
                 hole_radius=5,
                 observer_distance=6.72e+3):
        self.initial_intensity = initial_intensity
        self.wave_length = wave_length
        self.k = 2 * pi / wave_length
        self.hole_radius = hole_radius
        self.observer_distance = observer_distance

    def calculate_intensity(self):
        (rx, ry) = self.calculate_amplitude()
        return (rx*rx + ry*ry) * 3*10**8 / (8*pi)

    def calculate_amplitude(self):
        return self.calculate_partial_amplitude(True, 0, self.hole_radius)

    def calculate_partial_amplitude(self, parting, inner_r, outer_r):
        amp_re = 0
        amp_im = 0
        if parting:
            delta_r = 0.001
            n = self.hole_radius / delta_r
        else:
            delta_r = outer_r - inner_r
            inner_r += delta_r
            n = 1

        x2 = self.observer_distance**2

        for i in arange(0, n, 1):
            r = inner_r + i * delta_r
            d = sqrt(r**2 + x2)

            P = 1 / d
            P *= 1 + self.observer_distance / d # K
            P *= r

            arg = -self.k * d
            amp_re += -P * sin(arg)
            amp_im += P * cos(arg)

        k = pi / self.wave_length * self.initial_intensity * self.hole_radius / n
        amp_re *= k
        amp_im *= k

        return amp_re, amp_im

    """
    def calculate_amplitude(self, theta=+inf):
        n = 100

        phi_m = sqrt(self.hole_radius**2 + self.observer_distance**2) - self.observer_distance
        phi_m = 2*pi * phi_m / self.wave_length

        delta_angle = pi / n
        delta_r = self.hole_radius / n

        summ_x = 0
        summ_y = 0

        half_lambda = self.wave_length / 2
        pi_x_4 = 4 * pi * self.observer_distance

        phi = delta_angle
        r = 0
        pr = 0
        while phi < phi_m and phi < theta:
            distance = self.observer_distance + phi * half_lambda / pi
            #phi = 2*pi*(L - x) / WaveLength

            #alpha = arcsin(self.observer_distance / distance)
            amp = self.initial_intensity / distance

            #phi_lambda = phi * WaveLength
            #amp = amp * (pi / ((sqrt (abs (phi_lambda * (pi_x_4 - phi_lambda)))) * (4*pi*x*WaveLength - 2*phi*WaveLength*WaveLength) / 4*pi*pi))
            #amp = amp * deltaAngle

            #r = sqrt(distance**2 - self.observer_distance**2)
            #dr = r - pr
            #amp = 1 / n
            #pr = r
            amp *= delta_angle
            amp *= pi
            amp /= self.wave_length

            #amp = amp / n

            summ_x += amp * cos(phi)
            summ_y += amp * sin(phi)

            phi += delta_angle
            #r = r + deltaR

        return summ_x, summ_y
    """

    def calculate_spiral(self, spiral_x, spiral_y):
        spiral_x.append(0)
        spiral_y.append(0)
        re, im = 0, 0
        delta_r = self.hole_radius / 1000
        for inner_r in arange(0, self.hole_radius, delta_r):
            (r, i) = self.calculate_partial_amplitude(False, inner_r, inner_r + delta_r)
            re += r
            im += i
            spiral_x.append(im)
            spiral_y.append(re)