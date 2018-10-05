class FigureOfClase:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color


    @color.setter
    def color(self, col):
        self._color = col


    @color.deleter
    def color(self):
        del self.color