# garagetester.py
from truck import Truck
from garage import Garage

class GarageTester:
    @staticmethod
    def getExample():
        # Create a truck object (black color, no trailer)
        truck = Truck("black", False)

        # Create a garage and park the truck
        garage = Garage()
        garage.setVehicle(truck)

        # Print the description of the parked vehicle
        print(garage)  # This should trigger the Garage's _str_ method and output