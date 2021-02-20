vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# If the key doesnt exist, .get will return NONE, whereas indexing will crash the program
# the get method is useful when your not sure if the key exists or not

# accessing key value pairs
my_car = vehicles['fiesta']
print(my_car)

learner = vehicles.get("er5")
print(learner)\

print()

# adding items to a dictionary
vehicles["onewheel"] = "Plus XR"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Paper plane glider"

# changing values in a dictionary
vehicles["virago"] = "Yamaha XV535"

# removing items from a dictionary
del vehicles["toy"]
vehicles.pop("er5")
# pass none as the default so program will not crash if key is not in dictionary
vehicles.pop("f1", None)

# iterating a dictionary
for key, value in vehicles.items():
    print(key, value, sep=": ")











