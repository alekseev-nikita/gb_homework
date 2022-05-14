class OfficeEquipment:
    def __init__(self, price, size):
        self.price = price
        self.size = size


class Printer(OfficeEquipment):
    def __init__(self, price, size, is_laser, is_3d):
        super().__init__(price, size)
        self.is_laser = is_laser
        self.is_3d = is_3d


class Scaner(OfficeEquipment):
    def __init__(self, price, size, speed):
        super().__init__(price, size)
        self.speed = speed


class Xerox(OfficeEquipment):
    def __init__(self, price, size, age):
        super().__init__(price, size)
        self.age = age
