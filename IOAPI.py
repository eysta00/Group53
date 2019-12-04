from DestinationIO import DestinationIO
from VoyageIO import VoyageIO
from AircraftsIO import AircraftsIO
from EmployeesIO import EmployeesIO

class IOAPI():
    def __init__(self):
        self.DestinationData = DestinationIO('Data/DestinationData.csv')
        self.AircraftData = AircraftsIO('Data/AircraftData.csv')
        self.EmployeeData = EmployeesIO('Data/EmployeeData.csv')
        self.VoyageData = VoyageIO('Data/VoyageData.csv')


    ##### EMPLOYEE API #####
    def getEmployeeBySSN(employee_ssn):
        return self.EmployeeData.GetEmployeeBySSN

    def addEmployee(employee):
        return self.EmployeeData.addEmployee(employee)

    def updateEmployee(employee):
        return self.EmployeeData.updateEmployee(employee)


    ##### DESTINATION API #####
    def getDestinationByDestinationID(destination_id):
        return self.DestinationData.getDestinationByDest_id(destination_id)

    def addDestination(destination):
        return self.DestinationData.addDestination(destination)

    def updateDestination(destination):
        return self.DestinationData.updateDestination

    
    ##### VOYAGE API #####
    def getVoyageByVoyageID(voyageID):
        return self.VoyageData.getVoyageByVoyageID(voyageID)

    def addVoyage(voyage):
        return self.VoyageData.addVoyage(voyage)

    def updateVoyage(voyage):
        return self.VoyageData.updateVoyage(voyage)


    ##### AIRCRAFT API #####