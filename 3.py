class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_production_year(self):
        return self.__production_year

    def get_color(self):
        return self.__color

    def get_horse_power(self):
        return self.__horse_power

    def get_is_sport_car(self):
        return self.__is_sport_car

    def change_color(self, new_color):
        if not isinstance(new_color, str):
            raise ValueError('ახალი ფერი აუცილებლად უნდა იყოს სტრიქონის სახით შემოყვანილი')
        if new_color == self.__color:
            return False
        else:
            self.__color = new_color
            return True

    def increase_horse_power(self, hp):
        if not isinstance(hp, int):
            raise ValueError('Horse_power აუცილებლად უნდა იყოს სტრინგის ტიპის')
        if hp > 0:
            self.__horse_power += hp
            return True
        else:
            return False
car1 = Car('Ford','Mustang', 2023, 'black',500,)
increas = car1.increase_horse_power(50)
print(increas)
print(car1.get_horse_power())
color_chang= car1.change_color('Red')
print(color_chang)
print(car1.get_color())



