class Voyage:
    def __init__(self, voyageID, destination, departureTime, aircraftID = None, pilots_lst = None, flightAttendants_lst = None, captain = None, seatingSold = 0):
        # self.flight_init = flight_init
        # self.flight_sec = flight_sec
        # self.v_title = flight_init.f_destination 
        # self.v_data = [self.flight_init, self.flight_sec]
        self.voyageID = voyageID # this is a unique voyageID that the logic level will create
        self.destination = destination
        self.departureTime = departureTime
        self.aircraftID = aircraftID
        self.pilots_lst = pilots_lst
        self.flightAttendants_lst = flightAttendants_lst
        self.pilots_lst = pilots_lst
        self.captain = captain
        self.seatingSold = seatingSold


    # def update_data(self, new_init, new_sec):
    #     self.flight_init = new_init
    #     self.flight_sec = new_sec
    #     self.v_data = [self.flight_init, self.flight_sec]

    # def change_contact(self, flight_bool, new_contact): #flight_bool 0 for init flight, 1 for sec
    #     if flight_bool == 0:
    #         self.flight_init.f_dest_contact = new_contact
    #     else:
    #         self.flight_init.f_dest_contact = new_contact


    def __str__(self):
        return self.destination + ' : ' + self.departureTime

    def __repr__(self):
        return self.voyageID + ' : ' + self.destination