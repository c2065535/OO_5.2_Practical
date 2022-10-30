from car import Car

def main():
    c = Car(2022, 'ford')

    print(c.__str__())
    print(c.get_speed())
    print(c.accelerate())
    print(c.get_speed())
    print(c.brake())
    print(c.get_speed())


main()
