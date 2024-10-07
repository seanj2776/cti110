#Joseph Robert Eli Senn
#10/5/2024
#P2LAB2
#This assignment creates a dictionary of different vehicles with stored information and the user can ask about one of said cars to see its mpg and asks for how many miles they will drive it then displays the amount of gas needed.

# Define a dictionary of cars and their fuel efficiencies
cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

#Get keys from dict
cars_keys=cars.keys()

print(cars_keys)

print(*cars_keys, sep=", ")


#Get a car from user
car_name = input ("Enter a vehicle to see it's mpg: ")

#Get car gas mileage information
car_mpg = cars[car_name]
print (f"The {car_name} gets {car_mpg} mpg.")


#Get info from user of how many miles will be driven
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#Calculate
gallons_needed = miles_driven/car_mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
