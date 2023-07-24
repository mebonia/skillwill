from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        return 'car started'

    @abstractmethod
    def stop_engine(self):
        return 'car stopped'


class Car(vehicle):
    def __init__(self, max_speed, current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        return 'car started'

    def stop_engine(self):
        return 'car stopped'


class SportCar(Car):
    def __init__(self, max_speed, current_speed):
        super().__init__(max_speed, current_speed)

    def start_engine(self):
        parent_output = super().start_engine()
        return f"{parent_output} and max speed is {self.max_speed} km/h"

    def stop_engine(self):
        parent_output = super().stop_engine()
        self.current_speed = 0
        return f"{parent_output} and current speed is set to {self.current_speed}"


car1 = Car(200, 80)
print(car1.start_engine(),'\n',car1.stop_engine())

sport_car = SportCar(300, 180)

print(sportcar.start_engine(), '\n', sportcar.stop_engine())
