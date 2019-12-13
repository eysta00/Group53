import csv
import os
from InstanceClasses.Aircraft import Aircraft
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase
from datetime import datetime

class AircraftIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.tempFilePath = 'Data/AircraftTemp.csv'
        self.__fieldNames_lst = ['aircraftID', 'manufacturer', 'model', 'total_seats_int']

    def addAircraft(self, aircraft):
        
        if self.AircraftInDatabase_bool(aircraft.aircraftID): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateAircraft with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            
            csvWriter.writerow({'aircraftID' : aircraft.aircraftID, 'manufacturer' : aircraft.manufacturer, 'model' : aircraft.model, 'total_seats_int' : aircraft.total_seats_int})

    
    
    def updateAircraft(self, aircraft):
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            rows = list(csvReader)
            for entry in rows:
                if str(entry["aircraftID"]) == str(aircraft.aircraftID):
                    entry["aircraftID"], entry["manufacturer"], entry["model"], entry["total_seats_int"] = \
                        aircraft.aircraftID, aircraft.manufacturer, aircraft.model, aircraft.total_seats_int
                    self.__reWriteFileFromList(rows)
                    return
            raise EntryNotInDatabase('try using addAircraft')


# method to rewrite entire data file from list from update Employee
    def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
        with open(self.filePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)




# Method to access an Employe by Social Security Number
    def getAircraftByAircraftID(self, aircraftID):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["aircraftID"]) == str(aircraftID):
                    aircraftID = row['aircraftID']
                    manufacturer = row['manufacturer']
                    model = row['model']
                    total_seats_int = row['total_seats_int']
                    if total_seats_int == '' or total_seats_int == None:
                        total_seats_int = 0
                    return Aircraft(aircraftID, manufacturer, model, total_seats_int)
            raise EntryNotInDatabase("The given aircraft id does not correspond to the database")

# Method to check if the aircraft is already in the database
    def AircraftInDatabase_bool(self, AircraftID):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["aircraftID"]) == str(AircraftID):
                    return True
            return False

# Method That Returns all aircrafts in the database
    def getAllAircrafts(self):
        return_list = []

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                    return_list.append(Aircraft(row['aircraftID'], row['manufacturer'], row['model'], row['total_seats_int']))
        return return_list

if __name__ == "__main__":
    data = AircraftIO('Data/AircraftData.csv')
    aircraft = Aircraft(2, 'Boeng_747', 300)
    
    
    try:
        data.addAircraft(aircraft)
    except EntryInDatabase:
        print('Aircraft already in database')

    try:
        data.updateAircraft(aircraft)
    except EntryNotInDatabase:
        print('Aircraft not in database')

    print(data.getAllAircrafts())