class Aircraft:
    id_count = 0 #this would need to be loaded in from data for later

    def __init__(self, model, manufacturer, total_seats, req_licenses):
        self.ai_id = Aircraft.gen_id(self)
        self.ai_model = model
        self.ai_manufacturer = manufacturer
        self.ai_total_seats = total_seats
        self.ai_used_seats = 0
        self.ai_pilots = []
        self.ai_permissions = [] #pilots
        self.ai_req_licenses = req_licenses
        self.ai_flight_count = 0
        self.ai_flight_time = 0
        self.ai_status = 0 #0 for OK/1 for maintenence/2 for malfunctioning
        self.ai_data = {}

    def gen_id(self):
        self.id_count += 1
        self.ai_id = self.id_count


    def update_data(self):
        self.ai_data['aircraft id'] = self.ai_id
        self.ai_data['model'] = self.ai_model
        self.ai_data['manufacturer'] = self.ai_manufacturer
        self.ai_data['total seats'] = self.ai_total_seats
        self.ai_data['used seats'] = self.ai_used_seats
        self.ai_data['pilots'] = self.ai_pilots
        self.ai_data['permissions'] = self.ai_permissions
        self.ai_data['required licenses'] = self.ai_req_licenses
        self.ai_data['flight count'] = self.ai_flight_count
        self.ai_data['flight time'] = self.ai_flight_time
        self.ai_data['status'] = self.ai_status
    pass