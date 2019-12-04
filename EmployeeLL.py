from Employee import Employee
from IOAPI import IOAPI
from datetime import datetime
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase

class EmployeeLL:
    def __init__(self):
        data = IOAPI()

    def RegisterEmployee(self, name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str):
        try:
            data.addEmployee(Employee(name_str, ssn_str, address_str, phone_str, email_str, isPilot_bool, planeLicense_str))
            return 1 #Just a status code to say if the call was successfull, successfull if >= 0
        except EntryInDatabase:
            return -1

    
