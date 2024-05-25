class Vehicle:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display_info(self):
        print(f"Make:{self.make}, model:{self.model}, mileage:{self.mileage} miles")

    def drive(self, miles=0):
        self.miles = miles
        miles = int(input("Введіть на скільки збільшити пробіг машини:"))
        result = self.mileage + miles
        print("Тепер пробіг:", result)

    def maintenance_needed(self):
        if self.miles >= 100000:
            print(True)
        else:
            print(False)

    def reset_mileage(self):
        self.miles = 0
        print("Тепер пробіг знову дорінює нулю")


vehicle_1 = Vehicle("Tesla", "X", 0)
vehicle_1.display_info()
vehicle_1.drive()
vehicle_1.maintenance_needed()
vehicle_1.reset_mileage()
