import csv
import os
from InstanceClasses.Employee import Employee
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase



class EmployeesIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.tempFilePath = 'Data/EmployeeTemp.csv'
        self.__fieldNames_lst = ["ssn", "name", "address", "phone", "email", "pilot_bool", "planeType"]

# Method to add an employee to the database
    def addEmployee(self, employee):
        
        if self.EmplyeeInDataBase_bool(employee.ssn): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateEmployee with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            csvWriter.writerow({"ssn" : employee.ssn, "name" : employee.name, "address" : employee.address, "pilot_bool" : employee.pilot_bool,\
                "planeType" : employee.planeType, "phone" : employee.phone, "email" : employee.email})

    
# Method to update an employee in the database
    def updateEmployee(self, employee):
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            rows = list(csvReader)
            for emp in rows:
                if str(emp["ssn"]) == str(employee.ssn):
                    emp["name"], emp["address"], emp["pilot_bool"], emp['planeType'], emp['phone'], emp['email'] = \
                        employee.name, employee.address, employee.pilot_bool, employee.planeType, employee.phone, employee.email
                    self.__reWriteFileFromList(rows)
                    return
            raise EntryNotInDatabase('try using addEmployee')

# method to rewrite entire data file from list from update Employee
    def __reWriteFileFromList(self, dictList): 
        with open(self.filePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)



# Method to access an Employe by Social Security Number
    def getEmployeeBySSN(self, employeeSSN_int):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["ssn"]) == str(employeeSSN_int):
                    name = row["name"]
                    ssn = row["ssn"]
                    address = row["address"]
                    phone = row["phone"]
                    email = row["email"]
                    pilot_bool = row["pilot_bool"] == "True" #this is because it is stored as a string in the file
                    planeType = row["planeType"]

                    
                    return Employee(name, ssn, address, phone, email, pilot_bool, planeType)

# Method to check if employee ssn in already in the database
    def EmplyeeInDataBase_bool(self, employeeSSN_int):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["ssn"]) == str(employeeSSN_int):
                    return True
            return False
# Returns all Employees stored in a list
    def getAllEmployees(self): 
        return_list = []
        
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                name = row["name"]
                ssn = row["ssn"]
                address = row["address"]
                phone = row["phone"]
                email = row["email"]
                pilot_bool = row["pilot_bool"] == "True" #this is because it is stored as a string in the file
                planeType = row["planeType"]

                return_list.append(Employee(name, ssn, address, phone, email, pilot_bool, planeType))
        return return_list
    
               

if __name__ == "__main__":
    data = EmployeesIO("Data/EmployeeData.csv")
    employee = Employee("Oskar", 1611982429, "Einarsnes", 6619798, "oskarp17@ru.is")
    
    try:
        data.addEmployee(employee)
    except EntryInDatabase:
        print('Employee already exists')
    
    print(data.EmplyeeInDataBase_bool(1234567890))

    data.updateEmployee(employee)

    print(data.getAllEmployees())    


