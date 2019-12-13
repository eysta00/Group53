from LogicLayer.LLAPI import LLAPI
from Exceptions.Exceptions import *
from InstanceClasses.Aircraft import *
from datetime import datetime

class AircraftUI:
    def __init__(self):
        self.LLAPI = LLAPI()

    def register_aircraft(self):
        try:
            manufacturer = input('Enter Aircraft Manufacturer: ')
            model = input('Enter Aircraft Model: ')
            total_seats = input('Enter Total Number of Seats: ')

            self.LLAPI.RegisterAircraft(manufacturer, model, total_seats)
        except:
            print("Unexpected error has occured, returning to home screen")
            return
        return

    def print_aircrafts(self):
        try:
            print("\n##### List All Aircrafts #####\n")
            aircrafts = self.LLAPI.ListAllAircrafts()
            for aircraft in aircrafts:
                print(aircraft)
            print("\n")
        except:
            print("Unexpected error has occured, returning to home screen")
            return

    
    def showAircraftStatus(self):
        print("\nAircraft Status")
        # aircrafts = self.LLAPI.AircraftStatus()
        id = input("\nEnter Aircraft ID: ")
        try:
            aircraftStatus = self.LLAPI.AircraftStatus(id, datetime.now().isoformat())
            print("\nThe Aircraft is " + aircraftStatus)
        except EntryNotInDatabase:
            print("The entered Aircraft ID does not correspond to an entry in the database.")
        except:
            print("Unexpected error has occured, returning to home screen")
            return
        # if id in aircrafts:
        #     return LLAPI().ShowStatusOfAircrafts()
        # else:
        #     print("Aircraft ID not found!")

        print("\n")
    
    def printAvailableAircrafts(self):
        try:
            aircrafts = self.LLAPI.ShowStatusOfAircrafts()
            for aircraft in aircrafts:
                print(aircraft)
            print("\n")
        except:
            print("Unexpected error has occured, returning to home screen")
            return