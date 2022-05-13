from prac_08.taxi import Taxi

# 1.
my_taxi = Taxi("Prius 1", 100)

# 2.
my_taxi.drive(40)

# 3.
print(my_taxi)
print(f"Fare: {my_taxi.get_fare()}")

# 4.
my_taxi.start_fare()
my_taxi.drive(100)

# 5.
print(my_taxi)
print(f"Fare: {my_taxi.get_fare()}")
