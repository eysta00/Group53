class Flight:
    def __init__(self, flight_num, destination, dest_contact, date, end_date, departure, aircraft_id):
        self.f_flight_num = flight_num
        self.f_destination = destination 
        self.f_dest_contact = dest_contact
        self.f_date = date
        self.f_end_date = end_date
        self.f_departure = departure
        self.f_status = ''
        self.f_current_pos = ''
        self.f_aircraft_id = aircraft_id
        self.f_work_pr = {}
        self.f_employees = []
        self.f_pilots = []
        self.f_full = 0 #or 1
        self.f_data = {}

    def update_data(self):
        self.f_data['flight number'] = self.f_flight_num
        self.f_data['destination'] = self.f_destination
        self.f_data['destinaiton contact'] = self.f_dest_contact
        self.f_data['date'] = self.f_date
        self.f_data['end date'] = self.f_end_date
        self.f_data['departure'] = self.f_departure
        self.f_data['status'] = self.f_status
        self.f_data['current position'] = self.f_current_pos
        self.f_data['aircraft id'] = self.f_aircraft_id
        self.f_data['work procedures'] = self.f_work_pr
        self.f_data['employees'] = self.f_employees
        self.f_data['pilots'] = self.f_pilots
        self.f_data['flight full'] = self.f_full

    def change_contact(self, new_contact):
        self.f_dest_contact = new_contact
