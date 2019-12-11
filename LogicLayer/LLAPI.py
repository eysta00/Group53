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

    def getVoyageByVoyageID(self, voyageID):
        return self.voyage_logic.getVoyageByVoyageID(voyageID)

    def AddStaffToVoyage(self, voyage_ID, employee_SSN):
        return self.voyage_logic.AddStaffToVoyage(voyage_ID, employee_SSN)
    
    def AssignAircraftToVoyge(self, voyageID, aircraftID):
        return self.voyage_logic.assignAircraftToVoyage(voyageID, aircraftID)

    def ListVoyagePilots(self, voyageID):
        return self.voyage_logic.ListVoyagePilots(voyageID)

    def ListVoyageFlightAttendants(self, voyageID):
        return self.voyage_logic.ListVoyageFlightAttendants(voyageID)

    def UpdateVoyageCaptain(self,voyageID, pilotSSN):
        return self.voyage_logic.UpdateVoyageCaptain(voyageID, pilotSSN)

    def SellSeatsForVoyage(self, voyageID, seatsSold):
        return self.voyage_logic.SellSeatsForVoyage(voyageID, seatsSold)

    ##### DESTINATION API #####

    def ListAllDestinations(self):
        return self.destination_logic.ListAllDestinations()

    def RegisterDestination(self, dest_name_str, dest_id_int, flight_duration_double):
        return self.destination_logic.RegisterDestination(dest_name_str, dest_id_int, flight_duration_double)

    def UpdateDestinationContactNumber(self, destinationID, contactNr):
        return self.destination_logic.UpdateDestinationContactNumber(destinationID, contactNr)

    ##### AIRCRAFT API #####

    def RegisterAircraft(self, Id_str, model_str, totalseats_str):
        return self.aircraft_logic.RegisterAircraft(Id_str, model_str, totalseats_str)

    def ListAllAircrafts(self):
        return self.aircraft_logic.ListAllAircrafts()

    def ListAllAircrafts(self):
        return self.aircraft_logic.ListAllAircrafts()

    def AircraftStatus(self, aircraftID):
        return self.aircraft_logic.AircraftStatus(aircraftID)

    def ShowStatusOfAircrafts(self):
        return self.aircraft_logic.ShowStatusOfAircrafts()
        

if __name__ == "__main__":
    api = LLAPI()