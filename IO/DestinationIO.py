import csv
import os
from InstanceClasses.Destination import Destination
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase
from datetime import datetime

class DestinationIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.tempFilePath = 'Data/DestinationTemp.csv'
        # dest_name, dest_id, flightTime
        self.__fieldNames_lst = ['country_str', 'airport_str', 'dest_id', 'flight_duration', 'distanceFromReykjavik', 'contactName_str', 'contactNr_str']
# country_str, airport_str, dest_id, flight_duration, distanceFromReykjavik, contactName_str = None, contactNr_str = None
    def addDestination(self, destination):
        
        if self.DestinationInDatabase_bool(destination.dest_id): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateDestination with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            
            csvWriter.writerow({'country_str' : destination.country_str, 'airport_str' : destination.airport_str, 'dest_id' : destination.dest_id, 'flight_duration' : destination.flight_duration, 'distanceFromReykjavik' : destination.distanceFromReykjavik, 'contactName_str' : destination:contactName_str, 'contactNr_str' : destination.contactNr_str})

    
    
    def updateDestination(self, destination):
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            rows = list(csvReader)
            for entry in rows:
                if str(entry["dest_id"]) == str(destination.dest_id):
                    entry["country_str"], entry['airport_str'], entry["dest_id"], entry["flight_duration"], entry['distanceFromReykjavik'], entry['contactName_str'], entry["contactNr_str"] = \
                        destination.country_str, destination.airport_str, destination.dest_id, destination.flight_duration, destination.distanceFromReykjavik, destination.contactName_str,destination.contactNr_str
                    self.__reWriteFileFromList(rows)
                    return
            raise EntryNotInDatabase('try using addDestination')



# ------ This Method Creates A New File And Transfers The Data To Negate Likelyhood Of Data Loss ------
# method to rewrite entire data file from list from update Employee
    # def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
    #     with open(self.tempFilePath, 'w') as csv_file:
    #         csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
    #         for entry in dictList:
    #             csvWriter.writerow(entry)
    #         os.remove(self.filePath)
    #         os.rename(self.tempFilePath, self.filePath)

# ------ Same Purpose As Commented Function Above But Less Redundancy But Does Not Require Delete Priveledges ------
    def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
        with open(self.filePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)
            

# country_str, airport_str, dest_id, flight_duration, distanceFromReykjavik, contactName_str = None, contactNr_str = None

#class to access an Employe by Social Security Number
    def getDestinationByDest_id(self, dest_id):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["dest_id"]) == str(dest_id):
                    return Destination(row['country_str'], row['airport_str'], row['dest_id'], row['flight_duration'], row['distanceFromReykjavik'], row['contactName_str'], row['contactNr_str'])

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
                return_list.append(Destination(row['country_str'], row['airport_str'], row['dest_id'], row['flight_duration'], row['distanceFromReykjavik'], row['contactName_str'], row['contactNr_str']))
        return return_list
        
    def listAllDestinations(self):
        with open(self.filePath, 'r') as csv_file:
            # csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            print("{:<20}{:<20}{:<10}".format("Dest Name", "ID", "Duration"))
            for row in csv_file:
                dest_name, dest_id, flight_duration = row.strip().split(",")
                print("{:<20}{:<20}{:<10}".format(dest_name, dest_id, flight_duration))

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