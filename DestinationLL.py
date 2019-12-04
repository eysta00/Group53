from DestinationIO import DestinationIO
from Destination import Destination
from IOAPI import IOAPI
from datetime import datetime
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase
class DestinationLL:
    def __init__(self):
        self.data = IOAPI()
    
    def RegisterDestination(self, dest_name, dest_id, flight_duration):
        try:
            self.data.addDestination(Destination(dest_name, dest_id, flight_duration))
            return 1 
        except EntryInDatabase:
            return -1

    def ListAllDestinations(self):
        destinations = self.data.getAllDestinatons()
        # dst = []
        # for d in destinations:
        #     dst.append(d)
        destinations.sort(key=lambda x: x.name)
        return destinations

    