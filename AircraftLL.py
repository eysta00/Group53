from Aircraft import Aircraft
from IOAPI import IOAPI
from datetime import datetime
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase

class AircraftLL:
    def __init__(self):
        data = IOAPI()

    def RegisterAircraft(self, Id_str, model_str, totalseats_str):
        try:
            data.Aircraft(Aircraft( Id_str, model_str, totalseats_str))
            return 1 
        except EntryInDatabase:
            return -1

            
    
    ################


    def getAircraftByAircraftID(self, aircraftID):
        try:
            data.Aircraft(Aircraft(id_str, model_str, totatlseats_str))
            return self.Aircraftio().getAllAircrafts()

    def addAircraft(self, aircraft):
        return self.AircraftData.addAircraft(aircraft)

    def updateAircraft(self, aircraft):
        return self.AircraftData.updateAircraft(aircraft)