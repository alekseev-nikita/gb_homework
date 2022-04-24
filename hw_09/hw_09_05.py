class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(f'Взяли {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Лучше всех рисует {self.title}')


class Handle(Stationary):
    def draw(self):
        print(f'{self.title} выделяет текст')


pen = Pen('ручка')
pen.draw()
pencil = Pencil('ручка')
pencil.draw()
handle = Handle('маркер')
handle.draw()
