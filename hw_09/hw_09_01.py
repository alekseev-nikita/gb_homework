import time


class TrafficLight:
    color = {'красный': ('желтый', 7), 'желтый': ('зеленый', 2), 'зеленый': ('красный', 9)}
    current_light = 'красный'

    def running(self):
        while True:
            print(self.current_light)
            time.sleep(self.color.get(self.current_light)[1])
            self.current_light = self.color.get(self.current_light)[0]


tf_1 = TrafficLight()
tf_1.running()
