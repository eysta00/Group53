from Voyage import Voyage
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase
from IOAPI import IOAPI
import dateutil.parser
from datetime import datetime
from dateutil.parser import *
from dateutil.relativedelta import *
# import dateutil.parser


class VoyageLL:
    def __init__(self):
        self.data = IOAPI()

    def ListAllVoyages(self):
        return self.data.getAllVoyages()


    # We should possibly edit the code so that it doesn't access the stored instances in the classes directly but through methods
    def AddStaffToVoyage(self, voyageID, employeeSSN): 
        
        try:
            voyage = self.data.getVoyageByVoyageID(voyageID)
            employee = self.data.getEmployeeBySSN(employeeSSN)
            if employee.pilot_bool:
                print(voyage.pilots_lst)
                print(type(voyage.pilots_lst))
                voyage.pilots_lst.append(employeeSSN)
            else:
                voyage.flightAttendats_lst.append(employeeSSN)
            self.data.updateVoyage(voyage)
            return 1
        except EntryNotInDatabase: # error code to see if voyage is successfully updated
            return -1

    def addVoyage(self, destination_id, flightTime_str):
        
        # implement logic checking if there's enough staff available at the given time here

        try:
            voyage = Voyage(self._GenerateNewVoyageID(), destination_id, flightTime_str)
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
            parsedEndTime = self._getEndTimeOfVoyage(voy)

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
            parsedEndTime = self._getEndTimeOfVoyage(voy)
            if (parsedEndTime > dateParced and parsedEndTime < weekLaterParced) or (parsedStartTime > dateParced and parsedStartTime < weekLaterParced):
                voyagesInWeek_lst.append(voy)
        return voyagesInWeek_lst



    def _getEndTimeOfVoyage(self, voyage):
        destination = self.data.getDestinationByDestinationID(voyage.destination)
        StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S.%f')
        flightTime = int(destination.flight_duration) # consider changing this to int so as to not miss the disimal places!
        # print(flightTime)
        return parse((StartTime_dateTime + relativedelta(hour=+(flightTime*2+1))).isoformat()) # Assuming the rest at destination is 1 hour

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
