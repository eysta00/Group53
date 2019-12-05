from AircraftLL import AircraftLL

class AircraftUI:
    def __init__(self):
        self.AircraftLL = AircraftLL()

    def register_aircraft(self):
        model = input('Aircraft Model: ')
        manufacturer = input('Aircraft Manufacturer: ')
        total_seats = input('Number of Seats: ')
        req_licenses = input('Required Piloting Licenses: ')
        error = self.AircraftLL(model, manufacturer, total_seats, req_licenses)
        if error != 1:
            print("Error, input not valid!")
        
        return

test1 = AircraftUI()
test1.register_aircraft()