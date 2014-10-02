from pylab import *
from math import *
from numpy import arange


class Fresnel:
    # HoleRadius > x > HoleRadius^2 / WaveLength

    def __init__(self,
                 initial_intensity=1,
                 wave_length=400,
                 hole_radius=3000,
                 observer_distance=10000):
        self.initial_intensity = initial_intensity
        self.wave_length = wave_length
        self.hole_radius = hole_radius
        self.observer_distance = observer_distance

    def calculate_intensity(self, theta=+inf):
        (rx, ry) = self.calculate_amplitude(theta)
        return (rx*rx + ry*ry) * 3*10**8 / (8*pi)

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

            alpha = arcsin(self.observer_distance / distance)
            amp = self.initial_intensity / distance

            #phi_lambda = phi * WaveLength
            #amp = amp * (pi / ((sqrt (abs (phi_lambda * (pi_x_4 - phi_lambda)))) * (4*pi*x*WaveLength - 2*phi*WaveLength*WaveLength) / 4*pi*pi))
            #amp = amp * deltaAngle

            r = sqrt(distance**2 - self.observer_distance**2)
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

    def calculate_spiral(self, spiral_x, spiral_y):
        for theta in arange(0.0, 8.0*pi, 0.4):
            (rx, ry) = self.calculate_amplitude(theta)
            spiral_x.append(rx * 1000)
            spiral_y.append(ry * 1000)

    def get_k(self, alpha):
        return cos (alpha)