temp = 0 


try:
    temp = open('Output/DestinationData_c.csv', 'w+')
    temp.close()
except FileNotFoundError:
    pass

try:
    temp = open('Output/AircraftData_c.csv', 'w+')
    temp.close()
except FileNotFoundError:
    pass

try:
    temp = open('Output/EmployeeData_c.csv', 'w+')
    temp.close()
except FileNotFoundError:
    pass

try:
    temp = open('Output/VoyageData_c.csv', 'w+')
    temp.close()
except FileNotFoundError:
    pass