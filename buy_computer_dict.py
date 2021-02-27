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
computer_parts = {} # creates an empty dictionary


while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        if current_choice in computer_parts:
            # part is already in, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add a valid option from the list")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
        print("0: To Finish List")

    current_choice = input("> ")

