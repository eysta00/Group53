from LogicLayer.LLAPI import LLAPI
from datetime import datetime
from Exceptions.Exceptions import *
import os
class EmployeeUI:
    def __init__(self):
        self.LLAPI = LLAPI()
        self.header = "{:40}\t{:10}\t{:20}\t{:10}\t{:35}\t{:20}\t{}".format("Name", "SSN", "Address", "Phone", "Email", "Pilot status", "Licenses")

    def print_register_employee(self):
        rows_len, columns_len = os.get_terminal_size() # checks on length of terminal, this repeats.

        print("\n\tRegister a new employee")
        print("-" * (rows_len - 1))
        e_name = input("Full employee name: ")
        e_ssn = input("Employee social securtiy number: ")
        e_address = input("Employee Address: ")
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
        print(("-" * (int((rows_len - 24) / 2))) + "New Employee Registered" + ("-" * ((int((rows_len -24) / 2)))))
        print(self.header)
        print("-" * (rows_len - 1))
        new_employee = self.LLAPI.GetEmployeeBySSN(e_ssn)
        print(new_employee)
        print("-" * (rows_len - 1))
        print("\n")
        return
    
    def print_all_employees(self):
        rows_len, columns_len = os.get_terminal_size()

        print("\n\tList all employess\n")

        print(self.header)
        all_employees = self.LLAPI.ListAllEmployees()
        for employee in all_employees:
            print("-" * (rows_len - 1))
            print(employee)
            
        print("\n")
        
    def print_flight_attendants(self):
        rows_len, columns_len = os.get_terminal_size()

        print("\n\tList all flight attendants")
        print("-" * (rows_len-1))
        print(self.header)
        flight_attendants = self.LLAPI.ListFlightAttendants()
        for attendant in flight_attendants:
            print("-" * (rows_len-1))
            print(attendant)
        print("\n")
    
    def print_pilots(self):
        rows_len, columns_len = os.get_terminal_size()


        print("\n\tList all pilots")
        print("-" * (rows_len - 1))
        print(self.header)

        all_pilots = self.LLAPI.ListPilots()
        for pilot in all_pilots:
            print("-" * (rows_len - 1))
            print(pilot)
        print("\n")
    
    def print_assigned_employees(self):
        rows_len, columns_len = os.get_terminal_size()

        print("\n\tList all already assigned employees on a given day")
        year = int(input("Input year: "))
        month = int(input("Input month: "))
        day = int(input("Input day: "))
        date_iso = datetime(year, month, day).isoformat()
        assinged_employees = self.LLAPI.ListAssignedEmployees(date_iso)
        if len(assinged_employees) < 1:
            print("\nThere are no employees assigned on the imputed day ")
        else:
            print(self.header)
            print("-" * (rows_len - 1))
            for employee in assinged_employees:
                print("-" * (rows_len - 1))
                print(employee)
        print("\n")

    
    def print_unassigned_employees(self):
        rows_len, columns_len = os.get_terminal_size()
        
        print("\n\tList all unassigned employees on a given day")
        year = int(input("Input year: "))
        month = int(input("Input month: "))
        day = int(input("Input day: "))
        date_iso = datetime(year, month, day).isoformat()
        unassinged_employees = self.LLAPI.ListUnassignedEmployees(date_iso)
        if len(unassinged_employees) < 1:
            print("There are no employees that are unassigned")
        else:
            print(self.header)
            print("-" * (rows_len - 1))
            for employee in unassinged_employees:
                print("-" * (rows_len - 1))
                print(employee)
        
        print("\n")

    def print_update_employee_infomation(self):
        try:
            finalize = True
            rows_len, columns_len = os.get_terminal_size()
            print("\n\tUpdate employee information")
            employee_name = input("Input name of employee you want to update: ")
            employees_with_name = self.LLAPI.ListAllEmployeesWithName(employee_name)
            # If there are more employees with same name you get a list and have to select manually the ssn of the employee.
            if len(employees_with_name) > 1:
                print("More than one employee was found with that name")
                print("-" * (rows_len - 1))
                print(self.header)
                print("-" * (rows_len - 1))
                for employee in employees_with_name:
                    print(employee)
                    print("-" * (rows_len - 1))
                employee_ssn = input("Please input the ssn of employee you want to update: ")
                
                employee = self.LLAPI.GetEmployeeBySSN(employee_ssn)
                print("What would you like to change?\n")
                while finalize:
                    print("\t1. Address",
                    "\n\t2. Phone number ",
                    "\n\t3. Email",
                    "\n\t4. Pilot status",
                    "\n\t5. Plane license\n")
                    command_index = int(input("Please input a number: "))
                    if command_index == 1:
                        employee.address = input("New employee Address: ")
                    elif command_index == 2:
                        employee.phone = input("New employee phone number: ")
                    elif command_index == 3:
                        employee.email = input("New employee email address: ")
                    elif command_index == 4:
                        pilot_str = input("Is employee a Pilot? yes/no: ").lower()
                        if pilot_str == "yes":
                            employee.pilot_bool = True
                            employee.license = input("Employee plane license: ")
                        else:
                            employee.pilot_bool = False
                    elif command_index == 5:
                        employee.planeType = input("New plane license: ")
                    finalize_changes = input("Would you like to finalze your changes? yes/no: ").lower()
                    if finalize_changes == "yes":
                        finalize = False
                    else:
                        finalize = True
            # If there is only one employee with the name requested it goes straight to asking what would user want to change
            elif len(employees_with_name) == 1:
                employee = self.LLAPI.GetEmployeeBySSN(employees_with_name[0].ssn)
                print("What would you like to change?\n")
                while finalize:
                    print("\t1. Address",
                    "\n\t2. Phone number ",
                    "\n\t3. Email",
                    "\n\t4. Pilot status",
                    "\n\t5. Plane license\n")
                    command_index = int(input("Please input a number: "))
                    if command_index == 1:
                        employee.address = input("New employee Address: ")
                    elif command_index == 2:
                        employee.phone = input("New employee phone number: ")
                    elif command_index == 3:
                        employee.email = input("New employee email address: ")
                    elif command_index == 4:
                        pilot_str = input("Is employee a Pilot? yes/no: ").lower()
                        if pilot_str == "yes":
                            employee.pilot_bool = True
                            employee.license = input("Employee plane license: ")
                        else:
                            employee.pilot_bool = False
                    elif command_index == 5:
                        employee.planeType = input("New plane license: ")
                    finalize_changes = input("Would you like to finalze your changes? yes/no: ").lower()
                    if finalize_changes == "yes":
                        finalize = False
                    else:
                        finalize = True
            else:
                print("No employee with that name was found")

            self.LLAPI.UpdateEmployeeInfo(employee)

            return
        except EntryNotInDatabase:
            print("ERROR! Employee not found, please input correct ssn")
        except AttributeError:
            print("ERROR! you put in the wrong ssn! please try again")
            return



    def print_pilots_with_aircraft_privilage(self):
        rows_len, columns_len = os.get_terminal_size()

        print("\n\tList all pilots with a certain aircraft privilage")
        aircraft_model = input("Input aircraft model (case sensitive): ")
        pilot_licenses = self.LLAPI.ListPilotsWithAircraftPrivilege(aircraft_model)
        print(self.header)
        print("-" * (rows_len - 1))
        for pilot_license in pilot_licenses:
            print(pilot_license)
            print("-" * (rows_len - 1))
        print("\n")

    def print_work_summary(self):
        rows_len, columns_len = os.get_terminal_size()

        print("\n\tGet the work summary of an employee")

        try:
            employee_name = input("Input employee name: ")
            employees_with_name = self.LLAPI.ListAllEmployeesWithName(employee_name)
            if len(employees_with_name) > 1:
                print("More than one employee has that same name")
                print("-" * (rows_len - 1))
                print(self.header)
                print("-" * (rows_len - 1))
                for employee in employees_with_name:
                    print(employee)
                    print("-" * (rows_len - 1))

                employee_ssn = input("Input the ssn of employee you requested: ")

            else:
                employee_ssn = employees_with_name[0].ssn
            print("Please input the dates to get the work summary of", employee_name)
            year = int(input("Input year: "))
            month = int(input("Input month: "))
            day = int(input("Input day: "))
            date_iso = datetime(year, month, day).isoformat()
            work_procedures = self.LLAPI.GetWorkSummary(employees_with_name[0].ssn, date_iso)
            if len(work_procedures) > 0:
                for voy in work_procedures:
                    print("-" * (rows_len - 1))
                    print("Destination: ", voy.destination, "\tDeparture: ", voy.departureTime)
                    print("Aircraft ID: ", voy.aircraftID, "\tCaptain of Aircraft: ", voy.captain)
                    print("Incoming flight ID: ", voy.incomingFlightID, "\tOutgoing flight ID: ", voy.outgoingFlightID)
                    print("Flight Attendants: ",voy.flightAttendants_lst,"\nPilots: " ,voy.pilots_lst)
                    print("-" * (rows_len - 1))
            else:
                print("\nNo work procedures were found")



        except EntryNotInDatabase:
            print("\nThere is No employee with the name " + employee_name)

        except ValueError:
            print('\nDates must be within defined ranges, months 1-12, days 1-31.\n')

    def print_specific_employee(self):
        try:
            employee_name = input('Input employee name: ')
            employees_with_name = self.LLAPI.ListAllEmployeesWithName(employee_name)
            print("{:30}\t{:10}\t{:20}\t{:10}\t{:25}\t{:20}\t{}".format("Name", "SSN", "Address", "Phone", "Email", "Pilot status", "Licenses"))
            emp_id = str(employees_with_name)[-11:-1]
            emp = self.LLAPI.GetEmployeeBySSN(emp_id)
            if emp.pilot_bool:
                pilot = "True"
            else:
                pilot = "False"
            print("{:30}\t{:10}\t{:20}\t{:10}\t{:25}\t{:20}\t{}".format(emp.name, emp.ssn, emp.address, emp.phone, emp.email, pilot, emp.planeType))
        except EntryNotInDatabase:
            print("\nThere is No employee with the name " + employee_name)
