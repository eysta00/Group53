import csv
import os
from Destination import Destination
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase
from datetime import datetime

class DestinationIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.tempFilePath = 'Data/DestinationTemp.csv'
        # dest_name, dest_id, flightTime
        self.__fieldNames_lst = ['dest_name', 'dest_id', 'flight_duration']

    def addDestination(self, destination):
        
        if self.DestinationInDatabase_bool(destination.dest_id): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateDestination with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            
            csvWriter.writerow({'dest_name' : destination.dest_name, 'dest_id' : destination.dest_id, 'flight_duration' : destination.flight_duration})

    
    
    def updateDestination(self, destination):
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            rows = list(csvReader)
            for entry in rows:
                if str(entry["dest_id"]) == str(destination.dest_id):
                    entry["dest_name"], entry["dest_id"], entry["flight_duration"] = \
                        destination.dest_name, destination.dest_id, destination.flight_duration
                    self.__reWriteFileFromList(rows)
                    return
            raise EntryNotInDatabase('try using addDestination')


# method to rewrite entire data file from list from update Employee
    def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
        with open(self.tempFilePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)
            os.remove(self.filePath)
            os.rename(self.tempFilePath, self.filePath)



#class to access an Employe by Social Security Number
    def getDestinationByDest_id(self, dest_id):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["dest_id"]) == str(dest_id):
                    return Destination(row['dest_name'], row['dest_id'], row['flight_duration'])

    def DestinationInDatabase_bool(self, dest_id):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["dest_id"]) == str(dest_id):
                    return True
            return False

    def getAllDestinations(self):
        return_list = []
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                return_list.append(Destination(row['dest_name'], row['dest_id'], row['flight_duration']))
        return return_list
        

if __name__ == "__main__":
    data = DestinationIO('Data/DestinationData.csv')
    dest = Destination('San Francisco', 3, 6)

    try:
        data.addDestination(dest)
    except EntryInDatabase:
        print('destination already in database')

    try:
        data.updateDestination(dest)
    except EntryNotInDatabase:
        print('destination not in database')

    print(data.getAllDestinations())