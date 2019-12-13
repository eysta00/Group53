from LogicLayer.LLAPI import LLAPI
from Exceptions.Exceptions import *
from InstanceClasses.Aircraft import *
from datetime import datetime

class AircraftUI:
    def __init__(self):
        self.LLAPI = LLAPI()

# method to register a new aircraft
    def register_aircraft(self):
        manufacturer = input('Enter Aircraft Manufacturer: ')
        model = input('Enter Aircraft Model: ')
        total_seats = input('Enter Total Number of Seats: ')

        self.LLAPI.RegisterAircraft(manufacturer, model, total_seats)
        
        return

# method to print all aircrafts
    def print_aircrafts(self):
        print("\n##### List All Aircrafts #####\n")
        aircrafts = self.LLAPI.ListAllAircrafts()
        for aircraft in aircrafts:
            print(aircraft)
        print("\n")
    
# method to show status of all aircrafts
    def showAircraftStatus(self):
        print("\nAircraft Status")
        id = input("\nEnter Aircraft ID: ")
        try:
            aircraftStatus = self.LLAPI.AircraftStatus(id, datetime.now().isoformat())
            print("\nThe Aircraft is " + aircraftStatus)
        except EntryNotInDatabase:
            print("The entered Aircraft ID does not correspond to an entry in the database.")

        print("\n")
    
# method to print available aircrafts
    def printAvailableAircrafts(self):
        aircrafts = self.LLAPI.ShowStatusOfAircrafts()
        for aircraft in aircrafts:
            print(aircraft)
        print("\n")