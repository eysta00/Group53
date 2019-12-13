class EntryInDatabase(Exception):
    pass
class EntryNotInDatabase(Exception):
    pass
class DepartureTimeOccupied(Exception):
    pass
class ToFewAvailableEmployees(Exception):
    pass
class EmployeeAlreadyAssigned(Exception):
    pass
class NotEnoughSeats(Exception):
    pass
class AircraftNotRegistered(Exception):
    pass