class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passangers_name(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passengers")
            for passenger in self.passengers:
                print(f"{passenger.name}")
        else:
            print(f"There are no passenger in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
oleg = Human("Oleg")
car = Auto("BMW")
car.add_passengers(nick)
car.add_passengers(kate)
car.print_passangers_name()
car.add_passengers(oleg)
car.print_passangers_name()