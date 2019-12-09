from Exceptions.Exceptions import *
from LogicLayer.LLAPI import *

from datetime import datetime
from dateutil.parser import *
from dateutil.relativedelta import *


logic = LLAPI()
time = datetime(2020, 1, 8, 18, 0, 0).isoformat()
print(logic.ListAssignedEmployees(time))
# logic.AddVoyage(2, datetime(2019, 12, 24, 18).isoformat())

print(logic.AddStaffToVoyage(3, '1611982429'))