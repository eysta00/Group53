from IO.DestinationIO import DestinationIO
from IO.VoyageIO import VoyageIO
from IO.AircraftIO import AircraftIO
from IO.EmployeesIO import EmployeesIO

from InstanceClasses.Destination import Destination
from InstanceClasses.Employee import Employee
from InstanceClasses.Voyage import Voyage
from InstanceClasses.Aircraft import Aircraft

from datetime import datetime
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase

class IOAPI():
    def __init__(self):
        self.DestinationData = DestinationIO('Data/DestinationData.csv')
        self.AircraftData = AircraftIO('Data/AircraftData.csv')
        self.EmployeeData = EmployeesIO('Data/EmployeeData.csv')
        self.VoyageData = VoyageIO('Data/VoyageData.csv')


    ##### EMPLOYEE API #####
    def getEmployeeBySSN(self, employee_ssn):
        return self.EmployeeData.getEmployeeBySSN(employee_ssn)

    def addEmployee(self, employee):
        return self.EmployeeData.addEmployee(employee)

    def updateEmployee(self, employee):
        return self.EmployeeData.updateEmployee(employee)

    def getAllEmployees(self):
        return self.EmployeeData.getAllEmployees()


    ##### DESTINATION API #####
    def getDestinationByDestinationID(self, destination_id):
        return self.DestinationData.getDestinationByDest_id(destination_id)

    def addDestination(self, destination):
        return self.DestinationData.addDestination(destination)

    def updateDestination(self, destination):
        return self.DestinationData.updateDestination(destination)

    def getAllDestinatons(self):
        return self.DestinationData.getAllDestinations()

    
    ##### VOYAGE API #####
    def getVoyageByVoyageID(self, voyageID):
        return self.VoyageData.getVoyageByVoyageID(voyageID)

    def addVoyage(self, voyage):
        return self.VoyageData.addVoyage(voyage)

    def updateVoyage(self, voyage):
        return self.VoyageData.updateVoyage(voyage)

    def getAllVoyages(self):
        return self.VoyageData.getAllVoyages()

    ##### AIRCRAFT API #####
    def getAircraftByAircraftID(self, aircraftID):
        return self.AircraftData.getAircraftByAircraftID(aircraftID)

    def addAircraft(self, aircraft):
        return self.AircraftData.addAircraft(aircraft)

    def updateAircraft(self, aircraft):
        return self.AircraftData.updateAircraft(aircraft)

    def getAllAircrafts(self):
        return self.AircraftData.getAllAircrafts()
    
    


if __name__ == "__main__":
    data = IOAPI()
    print(data.getEmployeeBySSN(1611982429))
    print(data.getDestinationByDestinationID(1))
    print(data.getVoyageByVoyageID(1))
    print(data.getAircraftByAircraftID(1))

    destination = Destination('Nuuk', 4, 1.4)
    employee = Employee('Jimmy', '0101001010', 'boolean Vil', '666', 'Jimmy@yahoo.com', None)
    aircraft = Aircraft(3, 'spitfire', 3)
    voyage = Voyage(3, 'Nuuk', datetime(2019, 12, 5, 12, 0, 0), 3)

    try:
        data.addDestination(destination)
    except EntryInDatabase:
        print('destination already in database')

    try:
        data.addEmployee(employee)
    except EntryInDatabase:
        print('employee already in database')

    try:
        data.addAircraft(aircraft)
    except EntryInDatabase:
        print('aircraft already in database')

    try:
        data.addVoyage(voyage)
    except EntryInDatabase:
        print('voyage already in database')


    data.updateDestination(destination)
    data.updateEmployee(employee)
    data.updateAircraft(aircraft)
    data.updateVoyage(voyage)


    print(data.getAllDestinatons())
    print(data.getAllEmployees())
    print(data.getAllAircrafts())
    print(data.getAllVoyages())
    
    