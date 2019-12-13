from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.AircraftLL import AircraftLL
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.AircraftLL import AircraftLL
from LogicLayer.VoyageLL import VoyageLL


class LLAPI:
    def __init__(self):
        self.employee_logic = EmployeeLL() 
        self.aircraft_logic = AircraftLL()    
        self.destination_logic = DestinationLL()
        self.voyage_logic = VoyageLL()


    ##### EMPLOYEE API #####

    def UpdateEmployeeInfo(self, employee):
        return self.employee_logic.UpdateEmployeeInfo(employee)

    def GetEmployeeBySSN(self, ssn):
        return self.employee_logic.GetEmployeeBySSN(ssn)

    def RegisterEmployee(self, name, ssn, address, phone, email, pilot, planelicense):
        return self.employee_logic.RegisterEmployee(name, ssn, address, phone, email, pilot, planelicense)

    def ListPilots(self):
        return self.employee_logic.ListPilots()

    def ListFlightAttendants(self):
        return self.employee_logic.ListFlightAttendats()

    def ListAllEmployees(self):
        return self.employee_logic.ListAllEmployees()
    
    def ListPilotsWithAircraftPrivilege(self, aircraft_model):
        return self.employee_logic.ListPilotsWithAircraftPrivilege(aircraft_model)

    def ListUnassignedEmployees(self, date_iso):
        return self.employee_logic.ListUnassignedEmployees(date_iso)
    
    def ListAssignedEmployees(self, date_iso):
        return self.employee_logic.ListAssignedEmployees(date_iso)

    def ListAllEmployeesWithName(self, name):
        return self.employee_logic.ListAllEmployeesWithName(name)

    def GetWorkSummary(self, employeeSSN, current_date):
        return self.employee_logic.GetWorkSummaryBySsn(self ,employeeSSN, current_date)

    ##### VOYAGE API #####

    def UpdateVoyageHeadFlightAttendant(self, voyageID, flightAttendantSSN):
        return self.voyage_logic.UpdateVoyageHeadFlightAttendant(voyageID, flightAttendantSSN)

    def AddVoyage(self, destination_id, flightTime_str):
        return self.voyage_logic.addVoyage(self, destination_id, flightTime_str)

    def AddRecurringVoyages(self, destination_id, flightTime_str, dayInterval_int, quantity_int):
        return self.voyage_logic.AddRecurringVoyages(self, destination_id, flightTime_str, dayInterval_int, quantity_int)

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

    def SellSeatsForVoyageOutgoing(self, voyageID, seatsSold):
        return self.voyage_logic.SellSeatsForVoyageOutgoing(voyageID, seatsSold)

    def SellSeatsForVoyageIncoming(self, voyageID, seatsSold):
        return self.voyage_logic.SellSeatsForVoyageIncoming(voyageID, seatsSold)
    
    def ListAllVoyages(self):
        return self.voyage_logic.ListAllVoyages()

    def ListUpcomingVoyages(self):
        return self.voyage_logic.ListUpcomingVoyages()

    def ListVoyagesForGivenDay(self, date_iso):
        return self.voyage_logic.ListVoyagesForGivenDay(date_iso)

    def ListVoyagesForGivenWeek(self, date_iso):
        return self.voyage_logic.ListVoyagesForGivenWeek(date_iso)

    def ListVoyagesForDestination(self, dest_id):
        return self.voyage_logic.ListVoyagesForDestination(dest_id)

    def IsFullyStaffed(self, voyage):
        return self.voyage_logic.IsFullyStaffed(voyage)

    def GetVoyageStatus(self, voyage):
        return self.voyage_logic.GetVoyageStatus(voyage)

    ##### DESTINATION API #####

    def GetDestinationByDestinationID(self, destinationID):
        return self.destination_logic.GetDestinationByDestinationID(destinationID)

    def ListAllDestinations(self):
        return self.destination_logic.ListAllDestinations()

    def RegisterDestination(self, country_str, airport_str, flight_duration, distanceFromReykjavik, contactName_str, contactNr_str):
        return self.destination_logic.RegisterDestination(country_str, airport_str, flight_duration, distanceFromReykjavik, contactName_str, contactNr_str)

    def UpdateDestinationContactNumber(self, destinationID, contactNr):
        return self.destination_logic.UpdateDestinationContactNumber(destinationID, contactNr)

    def MostPopularDestination(self):
        return self.destination_logic.MostPopularDestination()

    ##### AIRCRAFT API #####

    def RegisterAircraft(self, manufacturer_str, model_str, totalSeats_str):
        return self.aircraft_logic.RegisterAircraft(manufacturer_str, model_str, totalSeats_str)

    def ListAllAircrafts(self):
        return self.aircraft_logic.ListAllAircrafts()

    def AircraftStatus(self, aircraftID, time_iso):
        return self.aircraft_logic.AircraftStatus(aircraftID, time_iso)

    def ShowStatusOfAircrafts(self):
        return self.aircraft_logic.ShowStatusOfAircrafts()

    def ListAvailableAircrafts(self, time):
        return self.aircraft_logic.ListAvailableAircrafts(time)
        

if __name__ == "__main__":
    api = LLAPI()