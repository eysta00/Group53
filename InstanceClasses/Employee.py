class Employee:
    # Instance Class for Employees
    def __init__(self, name, ssn, address, phone, email, pilot_bool = False, planeType = None):
        self.name = name 
        self.ssn = ssn
        self.address = address
        self.phone = phone
        self.email = email
        self.assigned = 0
        self.date = ''
        self.dest = ''
        self.pilot_bool = pilot_bool
        self.permissions = []
        self.data = {}
        self.planeType = planeType

    def __str__(self):
        if self.pilot_bool:
            pilot_str = "Pilot"
        else:
            pilot_str = "Flight Attendant"
        return_str = "{:40}\t{:10}\t{:20}\t{:10}\t{:35}\t{:20}\t{}".format(self.name, self.ssn, self.address, self.phone, self.email, pilot_str, self.planeType)
        return return_str

    def __repr__(self):
        return self.name + ' : ' + self.ssn