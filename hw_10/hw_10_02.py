from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, size):
        self._size = size

    @abstractmethod
    def total_material(self):
        pass


class Coat(Product):
    @property
    def total_material(self):
        return self._size / 6.5 + 0.5


class Suit(Product):
    @property
    def total_material(self):
        return 2 * self._size + 0.3


s = Suit(60)
print(s.total_material)
c = Coat(60)
print(s.total_material)
