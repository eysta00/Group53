class Employee:
    def __init__(self, name, ssn, address, phone, email, pilot_bool = False, planeType):
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
