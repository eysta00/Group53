QUIT_FLAG = 0

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

    def add_destination():
        dest_name = input('Destination name:')
        dest_id = input('Destination ID:')
        API.add_destination(dest_name, dest_id)

class API:
    def add_pilot(full_name, ssn, addr, phone, email, lcnse):
        LL.add_pilot(full_name, ssn, addr, phone, email, lcnse)

    def add_attendant(full_name, ssn, addr, phone, email):
        LL.add_attendant(full_name, ssn, addr, phone, email)

    def add_aircraft(model, manufacturer, total_seats, req_licenses):
        LL.add_aircraft(model, manufacturer, total_seats, req_licenses)

    def add_flight(a_num, a_dest, a_dest_cont, a_date, a_end_date, a_depar, a_arcrft, b_num, b_dest, b_dest_cont, b_date, b_end_date, b_depar, b_arcrft):
        LL.add_flight(a_num, a_dest, a_dest_cont, a_date, a_end_date, a_depar, a_arcrft, b_num, b_dest, b_dest_cont, b_date, b_end_date, b_depar, b_arcrft)
    
    def add_destination(dest_name, dest_id):
        LL.add_destination(dest_name, dest_id)

class LL:
    def add_pilot(full_name, ssn, addr, phone, email, lcnse):
        plt = Employee(full_name, ssn, addr, phone, email, 1, 0, lcnse)
        plt.update_data()
        #add to data layer
        ALL_DATA.add_employees(plt)

    def add_attendant(full_name, ssn, addr, phone, email):
        attnd = Employee(full_name, ssn, addr, phone, email, 0, 1)
        attnd.update_data()
        #add to data layer
        ALL_DATA.add_employees(attnd)

    def add_aircraft(model, manufacturer, total_seats, req_licenses):
        arcrft = Aircraft(model, manufacturer, total_seats, req_licenses)
        arcrft.update_data()
        #add to data layer
        ALL_DATA.add_aircrafts(arcrft)

    def add_flight(a_num, a_dest, a_dest_cont, a_date, a_end_date, a_depar, a_arcrft, b_num, b_dest, b_dest_cont, b_date, b_end_date, b_depar, b_arcrft):
        a_flght = Flight(a_num, a_dest, a_dest_cont, a_date, a_end_date, a_depar, a_arcrft)
        b_flght = Flight(b_num, b_dest, b_dest_cont, b_date, b_end_date, b_depar, b_arcrft)
        a_flght.update_data()
        b_flght.update_data()
        voy = Voyage(a_flght, b_flght)
        #add
        ALL_DATA.add_flights(a_flght)
        ALL_DATA.add_flights(b_flght)
        ALL_DATA.add_voyages(voy)
    
    def add_destination(dest_name, dest_id):
        dest = Destination(dest_name, dest_id)
        dest.update_data()
        # add to data layer
        ALL_DATA.add_destination(dest)

class Employee:
    def __init__(self, name, ssn, address, phone, email, pilot_bool = 0, attend_bool = 0, licenses = []):
        self.e_name = name #split for first, and surname
        self.e_ssn = ssn
        self.e_address = address
        self.e_phone = phone
        self.e_email = email
        self.e_assigned = 0
        self.e_date = ''
        self.e_dest = ''
        self.e_pilot = pilot_bool
        self.e_attendant = attend_bool
        self.e_permissions = []
        self.e_licenses = licenses.split()
        self.e_data = {}

    def update_data(self):
        self.e_data['name'] = self.e_name
        self.e_data['ssn'] = self.e_ssn
        self.e_data['address'] =self.e_address
        self.e_data['phone'] = self.e_phone
        self.e_data['email'] = self.e_email
        self.e_data['assigned'] = self.e_assigned
        self.e_data['date'] = self.e_date
        self.e_data['dest'] = self.e_dest
        self.e_data['is pilot'] = self.e_pilot
        self.e_data['is attendant'] = self.e_attendant
        self.e_data['permissions'] = self.e_permissions
        self.e_data['licenses'] = self.e_licenses

class Aircraft:
    id_count = 0 #this would need to be loaded in from data for later

    def __init__(self, model, manufacturer, total_seats, req_licenses):
        self.ai_id = Aircraft.gen_id(self)
        self.ai_model = model
        self.ai_manufacturer = manufacturer
        self.ai_total_seats = total_seats
        self.ai_used_seats = 0
        self.ai_pilots = []
        self.ai_permissions = [] #pilots
        self.ai_req_licenses = req_licenses
        self.ai_flight_count = 0
        self.ai_flight_time = 0
        self.ai_status = 0 #0 for OK/1 for maintenence/2 for malfunctioning
        self.ai_data = {}

    def gen_id(self):
        self.id_count += 1
        self.ai_id = self.id_count


    def update_data(self):
        self.ai_data['aircraft id'] = self.ai_id
        self.ai_data['model'] = self.ai_model
        self.ai_data['manufacturer'] = self.ai_manufacturer
        self.ai_data['total seats'] = self.ai_total_seats
        self.ai_data['used seats'] = self.ai_used_seats
        self.ai_data['pilots'] = self.ai_pilots
        self.ai_data['permissions'] = self.ai_permissions
        self.ai_data['required licenses'] = self.ai_req_licenses
        self.ai_data['flight count'] = self.ai_flight_count
        self.ai_data['flight time'] = self.ai_flight_time
        self.ai_data['status'] = self.ai_status
    pass

class Flight:
    def __init__(self, flight_num, destination, dest_contact, date, end_date, departure, aircraft_id):
        self.f_flight_num = flight_num
        self.f_destination = destination 
        self.f_dest_contact = dest_contact
        self.f_date = date
        self.f_end_date = end_date
        self.f_departure = departure
        self.f_status = ''
        self.f_current_pos = ''
        self.f_aircraft_id = aircraft_id
        self.f_work_pr = {}
        self.f_employees = []
        self.f_pilots = []
        self.f_full = 0 #or 1
        self.f_data = {}

    def update_data(self):
        self.f_data['flight number'] = self.f_flight_num
        self.f_data['destination'] = self.f_destination
        self.f_data['destinaiton contact'] = self.f_dest_contact
        self.f_data['date'] = self.f_date
        self.f_data['end date'] = self.f_end_date
        self.f_data['departure'] = self.f_departure
        self.f_data['status'] = self.f_status
        self.f_data['current position'] = self.f_current_pos
        self.f_data['aircraft id'] = self.f_aircraft_id
        self.f_data['work procedures'] = self.f_work_pr
        self.f_data['employees'] = self.f_employees
        self.f_data['pilots'] = self.f_pilots
        self.f_data['flight full'] = self.f_full

    def change_contact(self, new_contact):
        self.f_dest_contact = new_contact

    pass

class Voyage:
    def __init__(self, flight_init, flight_sec):
        self.flight_init = flight_init
        self.flight_sec = flight_sec
        self.v_title = flight_init.f_destination 
        self.v_data = [self.flight_init, self.flight_sec]

    def update_data(self, new_init, new_sec):
        self.flight_init = new_init
        self.flight_sec = new_sec
        self.v_data = [self.flight_init, self.flight_sec]

    def change_contact(self, flight_bool, new_contact): #flight_bool 0 for init flight, 1 for sec
        if flight_bool == 0:
            self.flight_init.f_dest_contact = new_contact
        else:
            self.flight_init.f_dest_contact = new_contact


    pass
class Destination:
    def __init__(self, dest_name, dest_id):
        self.dest_name = dest_name
        self.dest_id = dest_id
        self.d_data ={}

    def update_data(self, new_dname, new_did):
        self.d_data['dest_name'] = self.dest_name
        self.d_data['dest_id'] = self.dest_id


class Data: # class for test without datastructure
    def __init__(self):
        self.employees = {}
        self.aircrafts = {}
        self.flights = {}
        self.voyages = {}
        self.destinations = {}
        self.alldata = {**self.employees, **self.aircrafts, **self.flights, **self.voyages, **self.destinations}
    
    def add_employees(self, emp_obj):
        self.employees[emp_obj.e_name] = emp_obj.e_data
        self.update_alldata()

    def add_flights(self, flght_obj):
        self.flights[flght_obj.f_flight_num] = flght_obj.f_data
        self.update_alldata()

    def add_voyages(self, voy_obj):
        self.flights[voy_obj.v_title] = voy_obj.v_data
        self.update_alldata()

    def add_aircrafts(self, aircraft_obj):
        self.aircrafts[aircraft_obj.ai_id] = aircraft_obj.ai_data
        self.update_alldata()
    
    def add_destination(self, dest_obj):
        self.destinations[dest_obj.dest_id] = dest_obj.d_data

    def update_alldata(self):
        self.alldata = {**self.employees, **self.aircrafts, **self.flights}

    def __str__(self): ##for debug purposes
        all_string = 'Employees list:' + str(self.employees) + '\nAircrafts list:' + str(self.aircrafts) + '\nFlights list:' + str(self.flights)
        return all_string

ALL_DATA = Data()

def pmenu(instance):
    global QUIT_FLAG
    global ALL_DATA
    acc = 1
    temp = ''

    while acc == 1:
        if instance.get_type() == 0:
            border = '#' * (len(str(instance)) * 2) + '\n'
            header = border + ' ' * int((len(str(instance)) / 2)) + str(instance) + '\n' + border
            print(header)
        else:
            border = '-' * (len(str(instance)) * 2) + '\n'
            header = border + ' ' * int((len(str(instance)) / 2)) + str(instance) + '\n' + border
            print(header)

        counter = 1
        for op in instance.options:
            print('\t{}. {}'.format(counter, op))
            counter += 1

        if instance.get_type() == 1:
            instance.do_op()
            print('Press enter to continue...')
            temp = input('')
            return
        else:
            print()

        cmmd_index = input('Enter a command or type \'help\': ')

        if cmmd_index == 'help':
            print('\nEnter the number of a corresponding Menu or Operation to change to that Menu or carry out that Operation.\nOther commands include \'quit\' in order to exit the program and \'back\' to return to the previous Menu.\nPress enter to continue...')
            temp = input('')
        elif cmmd_index == 'data':
            print(str(ALL_DATA))
        elif cmmd_index == 'back':
            return
        elif cmmd_index == 'quit':
            QUIT_FLAG = 1
        else:
            pmenu(instance.options[int(cmmd_index) - 1])

        if QUIT_FLAG == 1:
            return

def testmain():
    global ALL_DATA

    ms1o6 = Operation('List Unassigned Employees', 1)
    ms1o5 = Operation('List Assigned Employees', 1)
    ms1o4 = Operation('List Pilots', 1)
    ms1o3 = Operation('List Employees', 1)
    ms1o2 = Operation('Add Attendent', 1, [], Operation.add_attendant)
    ms1o1 = Operation('Add Pilot', 1, [], Operation.add_pilot)
    ms1 = Menu('Employees', 0, [ms1o1, ms1o2, ms1o3, ms1o4, ms1o5, ms1o6])
    ms2o4 = Operation('Change Destination Contact Info', 1)
    ms2o3 = Operation('List Flights for Date', 1)
    ms2o2 = Operation('Add Flight', 1)
    ms2o1 = Operation('Add Aircraft', 1, [], Operation.add_aircraft)
    ms2 = Menu('Flights and Aircraft', 0, [ms2o1, ms2o2, ms2o3, ms2o4])
    ms301 = Operation('Add Destination', 1, [], Operation.add_destination)
    ms302 = Operation('List Destinations', 1)
    ms3 = Menu('Destinations', 0, [ms301, ms302])
    main_menu = Menu('Main Menu', 0, [ms1, ms2, ms3])
    pmenu(main_menu)

testmain()  
