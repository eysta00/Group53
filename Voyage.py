class Voyage:
    def __init__(self, flight_init, flight_sec):
        self.flight_init = flight_init
        self.flight_sec = flight_sec
        self.v_title = flight_init.f_destination 
        self.v_data = [self.flight_init, self.flight_sec]

    def update_data(self, new_init, new_sec):
        self.flight_init = new_init
        self.flight_sec = new_sec
        self.v_data = [self.flight_init, self.flight_sec]

    def change_contact(self, flight_bool, new_contact): #flight_bool 0 for init flight, 1 for sec
        if flight_bool == 0:
            self.flight_init.f_dest_contact = new_contact
        else:
            self.flight_init.f_dest_contact = new_contact


    pass
