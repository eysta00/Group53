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
        # voyageID, destination, departureTime, aircraftID = None, pilots_lst = None, flightAttendants_lst = None, captain = None
        self.__fieldNames_lst = ['voyageID','destination', 'departureTime', 'aircraftID', 'pilots_lst', 'flightAttendants_lst', 'captain', 'headFlightAttendant', 'seatingSoldOutgoing', 'seatingSoldIncoming', 'outgoingFlightID', 'incomingFlightID']

    def addVoyage(self, voyage):
        
        if self.VoyageInDatabase_bool(voyage.voyageID): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateVoyage with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            
            csvWriter.writerow({'voyageID' : voyage.voyageID,"destination" : voyage.destination, "departureTime" : voyage.departureTime, "aircraftID" : voyage.aircraftID, "pilots_lst" : voyage.pilots_lst,\
                "flightAttendants_lst" : voyage.flightAttendants_lst, "captain" : voyage.captain, 'headFlightAttendant' : voyage.headFlightAttendant, 'seatingSoldOutgoing' : voyage.seatingSoldOutgoing, 'seatingSoldIncoming': voyage.seatingSoldIncoming, 'outgoingFlightID' : voyage.outgoingFlightID, 'incomingFlightID' : voyage.incomingFlightID})

    
    
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

# ------ This Method Creates A New File And Transfers The Data To Negate Likelyhood Of Data Loss ------
# method to rewrite entire data file from list from update Employee
    # def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
    #     with open(self.tempFilePath, 'w') as csv_file:
    #         csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
    #         for entry in dictList:
    #             csvWriter.writerow(entry)
            
    #     os.remove(self.filePath)
    #     os.rename(self.tempFilePath, self.filePath)
    #         # os.rename(self.filePath, 'Data/temp.csv')
    #         # os.rename(self.tempFilePath, self.filePath)
    #         # os.rename('Data/temp.csv', self.tempFilePath)

# ------ Same Purpose As Commented Function Above But Less Redundancy But Does Not Require Delete Priveledges ------
    def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
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
                    # print(row['pilots_lst'])
                    # print(type(row['pilots_lst']))

                    pilots_lst = row['pilots_lst'].strip('][').split(', ') # this code is to convert pilots list to 
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


    def VoyageInDatabase_bool(self, voyageID):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["voyageID"]) == str(voyageID):
                    return True
            return False

    def getAllVoyages(self):
        return_list = []

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                voyageID = row['voyageID']
                destination = row['destination']
                departureTime = row['departureTime']
                aircraftID = row['aircraftID']
                # print(row['pilots_lst'])
                # print(type(row['pilots_lst']))
                pilots_lst = row['pilots_lst'].strip('][').split(', ') # this code is to convert pilots list to 
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