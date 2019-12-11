from LogicLayer.LLAPI import LLAPI

class DestinationUI:
    def __init__(self):
        self.LLAPI = LLAPI()

    def register_destination(self):
        destination_name = input('Destination name: ')
        destination_id = input('Destination ID: ')
        flight_duration = input('Flight duration: ')
        contactNr = input('Contact number: ')
        error = DestinationLL().RegisterDestination(destination_name, destination_id, flight_duration, contactNr)
        error = LLAPI().RegisterDestination(destination_name, destination_id, flight_duration)
        if error != 1:
            print("Error, input not valid!")
        
        return

    def print_destinations(self):
        print("List all destinations")
        destinations = self.LLAPI.ListAllDestinations()
        for destination in destinations:
            print(destination)
        print("\n")

#test1 = DestinationUI()
#test1.print_destinations()
#test1.register_destination()
