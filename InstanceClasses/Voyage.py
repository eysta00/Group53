class Voyage:
    # Instance class for voyages
    def __init__(self, voyageID, destination, departureTime, aircraftID = None, pilots_lst = None, flightAttendants_lst = None, captain = None, headFlightAttendant = None, seatingSoldOutgoing = 0, seatingSoldIncoming = 0, outgoingFlightID = None, incomingFlightID = None):
        self.voyageID = voyageID # this is a unique voyageID that the logic level will create
        self.destination = destination
        self.departureTime = departureTime
        self.aircraftID = aircraftID
        self.pilots_lst = pilots_lst 
        self.flightAttendants_lst = flightAttendants_lst 
        self.pilots_lst = pilots_lst 
        self.captain = captain
        self.headFlightAttendant = headFlightAttendant
        self.seatingSoldOutgoing = seatingSoldOutgoing
        self.seatingSoldIncoming = seatingSoldIncoming
        self.outgoingFlightID = outgoingFlightID
        self.incomingFlightID = incomingFlightID



    def __str__(self):
        return self.destination + ' : ' + self.departureTime

    def __repr__(self):
        return self.voyageID + ' : ' + self.destination