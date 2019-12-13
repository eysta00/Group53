from LogicLayer.LLAPI import LLAPI
from datetime import datetime
from Exceptions.Exceptions import *
import os
class VoyageUI:
    def __init__(self):
        self.LLAPI = LLAPI()

    def register_Voyage(self):
        try:
            print('\n##### Register New Voyage #####\n')
            destinations = self.LLAPI.ListAllDestinations()
            idList = [str(dest.dest_id) for dest in destinations]
            # print(idList)
            print('Available Destinations:')
            print('ID \t Name')
            for dest in destinations:
                print(str(dest.dest_id) + ' \t' + str(dest.dest_name))
            Voyage_destination_id = input('Enter Destination ID: ') # NEEDS RE CONFIGUREING
            if Voyage_destination_id not in idList:
                print('\nInvalid destinationID selection returning to main.')
                return
            print('\nSelect Time of Voyage\n')
            
            Voyage_year = int(input('Enter Year: '))
            Voyage_month = int(input('Enter Month: '))
            Voyage_day = int(input('Enter Day: '))
            Voyage_hour = int(input('Enter hour: '))
            Voyage_minute = int(input('Enter minute: '))
            
            departureTime = datetime(Voyage_year, Voyage_month, Voyage_day, Voyage_hour, Voyage_minute)
            
            if datetime.now() > departureTime:
                print('\nYou Must Select a Date in the Future, Returning to Main.')
                return


            self.LLAPI.AddVoyage(Voyage_destination_id, departureTime.isoformat())
            
            print('\nVoyage Successfully Added.\n')
            return

        except ToFewAvailableEmployees:
            print('\nThere are to few available employees at that time to create a voyage, returning to main.\n')
            return
        except DepartureTimeOccupied:
            print('\nThe Selected Departure Time is already taken, to flights can not take off similtaniously, returning to main.\n')
            return 
        except ValueError:
            print('The Selected date is invalid, month must be 1-12 and day must be 1-31')
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
        voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id)
        if len(voyage.pilots_lst) < 1:
            print('\nYou must assign Pilots to Voyage before assigning Captain.')
            return
        elif len(voyage.pilots_lst) == 1:
            cap = self.LLAPI.GetEmployeeBySSN(voyage.pilots_lst[0])
            self.LLAPI.UpdateVoyageCaptain(Voyage_id, voyage.pilots_lst[0])
            print(str(cap.name) + ' Has Been set as voyage Captain')
            return
        else:
            print('\nPlease Select what Pilot You Want To Make Captain:\n')
            print(self.LLAPI.GetEmployeeBySSN(voyage.pilots_lst[0]))
            print(self.LLAPI.GetEmployeeBySSN(voyage.pilots_lst[1]))
            capSSN = input('Pilot SSN: ')
            if capSSN not in voyage.pilots_lst:
                print('Invalid Selection, Returning to menu.')
                return
            self.LLAPI.UpdateVoyageCaptain(Voyage_id, capSSN)
            return 

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
        row_len, coloumns_len = os.get_terminal_size()
        print("\n\tList all Voyages")
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
