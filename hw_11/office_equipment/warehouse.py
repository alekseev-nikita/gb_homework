class Warehouse:
    def __init__(self):
        self.storage = []

    def __str__(self):
        return ''.join([f'{type(el)}: size - {el.size}; price - {el.price}\n' for el in self.storage])

    def add_equipment(self, equipment):
        self.storage.append(equipment)

    def remove_equipement(self, equipment):
        try:
            self.storage.remove(equipment)
        except ValueError:
            print('Out of stock')
