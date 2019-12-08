import csv
import os
from Voyage import Voyage
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase
from datetime import datetime

class VoyageIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.tempFilePath = 'Data/VoyageTemp.csv'
        # voyageID, destination, departureTime, aircraftID = None, pilots_lst = None, flightAttendants_lst = None, captain = None
        self.__fieldNames_lst = ['voyageID','destination', 'departureTime', 'aircraftID', 'pilots_lst', 'flightAttendants_lst', 'captain']

    def addVoyage(self, voyage):
        
        if self.VoyageInDatabase_bool(voyage.voyageID): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateVoyage with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            
            csvWriter.writerow({'voyageID' : voyage.voyageID,"destination" : voyage.destination, "departureTime" : voyage.departureTime, "aircraftID" : voyage.aircraftID, "pilots_lst" : voyage.pilots_lst,\
                "flightAttendants_lst" : voyage.flightAttendants_lst, "captain" : voyage.captain})

    
    
    def updateVoyage(self, voyage):
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            rows = list(csvReader)
            for entry in rows:
                if str(entry["voyageID"]) == str(voyage.voyageID):
                    entry["voyageID"], entry["destination"], entry["departureTime"], entry['aircraftID'], entry['pilots_lst'], entry['flightAttendants_lst'], entry['captain'] = \
                        voyage.voyageID, voyage.destination, voyage.departureTime, voyage.aircraftID, voyage.pilots_lst, voyage.flightAttendants_lst, voyage.captain
                    self.__reWriteFileFromList(rows)
                    return
            raise EntryNotInDatabase('try using addVoyage')


# method to rewrite entire data file from list from update Employee
    def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
        with open(self.tempFilePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)
            os.remove(self.filePath)
            os.rename(self.tempFilePath, self.filePath)



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
                    pilots_lst = row['pilots_lst']
                    flightAttendants_lst = row['flightAttendants_lst']
                    captain = row['captain']
                    if pilots_lst == '':
                        pilots_lst = []
                    if flightAttendants_lst == '':
                        flightAttendants_lst = []

                    return Voyage(voyageID, destination, departureTime, aircraftID, pilots_lst, flightAttendants_lst, captain)

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
                    return_list.append(Voyage(row['voyageID'], row['destination'], row['departureTime'], row['aircraftID'], row['pilots_lst'], row['flightAttendants_lst'], row['captain']))
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