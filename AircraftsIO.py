import csv

class AircraftsIO():
    def __init__(self, filePath):
        self.filePath = filePath

    def addAircraft(self, Aircraft):
        
        with open(self.filePath) as csv_file:
            csvreader = csv.read(csv)

    def updateAircraft(self, Aircraft):
        pass

    def getAircraftByNr(self, AircraftNr_int):
        pass


if __name__ == "__main__":
    data = AircraftsIO("Data/AircraftsData.csv")



