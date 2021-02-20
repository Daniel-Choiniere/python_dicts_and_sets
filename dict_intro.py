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
my_car = vehicles['fiesta']
print(my_car)

learner = vehicles.get("er5")
print(learner)\

print()

for key, value in vehicles.items():
    print(key, value, sep=": ")







