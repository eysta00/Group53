from LogicLayer.LLAPI import LLAPI
from datetime import datetime
from Exceptions.Exceptions import *
import os

class VoyageUI:
    def __init__(self):
        self.LLAPI = LLAPI()
        self.header = "{:^8}|{:^15}|{:^25}|{:^12}|{:^20}|{:^14}|{:^9}|{:^21}|{:^21}|{:^21}|{:^21}".format("VoyageID","DestinationID", "Departure Time", "Aircraft ID", "Head flight attendant", "Captain SSN","IsStaffed", "Outgoing seats sold", "Outgoing Flight ID", "Incoming seats sold", "Incoming flight ID")


# private method to format prints
    def __print_information(self, voyage):
        try:
            '''Prints information regarding voyages'''
            is_full_bool = self.LLAPI.IsFullyStaffed(voyage)
            row_len, coloumn_len = os.get_terminal_size()
            row_len_half = 2 // row_len
            seperator_str =("-" * (row_len - 1) + "\n")
            info_str = "{:^8} {:^15} {:^25} {:^12} {:^20} {:^14} {:^9} {:^21} {:^21} {:^21} {:^21}".format(str(voyage.voyageID) ,str(voyage.destination), str(voyage.departureTime), 
            str(voyage.aircraftID),str(voyage.headFlightAttendant), str(voyage.captain) ,str(is_full_bool),str(voyage.seatingSoldOutgoing), str(voyage.outgoingFlightID), str(voyage.seatingSoldIncoming), str(voyage.incomingFlightID))
            print(seperator_str, info_str)
        except:
            print("Unexpected error has occured, returning to home screen")
            return


# method to register a new voyage
    def register_Voyage(self):
        try:
            print('\n##### Register New Voyage #####\n')
            destinations = self.LLAPI.ListAllDestinations()
            idList = [str(dest.dest_id) for dest in destinations]
            # print(idList)
            print('Available Destinations:')
            print('ID \t Name')
            for dest in destinations:
                print(str(dest.dest_id) + ' \t' + str(dest.airport_str))
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
        except:
            print("Unexpected error has occured, returning to home screen")
            return


# Method to register recurring voyages
    def register_recuring_voyage(self):
        try:
            print('\nRegister A recurring voyage\n')

            destinations = self.LLAPI.ListAllDestinations()
            idList = [str(dest.dest_id) for dest in destinations]
            print('Available Destinations:')
            print('ID \t Name')
            for dest in destinations:
                print(str(dest.dest_id) + ' \t' + str(dest.airport_str))
            Voyage_destination_id = input('Enter Destination ID: ')
            if Voyage_destination_id not in idList:
                print('\nInvalid destinationID selection returning to main.')
                return
            
            dayInterval = int(input('\nEnter How Many Days are Desired Between The Recurring Events (7 for a week): '))
            if dayInterval < 1:
                print("\nInvalid day interval, returning to main.")
                return

            print("\nEnter the date and time of the first voyage below:")
            year = int(input("\nEnter the Year: "))
            month = int(input("\nEnter The Month: "))
            day = int(input("\nEnter the Day: "))
            hour = int(input("\nEnter the Hour: "))
            minute = int(input("\nEnter the Minute: "))

            firstTime = datetime(year, month, day,hour,minute).isoformat()

            quantity = int(input("\nEnter how many voyages you want to assign with the entered period: "))
            
            self.LLAPI.AddRecurringVoyages(Voyage_destination_id, firstTime, dayInterval, quantity)
            print('\n', quantity, " Voyages have been successfully added.")
            return
        except ValueError:
            print("\nDate is incorrectly set, returning to main")
            return
        except DepartureTimeOccupied:
            print("\nThe selected date and time already has a voyage, consider delaying the voyage, returning to main.")
            return
        except:
            print("Unexpected error has occured, returning to home screen")
            return

# Method to register an aircraft to a voyage
    def register_aircraft_to_voyage(self):
        try:
            Voyage_id = input('Enter Desired Voyage ID: ')
            voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id)
            print("\nAvailable aircrafts for Voyage:\n")
            availableAircrafts = self.LLAPI.ListAvailableAircrafts(voyage.departureTime)
            print('{:15}{:20}{:20}'.format('AircraftID', 'Manufacturer', 'Model'))
                

            airID_lst = [str(air.aircraftID) for air in availableAircrafts]

            if len(airID_lst) < 1:
                print('\nThere are no available Aircrafts at the time of the selected Voyage, returning to main.\n')
                return

            for air in availableAircrafts:
                print('{:15}{:20}{:20}'.format(air.aircraftID, air.manufacturer, air.model))
            
            aircraft_id = input('\nEnter Aircraft ID: ')
            
            if aircraft_id not in airID_lst:
                print('\nInvalid ID Choice, returning to main.\n')
                return

            self.LLAPI.AssignAircraftToVoyge(Voyage_id, aircraft_id)

            print('\nSuccessfully assigned aircraft to voyage\n')

        except EntryNotInDatabase:
            print('\nInvalid Voyage ID, returning to main')
            return
        except:
            print("Unexpected error has occured, returning to home screen")
            return

# Method to register an employee to a voyage
    def register_employees_to_voyage(self):
        employee_name = "default"
        try:
            rows_len, columns_len = os.get_terminal_size()
            
            voyage_id = input('Voyage ID: ')
            voyage = self.LLAPI.getVoyageByVoyageID(voyage_id)
            employee_name = input('Input the Name of the Employee: ')
            employees_with_name = self.LLAPI.ListAllEmployeesWithName(employee_name)
            
            if len(employees_with_name) == 1:
                employeeSSN = employees_with_name[0].ssn
            
            elif len(employees_with_name) > 1:
                employeeSSN_lst = [emp.ssn for emp in employees_with_name]

                print("More than one employee was found with that name")
                print("-" * (rows_len - 1))
                print("{:40}\t{:10}\t{:20}\t{:10}\t{:35}\t{:20}\t{}".format("Name", "SSN", "Address", "Phone", "Email", "Pilot status", "Licenses"))
                print("-" * (rows_len - 1))
                for employee in employees_with_name:
                    print(employee)
                    print("-" * (rows_len - 1))
                employeeSSN = input("\nPlease input the ssn of employee you want to update: ")
                
                if employeeSSN not in employeeSSN_lst:
                    print("\nInvalid ssn Selection, returning to main.\n")
                    return

            else:
                print("\nThere is no employee called " + employee_name + " in our system, returning to main.\n")
                return
            self.LLAPI.AddStaffToVoyage(voyage_id, employeeSSN)

        except EntryNotInDatabase:
            print("\nThere is no employee called " + employee_name + " in our system, returning to main.\n")
            return
        except EmployeeAlreadyAssigned:
            print('\n' + employee_name + ' is already assigned to this flight')
        except AircraftNotRegistered:
            print('\nYou Must Assign a Plane to the Voyage before Assigning Staff, returning to main\n')
        except:
            print("Unexpected error has occured, returning to home screen")
            return
                

# Method to assign a head flightattendant to a voyage
    def assign_head_flightattendant_to_voyage(self):
        try:
            print("Assign head flightattendant to voyage\n")
            Voyage_id = input('Voyage ID: ')
            voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id)
            if len(voyage.flightAttendants_lst) < 1:
                print('\nYou must assign a flight attendant to Voyage before assigning Head flight attendant.')
                return
            elif len(voyage.flightAttendants_lst) == 1:
                flight_att = self.LLAPI.GetEmployeeBySSN(voyage.flightAttendants_lst[0])
                self.LLAPI.UpdateVoyageHeadFlightAttendant(Voyage_id, voyage.flightAttendants_lst[0])
                print(str(flight_att.name) + ' Has Been set as head flight attendant')
                
                return
            else:
                print('\nPlease Select what Flight Attendant You Want To Make Head flight attendant:\n')
                for flight_person in voyage.flightAttendants_lst:
                    print(self.LLAPI.GetEmployeeBySSN(flight_person))
                SSN = input('Flight attendant SSN: ')
                if SSN not in voyage.flightAttendants_lst:
                    print('Invalid Selection, Returning to menu.')
                    return
                self.LLAPI.UpdateVoyageHeadFlightAttendant(Voyage_id, SSN)
                return 
        except:
            print("Unexpected error has occured, returning to home screen")
            return


# method to assign a captain to a voyage
    def assign_captain_to_voyage(self):
        try:
            print("Assign captain to voyage\n")
            Voyage_id = input('Voyage ID: ')
            voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id)
            if len(voyage.pilots_lst) < 1:
                print('\nYou must assign more pilots to Voyage before assigning Captain, returning to main')
                return

            elif len(voyage.pilots_lst) == 1:
                cap = self.LLAPI.GetEmployeeBySSN(voyage.pilots_lst[0])
                self.LLAPI.UpdateVoyageCaptain(Voyage_id, voyage.pilots_lst[0])
                print('\n' + str(cap.name) + ' Has Been set as voyage Captain')
                
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
        except:
            print("Unexpected error has occured, returning to home screen")
            return

# method to print all voyages for a given day
    def print_voyage_for_day(self):
        try:
            year = int(input("Input year: "))
            month = int(input("Input month: "))
            day = int(input("Input day: "))
            date_iso = datetime(year, month, day).isoformat()
            voyages = self.LLAPI.ListVoyagesForGivenDay(date_iso)

            if len(voyages) == 0:
                print("\nNo Assigned Voyages for date: ", date_iso)
                return

            print(self.header)
            for voyage in voyages:
                self.__print_information(voyage)
            print("\n")
        except:
            print("Unexpected error has occured, returning to home screen")
            return


# method to print all voyages for a certain week
    def print_voyage_for_week(self):
        try:
            print("Input first day of the week you want to look at")
            year = int(input("Input year: "))
            month = int(input("Input month: "))
            day = int(input("Input day: "))
            date_iso = datetime(year, month, day).isoformat()
            voyages = self.LLAPI.ListVoyagesForGivenWeek(date_iso)
            print(self.header)
            for voyage in voyages:
                self.__print_information(voyage)
            print("\n")
        except:
            print("Unexpected error has occured, returning to home screen")
            return

# method to print all voyages
    def print_Voyages(self):
        try:
            row_len, coloumns_len = os.get_terminal_size()
            print("\n\tList all Voyages")
            Voyages = self.LLAPI.ListAllVoyages()
            print(self.header)
            for Voyage in Voyages:
                self.__print_information(Voyage)
            print("\n")
        except:
            print("Unexpected error has occured, returning to home screen")
            return
    

# Methed to print all voyages by destination
    def print_voyage_by_dest(self):
        # destinations = self.LLAPI.
        try:
            dest_id = input("Destination ID: ")
            Voyages = self.LLAPI.ListVoyagesForDestination(dest_id)
            print(self.header)
            for voyage in Voyages:
                self.__print_information(voyage)
            print("\n")
        except:
            print("Unexpected error has occured, returning to home screen")
            return

# Method to update a voyages captain
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
        except:
            print("Unexpected error has occured, returning to home screen")
            return


# Method to sell seats to a voyage
    def soldSeatsForVoyage(self):
        try:
            Voyage_id = input("Enter voyage ID:")
            voyage = self.LLAPI.getVoyageByVoyageID(Voyage_id) # so error code hits at the right moment
            flightType = input("Is the flight:\n 1. Outgoing\n 2. Incoming\nFromIceland?: ")
            sold_seats = input("Enter seats:") 
            if flightType.lower() == "outgoing" or flightType == '1':
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
        except:
            print("Unexpected error has occured, returning to home screen")
            return

    def ListStatusOfVoyages(self):
        try:
            voyages = self.LLAPI.ListAllVoyages()
            print("\n{:10} {:15} {:20} {:30}".format("Voyage ID", "Airport", "Departure Time", 'Voyage Status'))
            
            for voy in voyages:
                print("\n{:10} {:15} {:20} {:30}".format(voy.voyageID, self.LLAPI.GetDestinationByDestinationID(voy.destination).airport_str, voy.departureTime, self.LLAPI.GetVoyageStatus(voy)))
        except:
            print("Unexpected error has occured, returning to home screen")
            return