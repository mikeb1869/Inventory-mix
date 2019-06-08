"""
Michael Barrera
MET CS 521, Fall 2018
Final Project
10/19/2018
"""
# This program was used to generate a mock inventory listing

from random import randint, random

# Open file
file = open('inventory.txt', 'w')

cars = ['sedan', 'sporty', 'SUV', 'van', 'truck', 'luxury']

# Write the data to the file
for i in range(1000):
    name = 'Stock #' + str(i+1)
    car = cars[randint(0, 5)]
    if car == 'sedan':
        price = 5000 + 20000*random()
    elif car == 'sporty':
        price = 10000 + 50000*random()
    elif car == 'SUV':
        price = 15000 + 30000*random()
    elif car == 'van':
        price = 15000 + 20000*random()
    elif car == 'truck':
        price = 15000 + 40000*random()
    else:
        price = 25000 + 50000*random()
    file.write('{0} {1} {2:0.2f}\n'.format(name, car, price))
    
file.close()