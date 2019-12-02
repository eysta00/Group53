import csv

class EmployeesIO():
    def __init__(self, filePath):
        self.filePath = filePath

    def addEmployee(self, employee):
        
        with open(self.filePath) as csv_file:
            csvreader = csv.read(csv)

    def updateEmployee(self, employee):
        pass

    def getEmployeeByID(self, employeeID_int):
        pass


if __name__ == "__main__":
    data = EmployeesIO("Data/EmployeesData.csv")



