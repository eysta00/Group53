from LogicLayer.LLAPI import LLAPI
from LogicLayer.DestinationLL import DestinationLL
from Exceptions.Exceptions import *
import os

class DestinationUI:
    def __init__(self):
        self.LLAPI = LLAPI()
        self.header = "{:20}{:25}{:25}{:25}{:35}{:25}{:25}".format("Destination ID", "Country", "Airport",
        "Flight Duration", "Distance From Reykjavik", "Contact Name", "Contact Number")
    
    def __printing_information(self, destination):
        information_str = "{:20}{:25}{:25}{:25}{:35}{:25}{:25}".format(str(destination.dest_id), str(destination.country_str), str(destination.airport_str),
        str(destination.flight_duration), str(destination.distanceFromReykjavik), str(destination.contactName_str), str(destination.contactNr_str))
        len_rows, len_coloumns = os.get_terminal_size()
        return information_str


    def register_destination(self):
        print("\n\tRegister a new destination")
        destination_name = input('Destination name: ')
        destination_id = input('Destination ID: ')
        flight_duration = input('Flight duration: ')
        contactNr = input('Contact number: ')
        LLAPI().RegisterDestination(destination_name, destination_id, flight_duration, contactNr)
        
        return

    def print_destinations(self):
        print("\n\tList all destinations\n")
        destinations = self.LLAPI.ListAllDestinations()
        print(self.header)
        for destination in destinations:
            print(self.__printing_information(destination))
        print("\n")
      
    def change_destination_contact_info(self):
        print("\n\tUpdate destination information")
        dest_id = input("Destination ID: ")
        contactNr = input("New contact number: ")
        contact = self.LLAPI.UpdateDestinationContactNumber(dest_id, contactNr)

    def most_popular_destinations(self):
        most_dest = self.LLAPI.MostPopularDestination()
    
        print(most_dest)

#test1 = DestinationUI()
#test1.print_destinations()
#test1.register_destination()
