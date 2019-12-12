class Employee:
    def __init__(self, name, ssn, address, phone, email, pilot_bool = False, planeType = None):
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
        if self.pilot_bool:
            pilot_str = "Pilot"
        else:
            pilot_str = "Flight Attendant"
        return_str = "{:40}\t{:10}\t{:20}\t{:10}\t{:35}\t{:20}\t{}".format(self.name, self.ssn, self.address, self.phone, self.email, pilot_str, self.planeType)
        return return_str

    def __repr__(self):
        return self.name + ' : ' + self.ssn