import csv
from Employee.py import Employee

class EmployeesIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.fieldNames_lst = ["ssn", "Name", "address", "phone", "email", "pilot_bool", "planeType"]

    def addEmployee(self, employee):
        
        with open(self.filePath, 'a+', newline='') as csv_file:
            csvwriter = csv.write(csv, fieldnames = self.fieldNames_lst)
            # to be updated when employee class is complete
            csvwriter.writerow({"ssn" : employee.ssn, "Name" : employee.name, "address" : employee.address, "pilot_bool" : employee.pilot_bool, "planeType" : employee.planeType})

    def updateEmployee(self, employee):
        pass

    def getEmployeeBySSN(self, employeeID_int):
        pass


if __name__ == "__main__":
    data = EmployeesIO("Data/EmployeesData.csv")
    employee = Employee("John", 1234567890, "localStreet", 5512345, "test@test.tst", pilot_bool = True, "Airbus")
    data.addEmployee()


