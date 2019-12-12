from LogicLayer.LLAPI import LLAPI
from Exceptions.Exceptions import *

class AircraftUI:
    def __init__(self):
        self.LLAPI = LLAPI()

    def register_aircraft(self):
        air_id = input('Aircraft ID: ')
        manufacturer = input('Aircraft Model: ')
        total_seats = input('Number of Seats: ')
        error = self.LLAPI.RegisterAircraft(air_id, manufacturer, total_seats)
        if error != 1:
            print("Error, input not valid!")
        
        return

    def print_aircrafts(self):
        print("List all aircrafts")
        aircrafts = self.LLAPI.ListAllAircrafts()
        for aircraft in aircrafts:
            print(aircraft)
        print("\n")
    
    def showAircraftStatus(self):
        print("\nAircraft Status")
        # aircrafts = self.LLAPI.AircraftStatus()
        id = input("\nEnter Aircraft ID: ")
        try:
            aircraftStatus = self.LLAPI.AircraftStatus(id)
            print("\nThe Aircraft is " + aircraftStatus)
        except EntryNotInDatabase:
            print("The entered Aircraft ID does not correspond to an entry in the database.")
        # if id in aircrafts:
        #     return LLAPI().ShowStatusOfAircrafts()
        # else:
        #     print("Aircraft ID not found!")

        print("\n")
    
    def printAvailableAircrafts(self):
        aircrafts = self.LLAPI.ShowStatusOfAircrafts()
        for aircraft in aircrafts:
            print(aircraft)
        print("\n")