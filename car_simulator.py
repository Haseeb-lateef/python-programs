class car:
    def __init__(self, colour, brand, max_speed, seats):
        self.colour = colour
        self.brand = brand
        self.max_speed = max_speed        
        self.seats = seats

    def move(self):
        return print("Car moving......")

    def stop(self):
       return print("Car stopping....")

    def horn(self):
        return print("beeeeeep......")


car_1 = car("Purple", "Ferrari", "200km/h", 3)
car_2 = car("Silver", "Bugatti","250km/h", 2 )

print(car_1.horn())

print(car_2.move())





    
