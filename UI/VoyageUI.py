from LogicLayer.LLAPI import LLAPI
from datetime import datetime
from Exceptions.Exceptions import *

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
        employee_name = input('Input the Name of the Employee')
        employees_with_name = self.LLAPI.ListAllEmployeesWithName(employee_name)

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
            print(voyage)
        print("\n")

    def print_Voyages(self):
        print("List all Voyages")
        Voyages = self.LLAPI.ListAllVoyages()
        for Voyage in Voyages:
            print(Voyage)
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
        try:
            Voyage_id = input("Enter voyage ID:")
            voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id) # so error code hits at the right moment
            flightType = input("Is the flight:\n 1. Outgoing\n 2. Incoming\nFromIceland?: ")
            sold_seats = input("Enter seats:")  #not sure about this
            if flightType.lower() == "outgoing" or flightType == '1':
                # print('going into outgoingl thing')
                self.LLAPI.SellSeatsForVoyageOutgoing(Voyage_id ,int(sold_seats))
                print('\nSold ' + str(sold_seats) + ' seats for the flight, the total is now ' + str(int(sold_seats) + int(voyage.seatingSoldOutgoing)))
                return
            elif flightType.lower() == "incoming" or flightType == '2':
                self.LLAPI.SellSeatsForVoyageIncoming(Voyage_id, int(sold_seats))
                print('\nSold ' + str(sold_seats) + ' seats for the flight, the total is now ' + str(int(sold_seats) + int(voyage.seatingSoldIncoming)))
                return
            else:
                print('\nInvalid Flight Type Selection, Returning to main menu.')
                return
        except EntryNotInDatabase:
            print("\nERROR! Voyage not found, please input correct id")
            return
        except NotEnoughSeats:
            print("\nThere are not enough available seats to sell " + str(sold_seats) + ' seats.')
            return
        except AircraftNotRegistered:
            print("\nYou must register an aircraft to the voyage before selling seats.")
            
# test1 = VoyageUI()
# test1.addVoyage()
