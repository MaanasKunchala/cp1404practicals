import random

quick_picks = int(input("How many quick picks? "))
for i in range(0, quick_picks):
    random_numbers = []
    for number in range(0, 6):
        random_number = random.randint(1, 45)
        while random_number in random_numbers:
            random_number = random.randint(1, 45)
        random_numbers.append(random_number)
    random_numbers.sort()
    for number in random_numbers:
        print(f"{number:>2}", end=" ")
    print()


