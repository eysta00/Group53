import csv
import os
from InstanceClasses.Voyage import Voyage
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase
from datetime import datetime

class VoyageIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.tempFilePath = 'Data/VoyageTemp.csv'
        self.__fieldNames_lst = ['voyageID','destination', 'departureTime', 'aircraftID', 'pilots_lst', 'flightAttendants_lst', 'captain', 'headFlightAttendant', 'seatingSoldOutgoing', 'seatingSoldIncoming', 'outgoingFlightID', 'incomingFlightID']

# Method to add voyage in database
    def addVoyage(self, voyage):
        
        if self.VoyageInDatabase_bool(voyage.voyageID): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateVoyage with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            
            csvWriter.writerow({'voyageID' : voyage.voyageID,"destination" : voyage.destination, "departureTime" : voyage.departureTime, "aircraftID" : voyage.aircraftID, "pilots_lst" : voyage.pilots_lst,\
                "flightAttendants_lst" : voyage.flightAttendants_lst, "captain" : voyage.captain, 'headFlightAttendant' : voyage.headFlightAttendant, 'seatingSoldOutgoing' : voyage.seatingSoldOutgoing, 'seatingSoldIncoming': voyage.seatingSoldIncoming, 'outgoingFlightID' : voyage.outgoingFlightID, 'incomingFlightID' : voyage.incomingFlightID})

    
# Method to update Voyage in database
    def updateVoyage(self, voyage):
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            rows = list(csvReader)
            for entry in rows:
                if str(entry["voyageID"]) == str(voyage.voyageID):
                    entry["voyageID"], entry["destination"], entry["departureTime"], entry['aircraftID'], entry['pilots_lst'], entry['flightAttendants_lst'], entry['captain'], entry['headFlightAttendant'], entry['seatingSoldOutgoing'], entry['seatingSoldIncoming'], entry['outgoingFlightID'], entry['incomingFlightID'] = \
                        voyage.voyageID, voyage.destination, voyage.departureTime, voyage.aircraftID, voyage.pilots_lst, voyage.flightAttendants_lst, voyage.captain, voyage.headFlightAttendant, voyage.seatingSoldOutgoing, voyage.seatingSoldIncoming, voyage.outgoingFlightID, voyage.incomingFlightID
                    self.__reWriteFileFromList(rows)
                    return
            raise EntryNotInDatabase('try using addVoyage')


# Method to rewrite the database with the entered data
    def __reWriteFileFromList(self, dictList): 
        with open(self.filePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)
            
        # os.remove(self.filePath)
        # os.rename(self.tempFilePath, self.filePath)
            



#class to access an Employe by Social Security Number
    def getVoyageByVoyageID(self, voyageID):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["voyageID"]) == str(voyageID):
                    voyageID = row['voyageID']
                    destination = row['destination']
                    departureTime = row['departureTime']
                    aircraftID = row['aircraftID']

                    pilots_lst = row['pilots_lst'].strip('][').split(', ') # this code is to convert pilots list from string to list
                    pilots_lst = [s.replace("'", "") for s in pilots_lst]

                    flightAttendants_lst = row['flightAttendants_lst'].strip('][').split(', ')
                    flightAttendants_lst = [s.replace("'", "") for s in flightAttendants_lst]
                    if pilots_lst[0] == '' and len(pilots_lst) == 1: # avoiding the list returning with one empty string
                        pilots_lst = []
                    if flightAttendants_lst[0] == '' and len(flightAttendants_lst) == 1:
                        flightAttendants_lst = []

                    captain = row['captain']
                    headFlightAttendant = row['headFlightAttendant']
                    seatingSoldOutgoing = row['seatingSoldOutgoing']
                    seatingSoldIncoming = row['seatingSoldIncoming']

                    outgoingFlightID = row['outgoingFlightID']
                    incomingFlightID = row['incomingFlightID']

                    if seatingSoldOutgoing == '':
                        seatingSoldOutgoing = 0
                    if seatingSoldIncoming == '':
                        seatingSoldIncoming = 0

                    if pilots_lst == '':
                        pilots_lst = []
                    if flightAttendants_lst == '':
                        flightAttendants_lst = []

                    return Voyage(voyageID, destination, departureTime, aircraftID, pilots_lst, flightAttendants_lst, captain, headFlightAttendant, seatingSoldOutgoing, seatingSoldIncoming, outgoingFlightID, incomingFlightID)
            raise EntryNotInDatabase

# Method to check if voyageid is in database
    def VoyageInDatabase_bool(self, voyageID):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["voyageID"]) == str(voyageID):
                    return True
            return False

# Method to get a list of all voyages
    def getAllVoyages(self):
        return_list = []

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                voyageID = row['voyageID']
                destination = row['destination']
                departureTime = row['departureTime']
                aircraftID = row['aircraftID']
                pilots_lst = row['pilots_lst'].strip('][').split(', ') # this code is to convert pilots from string to list 
                pilots_lst = [s.replace("'", "") for s in pilots_lst]
                flightAttendants_lst = row['flightAttendants_lst'].strip('][').split(', ')
                flightAttendants_lst = [s.replace("'", "") for s in flightAttendants_lst]
                if pilots_lst[0] == '' and len(pilots_lst) == 1: # avoiding the list returning with one empty string
                    pilots_lst = []
                if flightAttendants_lst[0] == '' and len(flightAttendants_lst) == 1:
                    flightAttendants_lst = []
                captain = row['captain']
                headFlightAttendant = row['headFlightAttendant']
                seatingSoldOutgoing = row['seatingSoldOutgoing']
                seatingSoldIncoming = row['seatingSoldIncoming']
                outgoingFlightID = row['outgoingFlightID']
                incomingFlightID = row['incomingFlightID']
                if seatingSoldOutgoing == '':
                    seatingSoldOutgoing = 0
                if seatingSoldIncoming == '':
                    seatingSoldIncoming = 0
                if pilots_lst == '':
                    pilots_lst = []
                if flightAttendants_lst == '':
                    flightAttendants_lst = []
                return_list.append(Voyage(voyageID, destination, departureTime, aircraftID, pilots_lst, flightAttendants_lst, captain, headFlightAttendant, seatingSoldOutgoing, seatingSoldIncoming, outgoingFlightID, incomingFlightID))
        return return_list


if __name__ == "__main__":
    data = VoyageIO('Data/VoyageData.csv')
    time_str = datetime(year = 2020, month = 2, day = 1, hour = 0, minute = 0, second = 0)
    voyage = Voyage(2, 'Copenhagen', time_str, 666, ['John', 'Phil'], ['Icarus', 'Paul'], 'John')
    
    try:
        data.addVoyage(voyage)
    except EntryInDatabase:
        print('Entry already in database')

    try:
        data.updateVoyage(voyage)
    except EntryNotInDatabase:
        print('Entry Not in database')

    print(data.getVoyageByVoyageID(2))

    print(data.getAllVoyages())