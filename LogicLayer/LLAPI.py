from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.AircraftLL import AircraftLL
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.AircraftLL import AircraftLL
from LogicLayer.VoyageLL import VoyageLL


class LLAPI:
    def __init__(self):
        self.employee_logic = EmployeeLL() # More logic layer classes to be added when implementation starts
        self.aircraft_logic = AircraftLL()    
        self.destination_logic = DestinationLL()
        self.voyage_logic = VoyageLL()


    ##### EMPLOYEE API #####

    def ListPilots(self):
        return self.employee_logic.ListPilots()

    def ListFlightAttendants(self):
        return self.employee_logic.ListFlightAttendats()

    def ListAllEmployees(self):
        return self.employee_logic.ListAllEmployees()

    def ListUnassignedEmployees(self, date_iso):
        return self.employee_logic.ListUnassignedEmployees(date_iso)
    
    def ListAssignedEmployees(self, date_iso):
        return self.employee_logic.ListAssignedEmployees(date_iso)

    

    ##### VOYAGE API #####

    def AddVoyage(self, destination_id, flightTime_str):
        return self.voyage_logic.addVoyage(destination_id, flightTime_str)


    def AddStaffToVoyage(self, voyage_ID, employee_SSN):
        return self.voyage_logic.AddStaffToVoyage(voyage_ID, employee_SSN)

    ##### DESTINATION API #####

    def ListAllDestinations(self):
        return self.destination_logic.ListAllDestinations()

    def RegisterDestination(self, dest_name_str, dest_id_int, flight_duration_double):
        return self.destination_logic.RegisterDestination(dest_name_str, dest_id_int, flight_duration_double)

    ##### AIRCRAFT API #####

    def RegisterAircraft(self, Id_str, model_str, totalseats_str):
        return self.aircraft_logic.RegisterAircraft(Id_str, model_str, totalseats_str)

    def ListAllAircrafts(self):
        return self.aircraft_logic.ListAllAircrafts()

    def ListAllAircrafts(self):
        return self.aircraft_logic.ListAllAircrafts()
        

if __name__ == "__main__":
    api = LLAPI()