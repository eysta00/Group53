from LogicLayer.LLAPI import LLAPI
from datetime import datetime
import os
class VoyageUI:
    def __init__(self):
        self.LLAPI = LLAPI()

    def register_Voyage(self):
        Voyage_destination = input('Voyage destination: ')
        Voyage_time = input('Voyage ID: ')
        Voyage_id = input('Voyage ID: ')
        error = LLAPI().RegisterVoyage(Voyage_destination, Voyage_time, Voyage_id)
        if error != 1:
            print("Error, input not valid!")
        
        return

    def register_aircraft_to_voyage(self):
        Voyage_id = input('Voyage ID: ')
        aircraft = input('Aircraft: ')

    def register_employees_to_voyage(self):
        Voyage_id = input('Voyage ID: ')
        Employee = input('Employee ID: ')

    def assign_captain_to_voyage(self):
        Voyage_id = input('Voyage ID: ')
        Pilot = input('Pilot ID: ')

    def print_voyage_for_day(self):
        year = int(input("Input year: "))
        month = int(input("Input month: "))
        day = int(input("Input day: "))
        date_iso = datetime(year, month, day).isoformat()
        voyages = self.LLAPI.ListVoyagesForGivenDay(date_iso)
        for voyage in voyages:
            print(voyage)
        print("\n")

    def print_voyage_for_week(self):
        print("Input first day of the week you want to look at")
        year = int(input("Input year: "))
        month = int(input("Input month: "))
        day = int(input("Input day: "))
        date_iso = datetime(year, month, day).isoformat()
        voyages = self.LLAPI.ListVoyagesForGivenWeek(date_iso)
        for voyage in voyages:
            
        print("\n")

    def print_Voyages(self):
        row_len, coloumns_len = os.get_terminal_size()
        print("\n\tList all Voyages")
        Voyages = self.LLAPI.ListAllVoyages()
        for Voyage in Voyages:
            print("-" * (int((row_len - len(Voyage.destination)) / 2)), Voyage.destination,)
        print("\n")
    
    def print_voyage_by_dest(self):
        dest_id = input("Destination ID: ")
        Voyages = self.LLAPI.ListVoyagesForDestination(dest_id)
        for voyage in Voyages:
            print(voyage)
        print("\n")

    def UpdateVoyageCaptain(self):
        Voyage_id = input("Enter voyage ID:")
        pilot_ssn = input("Enter pilot ID:")
        voyage_captain = self.LLAPI.UpdateVoyageCaptain(Voyage_id, pilot_ssn)
        try:
            voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id)
        except EntryNotInDatabase:
            print("ERROR! Voyage not found, please input correct id")
            return UpdateVoyageCaptain()
        try:
            captain = self.LLAPI.GetEmployeeBySSN(pilot_ssn)
        except EntryNotInDatabase:
            print("ERROR! Pilot not found, please correct ssn")
            return UpdateVoyageCaptain()

    def soldSeatsForVoyage(self):
        Voyage_id = input("Enter voyage ID:")
        sold_seats = input("Enter seats:")  #not sure about this
        try:
            voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id)
        except EntryNotInDatabase:
            print("ERROR! Voyage not found, please input correct id")
            return soldSeatsForVoyage()
# test1 = VoyageUI()
# test1.addVoyage()
