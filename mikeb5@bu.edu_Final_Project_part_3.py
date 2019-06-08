"""
Michael Barrera
MET CS 521, Fall 2018
Final Project
10/19/2018
"""

# This program prompts the user to enter inventory levels
# The Inventory class is invoked to compare inventory levels vs. targets

class Inventory:
    # Constructor
    def __init__(self, sedan = 200, sporty = 150, suv = 200, 
                 van = 150, truck = 200, luxury = 150):
        self.__sedan = sedan
        self.__sporty = sporty
        self.__suv = suv
        self.__van = van
        self.__truck = truck
        self.__luxury = luxury 
    # Accessors    
    def getSedanTarget(self):
        return self.__sedan
    def getSportyTarget(self):
        return self.__sporty
    def getSuvTarget(self):
        return self.__suv
    def getVanTarget(self):
        return self.__van
    def getTruckTarget(self):
        return self.__truck
    def getLuxuryTarget(self):
        return self.__luxury
    # Compare current inventory to targets
    def getSedan(self):
        sedan = self.getSedanTarget()
        if sedan <200:
            return "under target"
        elif sedan >250:
            return "over target"
        else:
            return "within optimal range"
    def getSporty(self):
        sport = self.getSportyTarget()
        if sport <150:
            return "under target"
        elif sport >175:
            return "over target"
        else:
            return "within optimal range"
    def getSuv(self):
        suv = self.getSuvTarget()
        if suv <200:
            return "under target"
        elif suv >250:
            return "over target"
        else:
            return "within optimal range"
    def getVan(self):
        van = self.getVanTarget()
        if van <150:
            return "under target"
        elif van >175:
            return "over target"
        else:
            return "within optimal range"
    def getTruck(self):
        truck = self.getTruckTarget()
        if truck <200:
            return "under target"
        elif truck >250:
            return "over target"
        else:
            return "within optimal range"
    def getLuxury(self):
        luxury = self.getSedanTarget()
        if luxury <200:
            return "under target"
        elif luxury >250:
            return "over target"
        else:
            return "within optimal range"

# Main method invokes Incentory class to display output
def main():
    
    sedan = eval(input("Enter number of sedans: "))
    sporty = eval(input("Enter number of sport cars: "))
    suv = eval(input("Enter number of SUVs: "))
    van = eval(input("Enter number of vans: "))
    truck = eval(input("Enter number of trucks: "))
    luxury = eval(input("Enter number of luxury: "))
    
    current = Inventory(sedan, sporty, suv, van, truck, luxury) #Invoke Inventory
    
    print("\nSedans are", current.getSedan())
    print("Sport cars are", current.getSporty())
    print("SUVs are", current.getSuv())
    print("Vans are",current.getVan())
    print("Trucks are", current.getTruck())
    print("Luxury are", current.getLuxury())
    
main()
    