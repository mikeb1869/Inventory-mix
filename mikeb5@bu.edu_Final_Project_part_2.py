"""
Michael Barrera
MET CS 521, Fall 2018
Final Project
10/19/2018
"""
# This is the first step of the project.
# This program reads in the inventory dataset then runs analytics for the user

# Open file
file = open('inventory.txt')

# Crete variables for prices
sedan_price = []
sports_car_price = []
suv_price = []
van_price = []
truck_price = []
luxury_price = []

# Read file in & append prices to appropriate variable
for line in file:
    car, price = line.split()[-2:]
    if car == 'sedan':
        sedan_price.append(eval(price))
    elif car == 'sporty':
        sports_car_price.append(eval(price))
    elif car == 'SUV':
        suv_price.append(eval(price))
    elif car == 'van':
        van_price.append(eval(price))
    elif car == 'truck':
        truck_price.append(eval(price))
    else:
        luxury_price.append(eval(price))
        
file.close

def main():
    # Displays menu the user and waits for their selection
    while True:
        print("\nEnter a choice from the options below to run analytics")
        print("1: Sedans")
        print("2: Sport Cars")
        print("3: SUVs")
        print("4: Vans")
        print("5: Trucks")
        print("6: Luxury")
        print("7: exit")
        choice = int(input("Enter a choice: "))
        
        # Reads usuer input and displays appropriate information
        if choice == 1:
            print(n1, "sedans in inventory")
            print("Average price: ${:0,.0f}".format(sum1))
        elif choice == 2:
            print(n2, "sport cars in inventory")
            print("Average price: ${:0,.0f}".format(sum2))
        elif choice == 3:
            print(n3, "SUVs in inventory")
            print("Average price: ${:0,.0f}".format(sum3))
        elif choice == 4:
            print(n4, "vans in inventory")
            print("Average price: ${:0,.0f}".format(sum4))
        elif choice == 5:
            print(n5, "trucks in inventory")
            print("Average price: ${:0,.0f}".format(sum5))
        elif choice == 6:
            print(n6, "luxury in inventory")
            print("Average price: ${:0,.0f}".format(sum6))
        else:
            break

# Calculates number of vehicles per segment
n1 = len(sedan_price)
n2 = len(sports_car_price)
n3 = len(suv_price)
n4 = len(van_price)
n5 = len(truck_price)
n6 = len(luxury_price)
# Calculates average listing price of each segment
sum1 = sum(sedan_price) / n1
sum2 = sum(sports_car_price) / n2
sum3 = sum(suv_price) / n3
sum4 = sum(van_price) / n4
sum5 = sum(truck_price) / n5
sum6 = sum(luxury_price) / n6

main()