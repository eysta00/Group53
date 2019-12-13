from UI.EmployeeUI import EmployeeUI
from UI.VoyageUI import VoyageUI
from UI.DestinationUI import DestinationUI
from UI.AircraftUI import AircraftUI

def default_operation():
    print('This operation is still WIP.\nThank you for your patience. :)')
    return MenuUI().showMainMenu()

class MenuUI:
    def showMainMenu(self):
        print("\n##### MAIN MENU #####")
        print("1. Employees"
              "\n2. Voyages"
              "\n3. Destinations"
              "\n4. Aircrafts",
              "\nIf you want to close the program enter \"q\"")
        
        return self.getMInput()
    
    def showEmployeeMenu(self):
        print("\n##### Employees ######")
        print("\n1. Register Employee",
              "\n2. List Employees",
              "\n3. List Pilots",
              "\n4. List Flight Attendants",
              "\n5. List Assigned Employees",
              "\n6. List Unassigned Employees",
              "\n7. List pilots with aircraft privilage",
              "\n8. Change Employee Info",
              "\n9. Work Summary",
              "\n10. List information for employee")
    
        return self.getEInput()
    
    def showVoyagesMenu(self):
        print("\n##### Voyages ######")
        print("\n1. Add Voyage",
              "\n2. List Voyages",
              "\n3. Assign Staff to Voyage",
              "\n4. Assign Captain to Voyage",
              "\n5. Assign lead Flight Attendant to Voyage",
              "\n6. Assign Aircraft to Voyage",
              "\n7. List voyage for given day",
              "\n8. List voyages for given week",
              "\n9. List Flights By Location",
              "\n10. Update Voyage Captain",
              "\n11. Sold seats for Voyage",
              "\n12. List Satus of Voyages",
              "\n13. Add Recurring Voyages")
        return self.getVInput()
    
    def showDestinationsMenu(self):
        print("\n##### Destinations ######")
        print("\n1. Add Destination",
              "\n2. List Destinations",
              "\n3. Change Destination Contact Info",
              "\n4. List Most Popular Destinations")
        return self.getDInput()

    def showAircraftsMenu(self):
        print("\n##### Aircrafts ######")
        print("\n1. Add Aircarft",
              "\n2. List Aircrafts",
              "\n3. Show aircraft status",
              "\n4. List All Available Aircrafts")
        return self.getAInput()
    
    def getMInput(self):
        choice = input("\nEnter a command: ")
        if choice == "1":
            return self.showEmployeeMenu()
        elif choice == "2":
            return self.showVoyagesMenu()
        elif choice == "3":
            return self.showDestinationsMenu()
        elif choice == "4":
            return self.showAircraftsMenu()
        elif choice == "q":
            return "quit_run"
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()

    def getEInput(self):
        choice = input("\nEnter a command: ")
        if choice == "1":
            return EmployeeUI().print_register_employee()
        elif choice == "2":
            return EmployeeUI().print_all_employees()
        elif choice == "3":
            return EmployeeUI().print_pilots()
        elif choice == "4":
            return EmployeeUI().print_flight_attendants()
        elif choice == "5":
            return EmployeeUI().print_assigned_employees()
        elif choice == "6":
            return EmployeeUI().print_unassigned_employees()
        elif choice == "7":
            return EmployeeUI().print_pilots_with_aircraft_privilage()
        elif choice == "8":
            return EmployeeUI().print_update_employee_infomation()
        elif choice == "9":
            return EmployeeUI().print_work_summary()
        elif choice == "10":
            return EmployeeUI().print_specific_employee()
        elif choice == "q":
            return "quit_run"
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()
    
    def getVInput(self):
        choice = input("\nEnter a command: ")
        if choice == "1":
            return VoyageUI().register_Voyage()
        elif choice == "2":
            return VoyageUI().print_Voyages()
        elif choice == "3":
            return VoyageUI().register_employees_to_voyage()
        elif choice == "4":
            return VoyageUI().assign_captain_to_voyage()
        elif choice == "5":
            return VoyageUI().assign_head_flightattendant_to_voyage()
        elif choice == "6":
            return VoyageUI().register_aircraft_to_voyage()
        elif choice == "7":
            return VoyageUI().print_voyage_for_day()
        elif choice == "8":
            return VoyageUI().print_voyage_for_week()
        elif choice == "9":
            return VoyageUI().print_voyage_by_dest()
        elif choice == "10":
            return VoyageUI().UpdateVoyageCaptain()
        elif choice == "11":
            return VoyageUI().soldSeatsForVoyage()
        elif choice == "12":
            return VoyageUI().ListStatusOfVoyages()
        elif choice == "13":
            return VoyageUI().register_recuring_voyage()

        elif choice == "q":
            return "quit_run"
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()
    
    def getDInput(self):
        choice = input("\nEnter a command: ")
        if choice == "1":
            return DestinationUI().register_destination()
        elif choice == "2":
            return DestinationUI().print_destinations()
        elif choice == "3":
            return DestinationUI().change_destination_contact_info()
        elif choice == "4":
            return DestinationUI().most_popular_destinations()    
        elif choice == "q":
            return "quit_run"
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()
    
    def getAInput(self):
        choice = input("\nEnter a command: ")
        if choice == "1":
            return AircraftUI().register_aircraft()
        elif choice == "2":
            return AircraftUI().print_aircrafts()
        elif choice == "3":
            return AircraftUI().showAircraftStatus()
        elif choice == "4":
            return AircraftUI().printAvailableAircrafts()
        elif choice == "q":
            return "quit_run"
        else:
            print("\nInvalid choice! Going to main menu....\n")

        return self.showMainMenu()