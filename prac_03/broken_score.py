"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    category = get_category(score)
    print(category)
    random_score = random.randint(0, 100)
    random_category = get_category(random_score)
    print(f"random score = {random_score}")
    print(random_category)


def get_category(score):
    if 0 <= score <= 100:
        if score >= 90:
            category = "Excellent"
        elif score >= 50:
            category = "Pass"
        else:
            category = "Bad"
    else:
        category = "Invalid Value"
    return category


main()
