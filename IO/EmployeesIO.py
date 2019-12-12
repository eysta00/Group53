import csv
import os
from InstanceClasses.Employee import Employee
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase


# class EntryInDatabase(Exception):
#     pass
# class EntryNotInDatabase(Exception):
#     pass

class EmployeesIO():
    def __init__(self, filePath):
        self.filePath = filePath
        self.tempFilePath = 'Data/EmployeeTemp.csv'
        self.__fieldNames_lst = ["ssn", "name", "address", "phone", "email", "pilot_bool", "planeType"]

    def addEmployee(self, employee):
        
        if self.EmplyeeInDataBase_bool(employee.ssn): # Custom exception raised if trying to add duplicate data
            raise EntryInDatabase("You might want to try updateEmployee with duplicate data")

        with open(self.filePath, 'a+') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            # to be updated when employee class is complete
            csvWriter.writerow({"ssn" : employee.ssn, "name" : employee.name, "address" : employee.address, "pilot_bool" : employee.pilot_bool,\
                "planeType" : employee.planeType, "phone" : employee.phone, "email" : employee.email})

    
    
    def updateEmployee(self, employee):
        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            rows = list(csvReader)
            # print(rows)
            for emp in rows:
                if str(emp["ssn"]) == str(employee.ssn):
                    emp["name"], emp["address"], emp["pilot_bool"], emp['planeType'], emp['phone'], emp['email'] = \
                        employee.name, employee.address, employee.pilot_bool, employee.planeType, employee.phone, employee.email
                    self.__reWriteFileFromList(rows)
                    return
            # print('raising an error')
            raise EntryNotInDatabase('try using addEmployee')

# ["ssn", "name", "address", "phone", "email", "pilot_bool", "planeType"]
# method to rewrite entire data file from list from update Employee
    def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
        with open(self.filePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)



#class to access an Employe by Social Security Number
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

    def EmplyeeInDataBase_bool(self, employeeSSN_int):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["ssn"]) == str(employeeSSN_int):
                    return True
            return False

    def getAllEmployees(self): # Returns all Employees stored in a list
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
    
    def ListALLStaff(self):
        print("{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}".format("SSN", "NAME", "ADDRESS", "PHONE", "EMAIL", "PILOT_BOOL", "PLANETYPE"))
        with open(self.filePath, 'r') as csv_file:
            # csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csv_file:
                name,ssn,address,phone,email,pilot_bool,planeType = row.strip().split(",")
                print("{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}".format(name,ssn,address,phone,email,pilot_bool,planeType))
               

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


