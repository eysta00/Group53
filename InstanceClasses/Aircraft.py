class Aircraft:
    # Instance Class for aircrafts
    def __init__(self, aircraftID, manufacturer, model, total_seats_int):
        self.aircraftID = aircraftID
        self.model = model
        self.total_seats_int = total_seats_int
        self.manufacturer = manufacturer

    def __str__(self):
        return str(self.manufacturer) + ' : ' + str(self.model) + ' : ' + str(self.total_seats_int)

    def __repr__(self):
        return self.aircraftID + ' : ' + self.model
    