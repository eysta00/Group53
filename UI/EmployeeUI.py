from LogicLayer.LLAPI import LLAPI

class EmployeeUI:
    def __init__(self):
        self.LLAPI = LLAPI()
        self.EmployeeLL = self.LLAPI.employee_logic

    def register_employee(self):
        print("Register a new employee")
        e_name = input("Full employee name: ")
        e_ssn = input("Employee social securtiy number: ")
        e_address = input("Employee Adress: ")
        e_phone = input("Employe phone number: ")
        e_email = input("Employee email: ")
        
        e_pilot = input("Is employee a pilot? yes/no: ").lower()
        if e_pilot == "yes":
            e_pilot = True
        else:
            e_pilot = False
        e_planelicense = input("Employee plane license: ")
        error = self.LLAPI.RegisterEmployee(e_name, e_ssn, e_address, e_phone, e_email, e_pilot, e_planelicense)
        #print(error)
        if error != 1:
            print("Error, input not valid!")
        print("\n")
        
        return
    
    def print_all_employees(self):
        print("\tList all employess")
        all_employees = self.LLAPI.ListAllEmployees()
        for employee in all_employees:
            print(employee)
        print("\n")
        
    def print_flight_attendants(self):
        print("\tList all flight attendats")
        flight_attendants = self.LLAPI.ListFlightAttendants()
        for attendant in flight_attendants:
            print(attendant)
        print("\n")
    
    def print_pilots(self):
        print("List all pilots")
        all_pilots = self.LLAPI.ListPilots()
        for pilot in all_pilots:
            print(pilot)
        print("\n")
    
    def print_unassigned_employees():
        print("\tList all unassigned employees")


    def print_pilots_with_aircraft_privilage(self):
        print("\tList all pilots with a certain aircraft privilage")
        aircraft_model = input("Input aircraft model (case sensitive): ")
        pilot_licenses = self.LLAPI.ListPilotsWithAircraftPrivilege(aircraft_model)
        for pilot_license in pilot_licenses:
            print(pilot_license)
        print("\n")

    def print_work_summary(self):
        employeeSSN = input('Enter Employee SSN: ')
        week_of = input('Enter Week of Work: ')

        work_procedures = self.LLAPI.GetWorkSummary(employeeSSN, week_of)
        for voy in work_procedures:
            print(voy)
        
        
#test1 = EmployeeUI()
#test1.print_all_employees()
# test1.register_employee()
# test1.print_flight_attendants()
# test1.print_pilots()
# test1.print_pilots_with_aircraft_privilage()