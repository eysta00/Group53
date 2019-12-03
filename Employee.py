class Employee:
    def __init__(self, name, ssn, address, phone, email, planeType, pilot_bool = False):
        self.name = name #split for first, and surname
        self.ssn = ssn
        self.address = address
        self.phone = phone
        self.email = email
        self.assigned = 0
        self.date = ''
        self.dest = ''
        self.pilot_bool = pilot_bool
        # self.attendant = attend_bool
        self.permissions = []
        # self.licenses = licenses.split()
        self.data = {}
        self.planeType = planeType

    def updatdata(self):
        self.data['name'] = self.name
        self.data['ssn'] = self.ssn
        self.data['address'] =self.address
        self.data['phone'] = self.phone
        self.data['email'] = self.email
        self.data['assigned'] = self.assigned
        self.data['date'] = self.date
        self.data['dest'] = self.dest
        self.data['is pilot'] = self.pilot_bool
        self.data['is attendant'] = self.attendant
        self.data['permissions'] = self.permissions
        self.data['licenses'] = self.licenses

    def __str__(self):
        return_str = 'name: ' + self.name + ', ssn: ' + self.ssn + ', address: ' + self.address + ', phone: ' + self.phone + ', email: ' + self.email + ', plane type: ' + self.planeType
        if self.pilot_bool:
            return_str += ", Position: Pilot"
        else:
            return_str += ', Position: Flight Attendant'
        return return_str