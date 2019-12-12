from LogicLayer.LLAPI import LLAPI
from LogicLayer.DestinationLL import DestinationLL

class DestinationUI:
    def __init__(self):
        self.LLAPI = LLAPI()

    def register_destination(self):
        destination_name = input('Destination name: ')
        destination_id = input('Destination ID: ')
        flight_duration = input('Flight duration: ')
        contactNr = input('Contact number: ')
        LLAPI().RegisterDestination(destination_name, destination_id, flight_duration, contactNr)
        
        return

    def print_destinations(self):
        print("List all destinations")
        destinations = self.LLAPI.ListAllDestinations()
        for destination in destinations:
            print(destination)
        print("\n")
      
    def change_destination_contact_info(self):
        dest_id = input("Destination ID: ")
        contactNr = input("New contact number: ")
        contact = self.LLAPI.UpdateDestinationContactNumber(dest_id, contactNr)


#test1 = DestinationUI()
#test1.print_destinations()
#test1.register_destination()
