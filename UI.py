def default_operation():
    print('This operation is still WIP.\nThank you for your patience. :)')

class UI:
    def __init__(self, name, flag, options = [], oper = default_operation):
        self.name = name
        self.flag = flag
        self.options = options
        self.oper = oper

    def __str__(self):
        return self.name

    def get_type(self):
        return self.flag

class Menu(UI):

    pass

class Operation(UI):

    def do_op(self):
        self.oper()

    def add_pilot():
        full_name = input('Full Name: ')
        ssn = input('Social Security Number: ')
        addr = input('Home Address: ')
        phone = input('Phone Number: ')
        email = input('Email Address: ')
        lcnse = input('Pilots License(s): ')
        API.add_pilot(full_name, ssn, addr, phone, email, lcnse)

    def add_attendant():
        full_name = input('Full Name: ')
        ssn = input('Social Security Number: ')
        addr = input('Home Address: ')
        phone = input('Phone Number: ')
        email = input('Email Address: ')
        API.add_attendant(full_name, ssn, addr, phone, email)

    def add_aircraft():
        model = input('Aircraft Model: ')
        manufacturer = input('Aircraft Manufacturer: ')
        total_seats = input('Number of Seats: ')
        req_licenses = input('Required Piloting Licenses: ')
        API.add_aircraft(model, manufacturer, total_seats, req_licenses)

    def add_flight():
        print('Flight 1: ')
        a_num = input('Flight Number: ')
        a_dest = input('Destination: ')
        a_dest_cont = input('Destination Contact Info: ')
        a_date = input('Date: ')
        a_end_date = input('End Date: ')
        a_depar = input('Departure Time: ')
        a_arcrft = input('Aircraft Id: ')
        print('\nFlight 2: ')
        b_num = input('Flight Number: ')
        b_dest = input('Destination: ')
        b_dest_cont = input('Destination Contact Info: ')
        b_date = input('Date: ')
        b_end_date = input('End Date: ')
        b_depar = input('Departure Time: ')
        b_arcrft = input('Aircraft Id: ')
        API.add_flight(a_num, a_dest, a_dest_cont, a_date, a_end_date, a_depar, a_arcrft, b_num, b_dest, b_dest_cont, b_date, b_end_date, b_depar, b_arcrft)
