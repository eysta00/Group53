from Employee import Employee
from IOAPI import IOAPI
from datetime import datetime
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase
import dateutil.parser

class EmployeeLL:
    def __init__(self):
        self.data = IOAPI()

    def RegisterEmployee(self, name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str):
        try:
            self.data.addEmployee(Employee(name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str))
            return 1 #Just a status code to say if the call was successfull, successfull if >= 0
        except EntryInDatabase:
            return -1

    def ListPilots(self):
        employees = self.data.getAllEmployees()
        pilots = []
        for emp in employees:
            if emp.pilot_bool:
                pilots.append(emp)
        pilots.sort(key=lambda x: x.name) # sort the lists based on name
        return pilots

    def ListFlightAttendats(self):
        employees = self.data.getAllEmployees()
        flightAttendats = []
        for emp in employees:
            if not emp.pilot_bool:
                flightAttendats.append(emp)
        flightAttendats.sort(key=lambda x: x.name) # sort the lists based on name
        return flightAttendats

    def ListAllEmployees(self): # Lists all employees, first Pilots then flightAttendants
        pilots = self.ListPilots()
        flightAttendats = self.ListFlightAttendats()
        return pilots + flightAttendats


    def AddEmployee(self, name_str, ssn_str, address_str, phone_str, email_str, pilot_bool = False, planeType = None):
        employee = Employee(name_str, ssn_str, address_str, phone_str, email_str, pilot_bool, planeType)
        try:
            self.data.addEmployee(employee)
            return 1
        except EntryInDatabase:
            return -1

    def UpdateEmployeeInfo(self, ssn_str, name_str, address_str, phone_str, email_str, pilot_bool = False, planeType_id = None):
        employee = Employee(name_str, ssn_str, address_str, phone_str, email_str, pilot_bool, planeType_id)
        try:
            self.data.updateEmployee(employee)
            return 1
        except EntryNotInDatabase:
            return -1

    def ListUnassignedEmployees(self, date_iso): # not implemeted, to be implemented once datetime slides appear
        dateParced = dateutil.parser.parse(date)
        voyages = self.data.getAllVoyages()
        employees = self.data.getAllEmployees()
        #Not Complete


    def ListPilotsWithAircraftPrivilege(self, aircraft_model):
        pilots = self.ListPilots()
        model_pilots = []
        for pil in pilots:
            if pil.planeType == aircraft_model:
                model_pilots.append(pil)
        model_pilots.sort(key=lambda x: x.name)
        return model_pilots


if __name__ == "__main__":
    logic = EmployeeLL()
    # print(logic.ListPilots())
    # print(logic.ListFlightAttendats())
    # print(logic.ListAllEmployees())
    print(logic.ListUnassignedEmployees())