available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "mouse pad",
                   "6": "hdmi cable",
                   "7": "DVD drive"
                   }

# When using 'in' with a dictionary it only checks the keys, not the values

current_choice = None
computer_parts = []

# current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add a valid option from the list")
        for key, value in available_parts.items():
            print(key, value, sep=": ")

    current_choice = input("> ")

print(computer_parts)

