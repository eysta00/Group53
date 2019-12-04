import csv
import os
from Employee import Employee
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase


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
            for emp in rows:
                if str(emp["ssn"]) == str(employee.ssn):
                    emp["name"], emp["address"], emp["pilot_bool"], emp['planeType'], emp['phone'], emp['email'] = \
                        employee.name, employee.address, employee.pilot_bool, employee.planeType, employee.phone, employee.email
                    self.__reWriteFileFromList(rows)
                    return
            raise EntryNotInDatabase('try using addEmployee')


# method to rewrite entire data file from list from update Employee
    def __reWriteFileFromList(self, dictList): # writing to new file then rename-ing files and deleting old 
        with open(self.tempFilePath, 'w') as csv_file:
            csvWriter = csv.DictWriter(csv_file, fieldnames = self.__fieldNames_lst)
            for entry in dictList:
                csvWriter.writerow(entry)
            os.remove(self.filePath)
            os.rename(self.tempFilePath, self.filePath)



#class to access an Employe by Social Security Number
    def getEmployeeBySSN(self, employeeSSN_int):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["ssn"]) == str(employeeSSN_int):
                    return Employee(row["name"], row["ssn"], row["address"], row["phone"], row["email"], row["pilot_bool"], row["planeType"])

    def EmplyeeInDataBase_bool(self, employeeSSN_int):

        with open(self.filePath, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file, fieldnames = self.__fieldNames_lst)
            for row in csvReader:
                if str(row["ssn"]) == str(employeeSSN_int):
                    return True
            return False


if __name__ == "__main__":
    data = EmployeesIO("Data/EmployeeData.csv")
    employee = Employee("Oskar", 1611982429, "Einarsnes", 6619798, "oskarp17@ru.is")
    
    try:
        data.addEmployee(employee)
    except EntryInDatabase:
        print('Employee already exists')
    
    print(data.EmplyeeInDataBase_bool(1234567890))

    data.updateEmployee(employee)    


