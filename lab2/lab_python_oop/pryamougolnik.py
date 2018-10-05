from .geom_fig import Fig
from .color import FigureOfClase


class Pryamougol(Fig):
    def __init__(self, w, h, color):
        self.width = w
        self.height = h
        self.color = FigureOfClase(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Ширина : {}, Высота: {}, Цвет: {}; Площадь: {}".format(
            self.width,
            self.height,
            self.color.color,
            self.area())