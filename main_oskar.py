from Exceptions.Exceptions import *
from LogicLayer.LLAPI import *
from LogicLayer.AircraftLL import *

from datetime import datetime
from dateutil.parser import *
from dateutil.relativedelta import *


logicAPI = LLAPI()
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
logicAPI.SellSeatsForVoyage(3,25)

# logic = AircraftLL()
# voyage = logicAPI.getVoyageByVoyageID(3)
# print(voyage)
# print(logic._getTimeOfVoyageActivities(voyage))