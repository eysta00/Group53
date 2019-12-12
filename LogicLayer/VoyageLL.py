from InstanceClasses.Voyage import Voyage
from Exceptions.Exceptions import *
from IO.IOAPI import IOAPI
import dateutil.parser
from datetime import datetime
from dateutil.parser import *
from dateutil.relativedelta import *
# import dateutil.parser


class VoyageLL:
    def __init__(self):
        self.data = IOAPI()

    def ListAllVoyages(self):
        voyages = self.data.getAllVoyages()
        #sort by something here not sure what
        return voyages

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

    def getVoyageByVoyageID(self, voyageID):
        return self.data.getVoyageByVoyageID(voyageID)


    # We should possibly edit the code so that it doesn't access the stored instances in the classes directly but through methods
    def AddStaffToVoyage(self, voyageID, employeeSSN): 

        voyage = self.data.getVoyageByVoyageID(voyageID)
        employee = self.data.getEmployeeBySSN(employeeSSN)
        print(employee) # did not run nor raise error
        
        if str(employeeSSN) in voyage.pilot_lst or str(employeeSSN) in voyage.flightAttendants_lst:
            raise EmployeeAlreadyAssigned('This employee is already assigned to this voyage')

        # print(employee.pilot_bool)
        # print(type(employee.pilot_bool))
        if employee.pilot_bool:
            # print(voyage.pilots_lst)
            # print(type(voyage.pilots_lst))
            # print(voyage.pilots_lst)
            voyage.pilots_lst.append(employeeSSN)
        else:    
            voyage.flightAttendants_lst.append(employeeSSN)

        self.data.updateVoyage(voyage)


    def assignAircraftToVoyage(self, voyageID, aircraftID):
        try:
            voyage = self.data.getVoyageByVoyageID(voyageID)
            voyage.aircraftID = aircraftID
            self.data.updateVoyage(voyage)
            return 1
        except EntryNotInDatabase:
            return -1


    def addVoyage(self, apiself, destination_id, flightTime_str):
        
        # implement logic checking if there's enough staff available at the given time here

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
        
        if freePilots > 2 or freeFlightAttendants > 1:
            raise ToFewAvailableEmployees("There are not enough available employees on this date to create a voyage")

        try:
            flightIDs_lst_str = self._GenerateFlightID(destination_id, flightTime_str)
            voyage = Voyage(self._GenerateNewVoyageID(), destination_id, flightTime_str, outgoingFlightID=flightIDs_lst_str[0], incomingFlightID=flightIDs_lst_str[1])
            self.data.addVoyage(voyage)
            return 1
        except EntryInDatabase:
            return -1

        


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
            

    def ListVoyagesForGivenWeek(self, date_iso): # the input date is the first day in the week
        voyages = self.data.getAllVoyages()
        voyagesInWeek_lst = []
        dateParced = parse(date_iso)
        weekLaterParced = dateParced + relativedelta(days=+7)
        # print(dateParced)
        # print(weekLaterParced)
        for voy in voyages:
            parsedStartTime = parse(voy.departureTime)
            parsedEndTime = parse(self._getEndTimeOfVoyage(voy))
            if (parsedEndTime > dateParced and parsedEndTime < weekLaterParced) or (parsedStartTime > dateParced and parsedStartTime < weekLaterParced):
                voyagesInWeek_lst.append(voy)
        return voyagesInWeek_lst


    def ListVoyagePilots(self, voyageID):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        pilotsSSN_lst = voyage.pilots_lst
        pilots_emp = []
        for pilotSSN in pilotsSSN_lst:
            pilots_emp.append(self.data.getEmployeeBySSN(pilotSSN))
        return pilots_emp

    def ListVoyageFlightAttendants(self, voyageID):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        flightAttendantsSSN_lst = voyage.flightAttendants_lst
        flightAttendats_emp = []
        for flightAttendatSSN in flightAttendantsSSN_lst:
            flightAttendats_emp.append(self.data.getEmployeeBySSN(flightAttendatSSN))
        return flightAttendats_emp


    def UpdateVoyageCaptain(self,voyageID, pilotSSN):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        voyage.captain = pilotSSN
        self.data.updateVoyage(voyage)

    def SellSeatsForVoyageOutgoing(self, voyageID, soldSeats):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        # Raise exception if no aircraft has been registered
        aircraft = self.data.getAircraftByAircraftID(voyage.aircraftID)
        print("1. " + str(voyage.seatingSoldOutgoing))
        print("2. " + str(soldSeats))
        print("3. " + str(aircraft.total_seats_int))
        if (int(voyage.seatingSoldOutgoing) + int(soldSeats)) > int(aircraft.total_seats_int):
            return -1
        else:
            voyage.seatingSoldOutgoing = int(voyage.seatingSoldOutgoing) + int(soldSeats)
            self.data.updateVoyage(voyage)
            return 1
    
    def SellSeatsForVoyageIncoming(self, voyageID, soldSeats):
        voyage = self.data.getVoyageByVoyageID(voyageID)
        # Raise exception if no aircraft has been registered
        aircraft = self.data.getAircraftByAircraftID(voyage.aircraftID)
        # print("1. " + str(voyage.seatingSoldIncoming))
        # print("2. " + str(soldSeats))
        # print("3. " + str(aircraft.total_seats_int))
        if (int(voyage.seatingSoldIncoming) + int(soldSeats)) > int(aircraft.total_seats_int):
            return -1
        else:
            voyage.seatingSoldIncoming = int(voyage.seatingSoldIncoming) + int(soldSeats)
            self.data.updateVoyage(voyage)
            return 1

    def ListVoyagesForDestination(self, dest_id):
        voyages = self.data.getAllVoyages()
        voyForDest = []

        for voy in voyages:
            if str(voy.destination) == str(dest_id):
                voyForDest.append(voy)
        return voyForDest

    def _isDepartureTimeFree(self, flightTime_str_iso):
        voyages = self.data.getAllVoyages()
        parsedTime = parse(flightTime_str_iso)
        for voy in voyages:
            if parsedTime == parse(voy.departureTime):
                return False
        return True

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
