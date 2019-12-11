from LogicLayer.VoyageLL import VoyageLL

class VoyageUI:
    def __init__(self):
        self.VoyageLL = VoyageLL()

    def register_Voyage(self):
        Voyage_destination = input('Voyage destination: ')
        Voyage_time = input('Voyage ID: ')
        Voyage_id = input('Voyage ID: ')
        error = VoyageLL().RegisterVoyage(Voyage_destination, Voyage_time, Voyage_id)
        if error != 1:
            print("Error, input not valid!")
        
        return

    def register_aircraft_to_voyage(self):
        Voyage_id = input('Voyage ID: ')
        aircraft = input('Aircraft: ')

    def register_employees_to_voyage(self):
        Voyage_id = input('Voyage ID: ')
        Employee = input('Employee ID: ')

    def assign_captain_to_voyage(self):
        Voyage_id = input('Voyage ID: ')
        Pilot = input('Pilot ID: ')

    def print_Voyages(self):
        print("List all Voyages")
        Voyages = self.VoyageLL.ListAllVoyages()
        for Voyage in Voyages:
            print(Voyage)
        print("\n")