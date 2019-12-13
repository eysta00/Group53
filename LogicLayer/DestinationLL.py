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
    # country_str, airport_str, dest_id, flight_duration, distanceFromReykjavik, contactName_str = None, contactNr_str = None
    def RegisterDestination(self, country_str, airport_str, flight_duration, distanceFromReykjavik, contactName_str, contactNr_str):
            
            dest_id = self._GenerateNewDestinationID()
            self.data.addDestination(Destination(country_str, airport_str, dest_id, flight_duration, distanceFromReykjavik, contactName_str, contactNr_str))
            

    def ListAllDestinations(self):
        destinations = self.data.getAllDestinatons()
        # dst = []
        # for d in destinations:
        #     dst.append(d)
        # destinations.sort(key=lambda x: x.name)
        return destinations

    def UpdateDestinationContactNumber(self, destinationID, contactNr_str):
        destination = self.data.getDestinationByDestinationID(destinationID)
        destination.contactNr_str = contactNr_str

        self.data.updateDestination(destination)


    def UpdateDestinationContactName(self, destinationID, contactName):
        destination = self.data.getDestinationByDestinationID(destinationID)
        destination.contactNr_str = contactNr_str

        self.data.updateDestination(destination)

    def MostPopularDestination(self): # Returns what destination has sold the most seats to in total
        voyages = self.data.getAllVoyages()
        destinations = self.data.getAllDestinatons()
        destinations_dict = {}
        for dest in destinations:
            destinations_dict[dest.dest_id] = 0
        
        for voy in voyages:
            try:
                destinations_dict[voy.destination] += int(voy.seatingSoldOutgoing)
            except ValueError:
                pass
        
        maxSold = 0
        mostPopularDest = None
        firstRun = True
        for key in destinations_dict:
            if firstRun:
                mostPopularDest = key
                firstRun = False
                maxSold = destinations_dict[key]
                continue
            if destinations_dict[key] > maxSold:
                maxSold = destinations_dict[key]
                mostPopularDest = key
        return self.data.getDestinationByDestinationID(mostPopularDest)



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