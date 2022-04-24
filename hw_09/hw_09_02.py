class Road:
    _length, _width = 0, 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        return self._length * self._width * 25 * 5


road = Road(5000, 25)
print(road.asphalt_mass())
