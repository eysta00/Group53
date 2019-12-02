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
