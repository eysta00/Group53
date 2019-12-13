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


# Method to register a new employee
    def RegisterEmployee(self, name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str):
        try:
            self.data.addEmployee(Employee(name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str))
            return 1 #Just a status code to say if the call was successfull, successfull if >= 0
        except EntryInDatabase:
            return -1

# Method to get an employee be its ssn
    def GetEmployeeBySSN(self, ssn):
        return self.data.getEmployeeBySSN(ssn)


# Method to get a list of all the pilots
    def ListPilots(self):
        employees = self.data.getAllEmployees()
        pilots = []
        for emp in employees:
            if emp.pilot_bool:
                pilots.append(emp)
        pilots.sort(key=lambda x: x.name) # sort the lists based on name
        return pilots

# Method to get a list of all flight attendants
    def ListFlightAttendats(self):
        employees = self.data.getAllEmployees()
        flightAttendats = []
        for emp in employees:
            if not emp.pilot_bool:
                flightAttendats.append(emp)
        flightAttendats.sort(key=lambda x: x.name) # sort the lists based on name
        return flightAttendats

# Method to list all the employees sorted by name and divided by position
    def ListAllEmployees(self): # Lists all employees, first Pilots then flightAttendants
        pilots = self.ListPilots()
        flightAttendats = self.ListFlightAttendats()
        return pilots + flightAttendats


# Method to list all employees that have a name containing the input
    def ListAllEmployeesWithName(self, name):
        employees = self.data.getAllEmployees()
        ret_lst = []  
        for emp in employees:
            if name in emp.name:
                ret_lst.append(emp)
        if len(ret_lst) == 0:
            raise EntryNotInDatabase('There is no employee with that name') 
        return ret_lst

# Method to update an employee
    def UpdateEmployeeInfo(self, employee):
        try:
            self.data.updateEmployee(employee)
            return 1
        except EntryNotInDatabase:
            return -1


# Method to list all unassigned employees in the system for a certain date
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
        unassigned_employees.sort(key=lambda x: x.name)
        unassigned_employees.sort(key=lambda x: x.pilot_bool, reverse = True)
        return unassigned_employees


# Method to list all assigned Employees
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

# Method to list all pilots with a priveledge to a certain aircraft model
    def ListPilotsWithAircraftPrivilege(self, aircraft_model):
        pilots = self.ListPilots()
        model_pilots = []
        for pil in pilots:
            if pil.planeType == aircraft_model:
                model_pilots.append(pil)
        model_pilots.sort(key=lambda x: x.name)
        return model_pilots

# Method to get the End time of a voyage
    def _getEndTimeOfVoyage(self, voyage):
        destination = self.data.getDestinationByDestinationID(voyage.destination)

        StartTime_dateTime = parse(voyage.departureTime)

        flightTimeHours = float(destination.flight_duration)
        flightTimeMinutes = (flightTimeHours % 1) * 60
        flightTimeSeconds = (flightTimeMinutes % 1) * 60
        flightTimeHours = int(flightTimeHours)
        flightTimeMinutes = int(flightTimeMinutes)
        flightTimeSeconds = int(flightTimeSeconds)
        endTime = StartTime_dateTime + relativedelta(hours= +(flightTimeHours*2+1), minutes = +2*flightTimeMinutes, seconds = +2*flightTimeSeconds)
        return endTime.isoformat()
        
# Method to get a work summary of an employee by ssn
    def GetWorkSummaryBySsn(self, apiSelf, employeeSSN, current_date):
        voyages_in_week = apiSelf.ListVoyagesForGivenWeek(current_date)
        emp_voyages = []

        for voyage in voyages_in_week:
            if employeeSSN in voyage.pilots_lst or employeeSSN in voyage.flightAttendants_lst:
                emp_voyages.append(voyage)

        return emp_voyages


if __name__ == "__main__":
    logic = EmployeeLL()
    # print(logic.ListPilots())
    # print(logic.ListFlightAttendats())
    # print(logic.ListAllEmployees())
    time = datetime(2019, 12, 8, 18, 0, 0).isoformat()
    print(logic.ListAssignedEmployees(time))