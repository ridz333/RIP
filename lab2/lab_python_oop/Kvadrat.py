from .pryamougolnik import Pryamougol

class Kvadr(Pryamougol):
    def __init__(self, w, color):
        super().__init__(w, w, color)

    def __repr__(self):
        return "Ширина : {}, Цвет: {}; Площадь: {}".format(
            self.width,
            self.color.color,
            self.area())