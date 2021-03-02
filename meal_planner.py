from pantry_contents import pantry, recipes

# dictionary comprehension
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("_________________________")
    for key, value in display_dict.items():
        print(f"{key} - {value}")