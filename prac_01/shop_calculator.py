price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(0, number_of_items):
    price += float(input("Price of item: "))
if price > 100:
    discount = (10 / 100) * price
    price -= discount
print("Total price for {} items is ${:.2f}".format(number_of_items, price))

