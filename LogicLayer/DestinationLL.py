# from DestinationIO import DestinationIO
from InstanceClasses.Destination import Destination
from IO.IOAPI import IOAPI
from datetime import datetime
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase
# import dateutil.parser

class DestinationLL():
    def __init__(self):
        self.data = IOAPI()
    
    def RegisterDestination(self, dest_name, dest_id, flight_duration, contactNr):
        try:
            self.data.addDestination(Destination(dest_name, dest_id, flight_duration, contactNr))
            return 1 
        except EntryInDatabase:
            return -1

    def ListAllDestinations(self):
        destinations = self.data.getAllDestinatons()
        # dst = []
        # for d in destinations:
        #     dst.append(d)
        # destinations.sort(key=lambda x: x.name)
        return destinations

    def UpdateDestinationContactNumber(self, destinationID, contactNr):
        destination = self.data.getDestinationByDestinationID(destinationID)
        destination.contactNr = contactNr

        try:
            self.data.updateDestination(destination)
            return 1
        except EntryNotInDatabase:
            return -1



    def _GenerateNewDestinationID(self):
        destinations = self.data.getAllDestinatons()
        iteration = 1
        for dest in destinations:
            if iteration <= 1:
                highest_id = int(dest.dest_id)
            else:
                if int(dest.dest_id) > highest_id:
                    highest_id = int(dest.dest_id)
            
            iteration += 1
        return int(highest_id) + 1 # returns an integer that is 1 higher than the highest id any voyage has in the database


    

if __name__ == "__main__":
    logic = DestinationLL()
    print(logic._GenerateNewDestinationID())