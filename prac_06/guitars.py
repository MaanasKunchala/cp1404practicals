from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{name} ({year}) : ${cost:,} added.")
    print()
    name = input("Name: ")
print("These are my guitars:")

for i, guitar in enumerate(guitars):
    vintage_string = "(vintage)" if guitar.is_vintage() is True else ""
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")