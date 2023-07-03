class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def features(self):
            raise NotImplementedError("subclass to use this method")

class PublicTransport(Car):
    def features(self):
        print(f"The public transport car used is {self.brand} . Its model make is {self.model}")
class LuxuryCar(Car):
    def features(self):
        print(f"The luxury car used is{self.brand} . Its model make is {self.model}")

class MotorCycle(Car):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity
    def features(self):
        print(f"The motorcycle used is {self.brand}. Its model make is {self.model} . Its engine capacity is {self.capacity}")

Car = PublicTransport("Scania", "4 series")
Car.features()
Car = LuxuryCar("Mercedes", "AMG")
Car.features()
Car = MotorCycle("Honda", 1000, "125cc")
Car.features()