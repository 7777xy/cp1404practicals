NAME_TO_CODE = {'Black': '#000000', 'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a', 'AliceBlue': '#f0f8ff',
                'Alizarin crimson': '#e32636', 'Amaranth': '#e52b50', 'Amber': '#ffbf00', 'Amethyst': '#9966cc',
                'AntiqueWhite': '#faebd7', 'Apricot': '#fbceb1'}
name = input("Color name: ").title()
while name != "":
    if name not in NAME_TO_CODE:
        print("Invalid color name.")
    else:
        print(NAME_TO_CODE[name])
    name = input("Color name: ").title()

