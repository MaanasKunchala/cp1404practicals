from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    option = input(">>> ").lower()
    while option != "q":
        if option == "c":
            choose_taxi()
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()
        if option == "d":
            drive_taxi()
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()
        else:
            print("Invalid option")
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()


main()
