class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} поворот: {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена скорость {self.speed}')
        else:
            print(f'Скорость: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена скорость {self.speed}')
        else:
            print(f'Скорость: {self.speed}')


class PoliceCar(Car):
    pass


work_car = WorkCar(50, 'желтый', 'трактор', False)
work_car.show_speed()

sport_car = SportCar(280, 'красный', 'F1', False)
sport_car.go()
sport_car.stop()
sport_car.turn('влево')
