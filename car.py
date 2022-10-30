class Car:

    def __init__(self, year, brand):
        self.year = year
        self.brand = brand

        self.__speed = 0
        self.__max_speed = 50
        

    def __str__(self):
        return f'Brand year: {self.year}, Car Brand: {self.brand}'

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5
