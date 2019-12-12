from Exceptions.Exceptions import *
from LogicLayer.LLAPI import *
from LogicLayer.AircraftLL import *
from LogicLayer.VoyageLL import *

from datetime import datetime
from dateutil.parser import *
from dateutil.relativedelta import *
# from InputData.clear_output import *
# from InputData.converter import *


logicAPI = LLAPI()
logicVoyage = VoyageLL()
# time = datetime(2020, 1, 8, 18, 0, 0).isoformat()
# print(logicAPI.ListAssignedEmployees(time))
# logicAPI.AddVoyage(3, datetime(2019, 12, 10, 12).isoformat())

# print(logicAPI.AddStaffToVoyage(4, '1234567890'))

# logicAPI.AssignAircraftToVoyge(4, 1)


# print(logicAPI.AircraftStatus(1))

# print(logicAPI.ShowStatusOfAircrafts())

# logicAPI.UpdateDestinationContactNumber(1, '6619798')

# print(logicAPI.ListVoyageFlightAttendants(1))

# logicAPI.UpdateVoyageCaptain(3, '1234567890')
# logicAPI.SellSeatsForVoyage(3,25)
# print(logicVoyage._GenerateFlightID(2, datetime.now().isoformat()))
# logicAPI.AddVoyage(2, datetime(2019, 12, 25, 18, 50).isoformat())
# logic = AircraftLL()
# voyage = logicAPI.getVoyageByVoyageID(3)
# print(voyage)
# print(logic._getTimeOfVoyageActivities(voyage))
employees = logicAPI.ListAllEmployees()
print(type(employees[1].pilot_bool))
