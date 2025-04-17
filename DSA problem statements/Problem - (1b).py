class Car:
    def __init__(self, brand,
                  car_type,
                  year, 
                  mileage):
        self.brand = brand
        self.car_type = car_type
        self.year = year
        self.mileage = mileage

    def __repr__(self):
        return f"Car(brand='{self.brand}', type='{self.car_type}', year={self.year}, mileage={self.mileage})"

def search_car_by_brand(cars, brand):
    return [car for car in cars if car.brand.lower() == brand.lower()]

# Create a list of cars
cars = [
    Car("Toyota", "Sedan", 2020, 25000),
    Car("Honda", "SUV", 2018, 40000),
    Car("Ford", "Truck", 2019, 30000),
    Car("Toyota", "SUV", 2021, 15000),
    Car("Honda", "Sedan", 2017, 60000)
]

# Example usage
brand_to_search = "Toyota"
result = search_car_by_brand(cars, brand_to_search)

print(f"Cars with brand '{brand_to_search}':")
for car in result:
    print(car)
