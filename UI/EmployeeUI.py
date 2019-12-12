from LogicLayer.LLAPI import LLAPI
from datetime import datetime
import os
class EmployeeUI:
    def __init__(self):
        self.LLAPI = LLAPI()
        self.header = "{:40}\t{:10}\t{:20}\t{:10}\t{:35}\t{:20}\t{}".format("Name", "SSN", "Address", "Phone", "Email", "Pilot status", "Licenses")

    def print_register_employee(self):
        rows_len, columns_len = os.get_terminal_size() # checks on length of terminal, this repeats.

        print("\tRegister a new employee")
        e_name = input("Full employee name: ")
        e_ssn = input("Employee social securtiy number: ")
        e_address = input("Employee Adress: ")
        e_phone = input("Employe phone number: ")
        e_email = input("Employee email: ")
        
        e_pilot = input("Is employee a pilot? yes/no: ").lower()
        if e_pilot == "yes":
            e_pilot = True
            e_planelicense = input("Employee plane license: ")
        else:
            e_planelicense = None
            e_pilot = False
        
        error = self.LLAPI.RegisterEmployee(e_name, e_ssn, e_address, e_phone, e_email, e_pilot, e_planelicense)
        if error != 1:
            print("Error, input not valid!")
            repeat_inquiry = input("Would you like to try again? yes/no: ").lower()
            if repeat_inquiry == "yes":
                return print_register_employee()
        print("\n")        
        return
    
    def print_all_employees(self):
        rows_len, columns_len = os.get_terminal_size()


        print("\tList all employess")
        print(self.header)
        all_employees = self.LLAPI.ListAllEmployees()
        for employee in all_employees:
            print("-" * (rows_len - 1))
            print(employee)
            
        print("\n")
        
    def print_flight_attendants(self):

        print("\tList all flight attendants")
        flight_attendants = self.LLAPI.ListFlightAttendants()
        for attendant in flight_attendants:
            print(attendant)
        print("\n")
    
    def print_pilots(self):


        print("\tList all pilots")
        all_pilots = self.LLAPI.ListPilots()
        for pilot in all_pilots:
            print(pilot)
        print("\n")
    
    def print_assigned_employees(self):


        print("\tList all assigned employees on a given day")
        year = int(input("Input year: "))
        month = int(input("Input month: "))
        day = int(input("Input day: "))
        date_iso = datetime(year, month, day).isoformat()
        assinged_employees = self.LLAPI.ListAssignedEmployees(date_iso)
        for employee in assinged_employees:
            print(employee)
        print("\n")

    
    def print_unassigned_employees(self):

        
        print("\tList all unassigned employees on a given day")
        year = int(input("Input year: "))
        month = int(input("Input month: "))
        day = int(input("Input day: "))
        date_iso = datetime(year, month, day).isoformat()
        unassinged_employees = self.LLAPI.ListUnassignedEmployees(date_iso)
        for employee in unassinged_employees:
            print(employee)
        print("\n")

    def print_update_employee_infomation():

        print("\tUpdate employee information")


    def print_pilots_with_aircraft_privilage(self):


        print("\tList all pilots with a certain aircraft privilage")
        aircraft_model = input("Input aircraft model (case sensitive): ")
        pilot_licenses = self.LLAPI.ListPilotsWithAircraftPrivilege(aircraft_model)
        for pilot_license in pilot_licenses:
            print(pilot_license)
        print("\n")

    def print_work_summary(self):


        employeeSSN = input('Enter Employee SSN: ') 
        # Change this to employee name, even though this is easier,
        # from a user prespective nobody would want to 
        # remember a SSN of an employee.
        week_of = input('Enter Week of Work: ')

        work_procedures = self.LLAPI.GetWorkSummaryBySsn(employeeSSN, week_of)
        for voy in work_procedures:
            print(voy)
        
        
#test1 = EmployeeUI()
#test1.print_all_employees()
# test1.register_employee()
# test1.print_flight_attendants()
# test1.print_pilots()
# test1.print_pilots_with_aircraft_privilage()