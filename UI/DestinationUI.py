from LogicLayer.LLAPI import LLAPI
from LogicLayer.DestinationLL import DestinationLL
from Exceptions.Exceptions import *

class DestinationUI:
    def __init__(self):
        self.LLAPI = LLAPI()

    def register_destination(self):
        country = input('Enter Destination Country: ')
        airport = input('Enter Destination Airport: ')
        flight_duration = input('Enter Flight duration: ')
        distanceFromReykjavik = input('Enter The Distance From Reykjavik: ')
        contactName = input('Enter Contact Name: ')
        contactNr = input('Enter Contact Number: ')
        self.LLAPI.RegisterDestination(country, airport, flight_duration, distanceFromReykjavik, contactName, contactNr)
        
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

    def most_popular_destinations(self):
        most_dest = self.LLAPI.MostPopularDestination()
    
        print(most_dest)

#test1 = DestinationUI()
#test1.print_destinations()
#test1.register_destination()
