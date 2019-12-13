class Destination:
    # Instance Class for Destinations
    def __init__(self, country_str, airport_str, dest_id, flight_duration, distanceFromReykjavik, contactName_str = None, contactNr_str = None):
        self.country_str = country_str
        self.airport_str = airport_str 
        self.dest_id = dest_id
        self.flight_duration = flight_duration
        self.distanceFromReykjavik = distanceFromReykjavik
        self.contactName_str = contactName_str
        self.contactNr_str = contactNr_str


    def __str__(self):
        return self.airport_str + ' : ' + self.flight_duration

    def __repr__(self):
        return self.dest_id + ' : ' + self.dest_name
