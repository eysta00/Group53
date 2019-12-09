from Exceptions.Exceptions import *
from LogicLayer.LLAPI import *

from datetime import datetime
from dateutil.parser import *
from dateutil.relativedelta import *


logic = LLAPI()
time = datetime(2020, 1, 8, 18, 0, 0).isoformat()
print(logic.ListAssignedEmployees(time))

logic.AddStaffToVoyage(3, '1234567890')