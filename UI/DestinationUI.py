from LogicLayer.LLAPI import LLAPI
from LogicLayer.DestinationLL import DestinationLL
from Exceptions.Exceptions import *
import os

class DestinationUI:
    def __init__(self):
        try:
            self.LLAPI = LLAPI()
            self.header = "{:20}{:25}{:25}{:25}{:35}{:25}{:25}".format("Destination ID", "Country", "Airport",
            "Flight Duration", "Distance From Reykjavik", "Contact Name", "Contact Number")
        except:
            print("Unexpected error has occured, returning to home screen")
            return

# private method to format text for printing
    def __printing_information(self, destination):
        try:
            information_str = "{:20}{:25}{:25}{:25}{:35}{:25}{:25}".format(str(destination.dest_id), str(destination.country_str), str(destination.airport_str),
            str(destination.flight_duration), str(destination.distanceFromReykjavik), str(destination.contactName_str), str(destination.contactNr_str))
            len_rows, len_coloumns = os.get_terminal_size()
            return information_str
        except:
            print("Unexpected error has occured, returning to home screen")
            return


# private method to register a new destination
    def register_destination(self):
        try:
            print("\n\tRegister a new destination")
            destination_country = input('Country: ')
            airport_str = input('Airport: ')
            flight_duration = input('Flight duration: ')
            distanceFromReykjavik = input('Distance from Reykjavík: ')
            contactName_str = input('Contact name: ')
            contactNr_str = input('Contact number: ')

            LLAPI().RegisterDestination(destination_country, airport_str, flight_duration, distanceFromReykjavik, contactName_str, contactNr_str)
            
            return
        except:
            print("Unexpected error has occured, returning to home screen")
            return

# method to print all destinations in the system
    def print_destinations(self):
        try:    
            print("\n\tList all destinations\n")
            destinations = self.LLAPI.ListAllDestinations()
            print(self.header)
            for destination in destinations:
                print(self.__printing_information(destination))
            print("\n")
        except:
            print("Unexpected error has occured, returning to home screen")
            return
      

# Method to change destination contact info
    def change_destination_contact_info(self):
        try:
            print("\n\tUpdate destination information")
            dest_id = input("Destination ID: ")
            contactNr = input("New contact number: ")
            contact = self.LLAPI.UpdateDestinationContactNumber(dest_id, contactNr)
        except:
            print("Unexpected error has occured, returning to home screen")
            return


# Method to show the most popular destination
    def most_popular_destinations(self):
        try:
            most_dest = self.LLAPI.MostPopularDestination()
            print(self.header)
            print(self.__printing_information(most_dest))
        except:
            print("Unexpected error has occured, returning to home screen")
            return

