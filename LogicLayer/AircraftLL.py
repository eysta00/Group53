from InstanceClasses.Aircraft import Aircraft
# from InstanceClasses.AircraftIO import AircraftIO
from IO.IOAPI import IOAPI
from datetime import datetime
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase
import dateutil.parser

class AircraftLL:
    def __init__(self):
        self.data = IOAPI()

    def RegisterAircraft(self, Id_str, model_str, totalseats_str):
        try:
            self.data.addAircraft(Aircraft( Id_str, model_str, totalseats_str))
            return 1 
        except EntryInDatabase:
            return -1

    def ListAllAircrafts(self):
        aircrafts = self.data.getAllAircrafts()
        aircrafts.sort(key=lambda x: x.model)
        return aircrafts

    def _GenerateNewAircraftID(self):
        aircrafts = self.data.getAllAircrafts()
        iteration = 1
        for air in aircrafts:
            if iteration <= 1:
                highest_id = int(air.aircraftID)
            else:
                if int(air.aircraftID) > highest_id:
                    highest_id = int(air.aircraftID)
            
            iteration += 1
        return highest_id + 1 # returns an integer that is 1 higher than the highest id any voyage has in the database

if __name__ == "__main__":
    logic = AircraftLL()
    print(logic._GenerateNewAircraftID())