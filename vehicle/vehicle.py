class BMW:
    def start(self):
        return "BMW engine started"

    def speed(self):
        return "BMW top speed is 400 km/h"


class Ferrari:
    def start(self):
        return "Ferrari engine roars to life"

    def speed(self):
        return "Ferrari top speed is 340 km/h"


def vehicle_info(vehicle):
    print(vehicle.start())
    print(vehicle.speed())


bmw = BMW()
ferrari = Ferrari()

vehicle_info(bmw)
vehicle_info(ferrari)
