class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

    def get_fare(self):
        return self.base_fare


class Bus(Vehicle):
    def __init__(self, base_fare, passengers):
        super().__init__(base_fare)
        self.passengers = passengers

    def get_total_fare(self):
        return self.base_fare * self.passengers


base_fare = float(input("Enter base fare per passenger: "))
passengers = int(input("Enter number of passengers: "))

bus = Bus(base_fare, passengers)
print("Total Bus Fare:", bus.get_total_fare())
