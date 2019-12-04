from EmployeeLL import EmployeeLL
from AircraftLL import AircraftLL


class LLAPI:
    def __init__(self):
        self.employee_logic = EmployeeLL() # More logic layer classes to be added when implementation starts
        self.aircraft_logic = AircraftLL()    
    ##### EMPLOYEE API #####

    def ListPilots(self):
        return self.employee_logic.ListPilots()

    def ListFlightAttendants(self):
        return self.employee_logic.ListFlightAttendats()

    def ListAllEmployees(self):
        return self.employee_logic.ListAllEmployees()



    ##### VOYAGE API #####

    ##### DESTINATION API #####

    ##### AIRCRAFT API #####

