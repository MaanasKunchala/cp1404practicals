"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if 0 <= score <= 100:
    if score >= 90:
        category = "Excellent"
    elif score >= 50:
        category = "Pass"
    else:
        category = "Bad"
else:
    category = "Invalid Value"
print(category)

