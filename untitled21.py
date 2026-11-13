class Vehicle:
    def __init__(self, brand, model, year, distance_traveled):
        self.brand = brand
        self.model = model
        self.year = year
        self.distance_traveled = distance_traveled

    def show_info(self):
        print(f"brand :{self.brand} model :{self.model} year :{self.year} distance_traveled:{self.distance_traveled}")

    def drive(self, distance):
        self.distance_traveled += distance
        print(self.distance_traveled)

    def calculate_trip_cost(self, distance):
        raise NotImplementedError("distanse bayad be class hay farzand bashad")


class electricity_car(Vehicle):
    def __init__(self, brand, model, year, distance_traveled):
        super().__init__(brand, model, year, distance_traveled)

    def energy_consumption(self, saat):
        m = saat * 100
        print("shoma", m, "kelomtr rafted")

    def electricity_price(self, safar, km):
        n = km / 100
        print(n)

    def calculate_trip_cost(self, distance):
        cost = (distance / 100) * 2 * 5000
        self.distance_traveled += distance
        print("cost :", cost)
        return cost


class GasCar(Vehicle):
    def __init__(self, brand, model, year, distance_traveled):
        super().__init__(brand, model, year, distance_traveled)

    def fuel_consumption(self, saat):
        m = saat * 100
        print("shoma", m, "kelomtr rafted")

    def fuel_price(self, safar, km):
        n = km / 100
        print(n)

    def calculate_trip_cost(self, distance):
        cost = (distance / 100) * 8 * 5000
        self.distance_traveled += distance
        print("cost :", cost)
        return cost


car1 = GasCar("f", "h", 144443, 1000)
car2 = electricity_car("h", "f", 10000, 500)
vehicles = [car1, car2]
for vehicle in vehicles:
    vehicle.show_info()
    vehicle.calculate_trip_cost(150)
        
        
