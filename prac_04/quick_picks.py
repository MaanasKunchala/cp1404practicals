import random
NUMBERS_EACH_PICK = 6
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 45


quick_picks = int(input("How many quick picks? "))
for i in range(0, quick_picks):
    random_numbers = []
    for number in range(0, NUMBERS_EACH_PICK):
        random_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        while random_number in random_numbers:
            random_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        random_numbers.append(random_number)
    random_numbers.sort()
    for number in random_numbers:
        print(f"{number:>2}", end=" ")
    print()


