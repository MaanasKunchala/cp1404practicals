COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_TO_CODE:
        print(f"{colour} is {COLOUR_TO_CODE[colour]}")
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")
