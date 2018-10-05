from .geom_fig import Fig
from .color import FigureOfClase
from math import pi


class Krug(Fig):
    def __init__(self, r, color):
        self.radius = r
        self.color = FigureOfClase(color)

    def area(self):
        return pi * self.radius * self.radius

    def __repr__(self):
        return "Радиус: {}, Цвет: {}; Площадь: {}".format(
            self.radius,
            self.color.color,
            self.area())