from DestinationLL import DestinationLL

class DestinationUI:
    def __init__(self):
        self.DestinationLL = DestinationLL()

    def register_destination(self):
        destination_name = input('Destination name: ')
        destination_id = input('Destination ID: ')
        flight_duration = input('Flight duration: ')
        error = self.DestinationLL(destination_name, destination_id, flight_duration)
        if error != 1:
            print("Error, input not valid!")
        
        return

    def print_destinations(self):
        print("List all destinations")
        destinations = self.DestinationLL.ListAllDestinations()
        for destination in destinations:
            print(destination)
        print("\n")

test1 = DestinationUI()
test1.print_destinations()
test1.register_destination()