class API:
    def add_pilot(full_name, ssn, addr, phone, email, lcnse):
        LL.add_pilot(full_name, ssn, addr, phone, email, lcnse)

    def add_attendant(full_name, ssn, addr, phone, email):
        LL.add_attendant(full_name, ssn, addr, phone, email)

    def add_aircraft(model, manufacturer, total_seats, req_licenses):
        LL.add_aircraft(model, manufacturer, total_seats, req_licenses)

    def add_flight(a_num, a_dest, a_dest_cont, a_date, a_end_date, a_depar, a_arcrft, b_num, b_dest, b_dest_cont, b_date, b_end_date, b_depar, b_arcrft):
        LL.add_flight(a_num, a_dest, a_dest_cont, a_date, a_end_date, a_depar, a_arcrft, b_num, b_dest, b_dest_cont, b_date, b_end_date, b_depar, b_arcrft)
