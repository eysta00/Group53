from UI.EmployeeUI import EmployeeUI
from UI.VoyageUI import VoyageUI
from UI.DestinationUI import DestinationUI

def default_operation():
    print('This operation is still WIP.\nThank you for your patience. :)')
    return MenuUI().showMainMenu()

class MenuUI:
    def showMainMenu(self):
        print("##### MAIN MENU #####")
        print("1. Employees"
              "\n2. Voyages"
              "\n3. Destinations"
              "\n4. Aircrafts")
        
        return self.getMInput()
    
    def showEmployeeMenu(self):
        print("##### Employees ######")
        print("\n1. Register Employee",
              "\n2. List Employees",
              "\n3. List Pilots",
              "\n4. List Flight Attendants",
              "\n5. List Assigned Employees",
              "\n6. List Unassigned Employees",
              "\n7. List pilots with aircraft privilage",
              "\n8. Change Employee Info",
              "\n9. Work Summary")
    
        return self.getEInput()
    
    def showVoyagesMenu(self):
        print("##### Voyages ######")
        print("\n1. Add Voyage",
              "\n2. List Voyages",
              "\n3. List Flights By Location",
              "\n4. Change Destination Contact Info",
              "\n5. List All Aircrafts",
              "\n6. List Available Aircrafts",
              "\n7. Assign Staff to Voyage")
        return self.getVInput()
    
    def showDestinationsMenu(self):
        print("##### Destinations ######")
        print("\n1. Add Destination",
              "\n2. List Destinations")
        return self.getDInput()

    def showAircraftsMenu(self):
        print("##### Aircrafts ######")
        print("\n1. Add Aircarft",
              "\n2. List Aircrafts")
        return self.getAInput()
    
    def getMInput(self):
        choice = input("\nEnter a command:")
        if choice == "1":
            return self.showEmployeeMenu()
        elif choice == "2":
            return self.showVoyagesMenu()
        elif choice == "3":
            return self.showDestinationsMenu()
        elif choice == "4":
            return self.showAircraftsMenu()
        elif choice == "q":
            return
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()

    def getEInput(self):
        choice = input("\nEnter a command:")
        if choice == "1":
            return EmployeeUI().print_register_employee()
        elif choice == "2":
            return EmployeeUI().print_all_employees()
        elif choice == "3":
            return EmployeeUI().print_pilots()
        elif choice == "4":
            return EmployeeUI().print_flight_attendants()
        elif choice == "5":
            return default_operation()
        elif choice == "6":
            return default_operation()
        elif choice == "7":
            return EmployeeUI().print_pilots_with_aircraft_privilage()
        elif choice == "8":
            return default_operation()
        elif choice == "9":
            return default_operation()
        elif choice == "q":
            return
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()
    
    def getVInput(self):
        choice = input("\nEnter a command:")
        if choice == "1":
            return default_operation()
        elif choice == "2":
            return VoyageUI().ListVoyages()
        elif choice == "3":
            return default_operation()
        elif choice == "4":
            return default_operation()
        elif choice == "q":
            return
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()
    
    def getDInput(self):
        choice = input("\nEnter a command:")
        if choice == "1":
            return DestinationUI().register_destination()
        elif choice == "2":
            return DestinationUI().print_destinations()
        elif choice == "q":
            return
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()
    
    def getAInput(self):
        choice = input("\nEnter a command:")
        if choice == "1":
            return 
        elif choice == "2":
            return
        elif choice == "3":
            return 
        elif choice == "4":
            return
        elif choice == "q":
            return
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()