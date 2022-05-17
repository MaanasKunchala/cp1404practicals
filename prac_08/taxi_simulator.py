from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    option = input(">>> ").lower()
    while option != "q":
        if option == "c":

            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_option = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_option]
                if taxi_option not in range(0, 3):
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input")
            print(f"Bill to date: ${bill:.2f}")
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()

        elif option == "d":

            drive_taxi()

            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()

        else:
            print("Invalid option")
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()


main()
