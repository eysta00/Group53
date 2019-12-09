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

    ##### VOYAGE API #####

    def ListAllAircrafts(self):
        Aircrafts = self.aircraft_logic.ListAllAircrafts()
        Aircrafts.sort(key = lambda x: x.model)
        return Aircrafts

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


if __name__ == "__main__":
    api = LLAPI()