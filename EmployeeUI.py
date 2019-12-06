from EmployeeLL import EmployeeLL

class EmployeeUI:
    def __init__(self):
        self.EmployeeLL = EmployeeLL()

    def register_employee(self):
        print(10*"X")
        e_name = input("Full employee name: ")
        e_ssn = input("Employee social securtiy number: ")
        e_address = input("Employee Adress: ")
        e_phone = input("Employe phone number: ")
        e_email = input("Employee email: ")
        e_pilot = bool(True)#input("Is employee a pilot? ")
        e_planelicense = input("Employee plane license: ")
        error = self.EmployeeLL.RegisterEmployee(e_name, e_ssn, e_address, e_phone, e_email, e_pilot, e_planelicense)
        #print(error)
        if error != 1:
            print("Error, input not valid!")
        
        return
    
    def list_employees(self):
        

#test1 = EmployeeUI()
#test1.register_employee()
