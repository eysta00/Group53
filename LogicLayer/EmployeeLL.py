from InstanceClasses.Employee import Employee
from IO.IOAPI import IOAPI
from datetime import datetime
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase
from dateutil.parser import *
from dateutil.relativedelta import *
# from dateutil.parser import *

class EmployeeLL:
    def __init__(self):
        self.data = IOAPI()

    def RegisterEmployee(self, name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str):
        try:
            self.data.addEmployee(Employee(name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str))
            return 1 #Just a status code to say if the call was successfull, successfull if >= 0
        except EntryInDatabase:
            return -1

    def GetEmployeeBySSN(self, ssn):
        return self.data.GetEmployeeBySSN(ssn)

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

    def ListAllEmployeesWithName(self, name):
        employees = self.data.getAllEmployees()
        ret_lst = []  
        for emp in employees:
            if emp.name == name:
                ret_lst.append(emp)
        return ret_lst


    def AddEmployee(self, name_str, ssn_str, address_str, phone_str, email_str, pilot_bool = False, planeType = None):
        employee = Employee(name_str, ssn_str, address_str, phone_str, email_str, pilot_bool, planeType)
        try:
            self.data.addEmployee(employee)
            return 1
        except EntryInDatabase:
            return -1

    def UpdateEmployeeInfo(self, employee):
        try:
            self.data.updateEmployee(employee)
            return 1
        except EntryNotInDatabase:
            return -1

    def ListUnassignedEmployees(self, date_iso): # not implemeted, to be implemented once datetime slides appear
        dateParced = parse(date_iso)
        voyages = self.data.getAllVoyages()
        employees = self.data.getAllEmployees()
        unassigned_employees = []
        for emp in employees:
            assigned = False
            for voy in voyages:
                if emp.ssn in voy.pilots_lst or emp.ssn in voy.flightAttendants_lst:
                    parsedStartTime = parse(voy.departureTime)
                    parsedEndTime = parse(self._getEndTimeOfVoyage(voy))

                    # testing if the departure or the return date are on the tested date
                
                    assigned = assigned or (((dateParced.year == parsedStartTime.year and dateParced.month == parsedStartTime.month and dateParced.day == parsedStartTime.day)\
                        and (dateParced.year == parsedEndTime.year and dateParced.month == parsedEndTime.month and dateParced.day == parsedEndTime.day)))
                

            if not assigned:
                unassigned_employees.append(emp)
        return unassigned_employees

    def ListAssignedEmployees(self, date_iso): 
        dateParced = parse(date_iso)
        voyages = self.data.getAllVoyages()
        employees = self.data.getAllEmployees()
        assigned_employees = []
        for emp in employees:
            assigned = False
            for voy in voyages:
                if emp.ssn in voy.pilots_lst or emp.ssn in voy.flightAttendants_lst:
                    parsedStartTime = parse(voy.departureTime)
                    parsedEndTime = parse(self._getEndTimeOfVoyage(voy))

                    # testing if the departure or the return date are on the tested date
                
                    assigned = assigned or ((dateParced.year == parsedStartTime.year and dateParced.month == parsedStartTime.month and dateParced.day == parsedStartTime.day)\
                        and (dateParced.year == parsedEndTime.year and dateParced.month == parsedEndTime.month and dateParced.day == parsedEndTime.day))
                

            if assigned:
                assigned_employees.append(emp)
        return assigned_employees


    def ListPilotsWithAircraftPrivilege(self, aircraft_model):
        pilots = self.ListPilots()
        model_pilots = []
        for pil in pilots:
            if pil.planeType == aircraft_model:
                model_pilots.append(pil)
        model_pilots.sort(key=lambda x: x.name)
        return model_pilots

    def _getEndTimeOfVoyage(self, voyage):
        destination = self.data.getDestinationByDestinationID(voyage.destination)
        # try:
        #     StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S.%f')
        # except ValueError:
        #     StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S')

        StartTime_dateTime = parse(voyage.departureTime)

        flightTimeHours = float(destination.flight_duration)
        flightTimeMinutes = (flightTimeHours % 1) * 60
        flightTimeSeconds = (flightTimeMinutes % 1) * 60
        flightTimeHours = int(flightTimeHours)
        flightTimeMinutes = int(flightTimeMinutes)
        flightTimeSeconds = int(flightTimeSeconds)
        # print(flightTime)
        endTime = StartTime_dateTime + relativedelta(hours= +(flightTimeHours*2+1), minutes = +2*flightTimeMinutes, seconds = +2*flightTimeSeconds)
        return endTime.isoformat()
        
    # def _getEndTimeOfVoyage(self, voyage):
    #     destination = self.data.getDestinationByDestinationID(voyage.destination)
    #     try:
    #         StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S.%f')
    #     except ValueError:
    #         StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S')

    #     flightTime = int(destination.flight_duration) # consider changing this to int so as to not miss the disimal places!
    #     # print(flightTime)
    #     return parse((StartTime_dateTime + relativedelta(hour=+(flightTime*2+1))).isoformat()) # Assuming the rest at destination is 1 hour


    def GetWorkSummaryBySsn(self, employeeSSN, current_date):
        voyages_in_week = VoyageLL().ListVoyagesForGivenWeek(current_date)
        emp_voyages = []

        for voyage in voyages_in_week:
            if employeeSSN in voyage.pilots_lst:
                emp_voyages.append(voyage)

        return emp_voyages

        #not finished implementing

if __name__ == "__main__":
    logic = EmployeeLL()
    # print(logic.ListPilots())
    # print(logic.ListFlightAttendats())
    # print(logic.ListAllEmployees())
    time = datetime(2019, 12, 8, 18, 0, 0).isoformat()
    print(logic.ListAssignedEmployees(time))