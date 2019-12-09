from LogicLayer.AircraftLL import AircraftLL

class AircraftUI:
    def __init__(self):
        self.AircraftLL = AircraftLL()

    def register_aircraft(self):
        model = input('Aircraft Model: ')
        manufacturer = input('Aircraft Manufacturer: ')
        total_seats = input('Number of Seats: ')
        req_licenses = input('Required Piloting Licenses: ')
        error = AircraftLL().RegisterAircraft(model, manufacturer, total_seats, req_licenses)
        if error != 1:
            print("Error, input not valid!")
        
        return

    def print_aircrafts(self):
        print("List all aircrafts")
        aircrafts = self.AircraftLL.ListAllAircrafts()
        for aircraft in aircrafts:
            print(aircraft)
        print("\n")


test1 = AircraftUI()
test1.print_aircrafts()
test1.register_aircraft()