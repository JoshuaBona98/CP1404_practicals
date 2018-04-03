COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "black": "#000000", "brown": "#a52a2a",
                "blueviolet": "#8a2be2", "cadetblue": "#5f9ea0",
                "coral": "#ff7f50", "chocolate": "#d2691e",
                "darkgreen": "#006400", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ").lower()
