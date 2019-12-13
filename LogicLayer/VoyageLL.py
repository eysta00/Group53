from InstanceClasses.Voyage import Voyage
from Exceptions.Exceptions import *
from IO.IOAPI import IOAPI
import dateutil.parser
from datetime import datetime
from dateutil.parser import *
from dateutil.relativedelta import *


class VoyageLL:
    def __init__(self):
        self.data = IOAPI()


# Method to list all voyages in the system
    def ListAllVoyages(self):
        voyages = self.data.getAllVoyages()
        return voyages

# Method to list all upcoming voyages
    def ListUpcomingVoyages(self):
        voyages = self.data.getAllVoyages()
        nowParsed = datetime.now()
        upcomingVoyages = []
        for voy in voyages:
            parsedTime = parse(voy.departureTime)
            if parsedTime > nowParsed:
                upcomingVoyages.append(voy)
        upcomingVoyages.sort(key=lambda x: parse(x.departureTime))
        return upcomingVoyages


# Method to get a specifiv voyage by voyage id
    def getVoyageByVoyageID(self, voyageID):
        return self.data.getVoyageByVoyageID(voyageID)


# Method to add staff to a voyage
    def AddStaffToVoyage(self, voyageID, employeeSSN): 

        voyage = self.data.getVoyageByVoyageID(voyageID)
        if voyage.aircraftID == '' or voyage.aircraftID == None:
            raise AircraftNotRegistered
        employee = self.data.getEmployeeBySSN(employeeSSN)
        try:
            aircraft = self.data.getAircraftByAircraftID(voyage.aircraftID)
        except EntryNotInDatabase:
            raise AircraftNotRegistered
        
        
        if str(employeeSSN) in voyage.pilots_lst or str(employeeSSN) in voyage.flightAttendants_lst:
            raise EmployeeAlreadyAssigned('This employee is already assigned to this voyage')

        if employee.pilot_bool:
            if employee.planeType != aircraft.model:
                print('hi')
            voyage.pilots_lst.append(employeeSSN)
        else:    
            voyage.flightAttendants_lst.append(employeeSSN)

        self.data.updateVoyage(voyage)


# Method to assign an aircraft to a voyage
    def assignAircraftToVoyage(self, voyageID, aircraftID):
        
        voyage = self.data.getVoyageByVoyageID(voyageID)
        voyage.aircraftID = aircraftID
        self.data.updateVoyage(voyage)
        

# Method to add voyage to the system
    def addVoyage(self, apiself, destination_id, flightTime_str):
        

        if not self._isDepartureTimeFree(flightTime_str):
            raise DepartureTimeOccupied('There is already a flight at that time')

        freeEmployees = apiself.ListUnassignedEmployees(flightTime_str)
        freePilots = 0
        freeFlightAttendants = 0
        for emp in freeEmployees:
            if emp.pilot_bool:
                freePilots += 1
            else:
                freeFlightAttendants += 1
        
        if freePilots < 2 or freeFlightAttendants < 1:
            raise ToFewAvailableEmployees("There are not enough available employees on this date to create a voyage")

        
        flightIDs_lst_str = self._GenerateFlightID(destination_id, flightTime_str)
        voyage = Voyage(self._GenerateNewVoyageID(), destination_id, flightTime_str, outgoingFlightID=flightIDs_lst_str[0], incomingFlightID=flightIDs_lst_str[1])
        self.data.addVoyage(voyage)
        
    # Method to add recuring voyages
    def AddRecurringVoyages(self, apiself, destination_id, flightTime_str, dayInterval_int, quantity_int):
        parsedTime = parse(flightTime_str)
        deltaTime = relativedelta(days = +dayInterval_int)

        for _ in range(quantity_int):
            self.addVoyage(apiself, destination_id, parsedTime.isoformat())
            parsedTime = parsedTime + deltaTime
        return

        

# List all voyages for a given day
    def ListVoyagesForGivenDay(self, date_iso):
        voyages = self.data.getAllVoyages()
        voyagesOnDay_lst = []
        dateParced = parse(date_iso)
        for voy in voyages:
            parsedStartTime = parse(voy.departureTime)
            parsedEndTime = parse(self._getEndTimeOfVoyage(voy))

            if ((dateParced.year == parsedStartTime.year and dateParced.month == parsedStartTime.month and dateParced.day == parsedStartTime.day)\
                and (dateParced.year == parsedEndTime.year and dateParced.month == parsedEndTime.month and dateParced.day == parsedEndTime.day)):
                voyagesOnDay_lst.append(voy)
        return voyagesOnDay_lst
            
# list all voyages in the upcoming week
    def ListVoyagesForGivenWeek(self, date_iso): # the input date is the first day in the week
        voyages = self.data.getAllVoyages()
        voyagesInWeek_lst = []
        dateParced = parse(date_iso)
        weekLaterParced = dateParced + relativedelta(days=+7)
        for voy in voyages:
            parsedStartTime = parse(voy.departureTime)
            parsedEndTime = parse(self._getEndTimeOfVoyage(voy))
            if (parsedEndTime > dateParced and parsedEndTime < weekLaterParced) or (parsedStartTime > dateParced and parsedStartTime < weekLaterParced):
                voyagesInWeek_lst.append(voy)
        return voyagesInWeek_lst

# List all pilots for a voyage
    def ListVoyagePilots(self, voyageID):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        pilotsSSN_lst = voyage.pilots_lst
        pilots_emp = []
        for pilotSSN in pilotsSSN_lst:
            pilots_emp.append(self.data.getEmployeeBySSN(pilotSSN))
        return pilots_emp

# list all flightattendants for a voyage
    def ListVoyageFlightAttendants(self, voyageID):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        flightAttendantsSSN_lst = voyage.flightAttendants_lst
        flightAttendats_emp = []
        for flightAttendatSSN in flightAttendantsSSN_lst:
            flightAttendats_emp.append(self.data.getEmployeeBySSN(flightAttendatSSN))
        return flightAttendats_emp

# update the voyage captain
    def UpdateVoyageCaptain(self,voyageID, pilotSSN):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        voyage.captain = pilotSSN
        self.data.updateVoyage(voyage)

# update the head flight attendant for the voyage
    def UpdateVoyageHeadFlightAttendant(self, voyageID, flightAttendantSSN):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        voyage.headFlightAttendant = flightAttendantSSN 
        self.data.updateVoyage(voyage)

# sell seats for the voyage
    def SellSeatsForVoyageOutgoing(self, voyageID, soldSeats):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        
        try:
            aircraft = self.data.getAircraftByAircraftID(voyage.aircraftID)
        except EntryNotInDatabase:
            raise AircraftNotRegistered('The voyage does not have a Aircraft registered')
        if (int(voyage.seatingSoldOutgoing) + int(soldSeats)) > int(aircraft.total_seats_int):

            raise NotEnoughSeats("There are not enough available seats")
        else:
            voyage.seatingSoldOutgoing = int(voyage.seatingSoldOutgoing) + int(soldSeats)
            self.data.updateVoyage(voyage)
            return

# sell seats for the incoming flight of a voyage    
    def SellSeatsForVoyageIncoming(self, voyageID, soldSeats):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        aircraft = self.data.getAircraftByAircraftID(voyage.aircraftID)
        if (int(voyage.seatingSoldIncoming) + int(soldSeats)) > int(aircraft.total_seats_int):
            return -1
        else:
            voyage.seatingSoldIncoming = int(voyage.seatingSoldIncoming) + int(soldSeats)
            self.data.updateVoyage(voyage)
            return 1


# List all voyages for a given destination
    def ListVoyagesForDestination(self, dest_id):
        voyages = self.data.getAllVoyages()
        voyForDest = []

        for voy in voyages:
            if str(voy.destination) == str(dest_id):
                voyForDest.append(voy)
        return voyForDest

# returns weather the voyage has been fully staffed
    def IsFullyStaffed(self, voyage):
        return len(voyage.pilots_lst) > 1 and len(voyage.flightAttendants_lst) > 0

# Get the status of the voyage
    def GetVoyageStatus(self, voyage):
        voyageTimes = self._getTimeOfVoyageActivities(voyage)
        timeNow = datetime.now()
        if timeNow < voyageTimes[0]:
            return "Not Departed"
        if timeNow < voyageTimes[1]:
            return "In Transit To Dest"
        if timeNow < voyageTimes[2]:
            return "Idle At Destination"
        if timeNow < voyageTimes[3]:
            return "In Transit To Iceland"
        else:
            return "Voyage is Complete"


# Private Method to get all inner times of a voyage
    def _getTimeOfVoyageActivities(self, voyage): # returns list [<Departure from iceland>, <Arrival at destination>, <departure from destination>, <Arrival at Iceland>]
        destination = self.data.getDestinationByDestinationID(voyage.destination)
        
        try:
            StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError:
            StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S')

        flightTime = float(destination.flight_duration) # consider changing this to int so as to not miss the disimal places!
        deltaHours = flightTime
        deltaMinutes = (deltaHours%1)*60
        deltaSeconds = (deltaMinutes%1)*60
        deltaHours = int(deltaHours)
        deltaMinutes = int(deltaMinutes)
        deltaSeconds = int(deltaSeconds)

        DepartureFromIceland = parse(StartTime_dateTime.isoformat())
        ArrivalAtDestination = parse((StartTime_dateTime + relativedelta(hours=+(flightTime), minutes=+deltaMinutes, seconds=+deltaSeconds)).isoformat())
        DepartureFromDestination = parse((StartTime_dateTime + relativedelta(hours=+(flightTime+1), minutes=+deltaMinutes, seconds=+deltaSeconds)).isoformat())
        ArrivalAtIceland = parse((StartTime_dateTime + relativedelta(hours=+(flightTime*2+1), minutes=+deltaMinutes*2, seconds=+deltaSeconds*2)).isoformat())
        return [DepartureFromIceland, ArrivalAtDestination, DepartureFromDestination, ArrivalAtIceland] # Assuming the rest at destination is 1 hour


# private method to say weather a time is free for an new flight
    def _isDepartureTimeFree(self, flightTime_str_iso):
        voyages = self.data.getAllVoyages()
        parsedTime = parse(flightTime_str_iso)
        for voy in voyages:
            if parsedTime == parse(voy.departureTime):
                return False
        return True

# private method to generate a new flight id
    def _GenerateFlightID(self, destinationID, departureTime):
        outgoingFlightID_str = 'NA'
        incomingFlightID_str = 'NA'
        destinationID_str = str(destinationID)
        if len(destinationID_str) == 1:
            destinationID_str = '0' + destinationID_str
        outgoingFlightID_str += destinationID_str
        incomingFlightID_str += destinationID_str
        highestFlightID = self._HighestFlightID(destinationID, departureTime)
        outgoingFlightID_str += str(highestFlightID)
        incomingFlightID_str += str(highestFlightID + 1)
        return [outgoingFlightID_str, incomingFlightID_str]


# private methdo to find the hightest flight id
    def _HighestFlightID(self, destinationID, date_iso): # simply finds the flight on the desired day with the highest flight id so you can generate one that's higher
        voyages = self.data.getAllVoyages()
        parsedDate = parse(date_iso)
        highestID = 0
        for voy in voyages:
            if str(voy.destination) == str(destinationID):
                parsedVoyTime = parse(voy.departureTime)
                if parsedDate.year == parsedVoyTime.year and parsedDate.month == parsedVoyTime.month and parsedDate.day == parsedVoyTime.day:
                    if voy.incomingFlightID != None and voy.incomingFlightID != '' and int(voy.incomingFlightID[-1]) > highestID:
                        highestID = int(voy.incomingFlightID[-1]) + 1
        return highestID

# private method to get teh end of the given voyage
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

# private method to generate a new voyage id
    def _GenerateNewVoyageID(self):
        voyages = self.data.getAllVoyages()
        iteration = 1
        highest_id = 0
        for voy in voyages:
            if iteration <= 1:
                highest_id = int(voy.voyageID)
            else:
                if int(voy.voyageID) > highest_id:
                    highest_id = int(voy.voyageID)
            
            iteration += 1
        return highest_id + 1 # returns an integer that is 1 higher than the highest id any voyage has in the database


if __name__ == "__main__":
    logic = VoyageLL()
    # print(logic._GenerateNewVoyageID())

    # time = datetime.now().isoformat()
    # voyage = Voyage(logic._GenerateNewVoyageID(), 1, time)
    # logic.addVoyage(2, time)
    print(logic.AddStaffToVoyage(1, '1611982429'))
    date = datetime(2020, 2, 8, 0, 0, 0).isoformat()
    print(logic.ListVoyagesForGivenWeek(date))
