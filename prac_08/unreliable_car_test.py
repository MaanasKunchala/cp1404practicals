from prac_08.unreliable_car import UnreliableCar

my_car = UnreliableCar("Lamborghini", 100, 40)

# Testing - __init__
print(f"my_car name - {my_car.name}")
print(f"my_car fuel - {my_car.fuel}")
print(f"my_car reliability - {my_car.reliability}")

# Testing - drive()
print(my_car)
print(f"Distance driven: {my_car.drive(100)}")
print(my_car)
