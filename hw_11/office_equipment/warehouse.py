from office_equipment import Printer, Xerox, Scaner


class Warehouse:
    def __init__(self):
        self.storage = {
            Printer: [],
            Scaner: [],
            Xerox: []
        }

    def add_equipment(self, equipment, count: int):
        for i in range(count):
            self.storage.get(type(equipment)).append(equipment)

    def remove_equipment(self, equipment):
        try:
            self.storage.get(type(equipment)).remove(equipment)
        except ValueError:
            print('Out of stock')


