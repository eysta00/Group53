from LogicLayer.LLAPI import LLAPI
from datetime import datetime
import os
from Exceptions.Exceptions import *
class VoyageUI:
    def __init__(self):
        self.LLAPI = LLAPI()
        self.header = ""

    def __print_information(self, voyage):
        '''Prints information regarding voyages '''
        row_len, coloumn_len = os.get_terminal_size()
        row_len_half = 2 // row_len
        seperator_str =("-" * (row_len - 1) + "\n")
        info_str = "{:^20} {:30} {:>20} {:>20} {:>20} {:>20} {:>10} {:>10}".format(voyage.destination, voyage.departureTime,
        voyage.aircraftID, voyage.captain ,voyage.seatingSoldOutgoing, voyage.outgoingFlightID, voyage.seatingSoldIncoming, voyage.incomingFlightID)
        print(seperator_str, info_str)

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
            
            departureTime = datetime(Voyage_year, Voyage_month, Voyage_day, Voyage_hour, Voyage_minute).isoformat()
            self.LLAPI.AddVoyage(Voyage_destination_id, departureTime)
            
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
            self.__print_information(voyage)
        print("\n")

    def print_voyage_for_week(self):
        print("Input first day of the week you want to look at")
        year = int(input("Input year: "))
        month = int(input("Input month: "))
        day = int(input("Input day: "))
        date_iso = datetime(year, month, day).isoformat()
        voyages = self.LLAPI.ListVoyagesForGivenWeek(date_iso)
        for voyage in voyages:
            self.__print_information(voyage)
        print("\n")

    def print_Voyages(self):
        row_len, coloumns_len = os.get_terminal_size()
        print("\n\tList all Voyages")
        Voyages = self.LLAPI.ListAllVoyages()
        for Voyage in Voyages:
            self.__print_information(Voyage)
        print("\n")
    
    def print_voyage_by_dest(self):
        dest_id = input("Destination ID: ")
        Voyages = self.LLAPI.ListVoyagesForDestination(dest_id)
        for voyage in Voyages:
            self.__print_information(voyage)
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
