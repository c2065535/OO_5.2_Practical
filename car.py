class Car:

    def __init__(self, year, brand):
        self.year = year
        self.brand = brand

        self.__speed = 0
        self.__top_speed = 10


    def __str__(self):
        return f'Brand year: {self.year}, Car Brand: {self.brand}'

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        if self.__speed < self.__top_speed:
            self.__speed = self.__speed + 5
        else:
            self.__speed = self.__top_speed

    def brake(self):
        if self.__speed > 0:
            self.__speed = self.__speed - 5
        else:
            self.__speed = 0
