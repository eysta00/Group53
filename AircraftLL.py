from Aircraft import Aircraft
from AircraftIO import AircraftIO
from IOAPI import IOAPI
from datetime import datetime
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase

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
        arcft = []
        for a in aircrafts:
            arcft.append(a)
        arcft.sort(key=lambda x: x.name)
        return arcft