from UI.EmployeeUI import EmployeeUI
X = "a"
while X != "q":
    test1 = EmployeeUI()
    test1.print_all_employees()
    # test1.register_employee()
    test1.print_flight_attendants()
    test1.print_pilots()
    # test1.print_pilots_with_aircraft_privilage()
    X = input("type q to quit, anything else to continue: ")