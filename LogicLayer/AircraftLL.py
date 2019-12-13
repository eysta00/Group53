from InstanceClasses.Aircraft import Aircraft
# from InstanceClasses.AircraftIO import AircraftIO
from IO.IOAPI import IOAPI
from datetime import datetime
from Exceptions.Exceptions import EntryInDatabase
from Exceptions.Exceptions import EntryNotInDatabase
from dateutil.parser import *
from dateutil.relativedelta import *



class AircraftLL:
    def __init__(self):
        self.data = IOAPI()

    def RegisterAircraft(self, manufacturer_str, model_str, totalseats_str):
        aircraft_id = self._GenerateNewAircraftID()
        self.data.addAircraft(Aircraft(aircraft_id, manufacturer_str, model_str, totalseats_str))


    def ListAllAircrafts(self):
        aircrafts = self.data.getAllAircrafts()
        aircrafts.sort(key=lambda x: x.model)
        return aircrafts


    def ShowStatusOfAircrafts(self): # returns a list of tuples (aircraft, status)
        aircrafts = self.data.getAllAircrafts()
        ret_list = []
        time = datetime.now().isoformat()
        for air in aircrafts:
            ret_list.append((air, self.AircraftStatus(air.aircraftID, time)))
        return ret_list
        

    def AircraftStatus(self, aircraftID, time_iso):
        aircraft = self.data.getAircraftByAircraftID(aircraftID)
        voyages = self.data.getAllVoyages()
        timeParsed = parse(time_iso)
        for voy in voyages:
            if str(voy.aircraftID) == str(aircraftID):
                # print('hit this spot')
                # print(voy.aircraftID, end = ' : ')
                # print(aircraftID)
                
                voyageTimes = self._getTimeOfVoyageActivities(voy)
                if timeParsed > voyageTimes[0] and timeParsed < voyageTimes[3]:
                    if timeParsed > voyageTimes[2]:
                        return "Returning to Iceland"
                    elif timeParsed > voyageTimes[1]:
                        return "Idle at Destination"
                    else:
                        return "Flying to Destination"
        return "Unoccupied"

    def ListAvailableAircrafts(self, time):
        aircrafts = self.data.getAllAircrafts()
        availableAircrafts = []
        for air in aircrafts:
            if self.AircraftStatus(air.aircraftID, time) == "Unoccupied":
                availableAircrafts.append(air)
        return availableAircrafts

                    
    def _GenerateNewAircraftID(self):
        aircrafts = self.data.getAllAircrafts()
        iteration = 1
        highest_id = 0
        for air in aircrafts:
            if iteration <= 1:
                print('aircraftID: ', air.aircraftID)
                highest_id = int(air.aircraftID)
            else:
                if int(air.aircraftID) > highest_id:
                    highest_id = int(air.aircraftID)
            
            iteration += 1
        return highest_id + 1 # returns an integer that is 1 higher than the highest id any voyage has in the database


    def _getTimeOfVoyageActivities(self, voyage): # returns list [<Departure from iceland>, <Arrival at destination>, <departure from destination>, <Arrival at Iceland>]
        destination = self.data.getDestinationByDestinationID(voyage.destination)
        
        try:
            StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError:
            StartTime_dateTime = datetime.strptime(voyage.departureTime, '%Y-%m-%dT%H:%M:%S')

        flightTime = float(destination.flight_duration) # consider changing this to int so as to not miss the disimal places!
        deltaHours = flightTime
        deltaMinutes = (deltaHours%1)*60
        deltaSeconds = (deltaMinutes%1)*60
        deltaHours = int(deltaHours)
        deltaMinutes = int(deltaMinutes)
        deltaSeconds = int(deltaSeconds)

        DepartureFromIceland = parse(StartTime_dateTime.isoformat())
        ArrivalAtDestination = parse((StartTime_dateTime + relativedelta(hours=+(flightTime), minutes=+deltaMinutes, seconds=+deltaSeconds)).isoformat())
        DepartureFromDestination = parse((StartTime_dateTime + relativedelta(hours=+(flightTime+1), minutes=+deltaMinutes, seconds=+deltaSeconds)).isoformat())
        ArrivalAtIceland = parse((StartTime_dateTime + relativedelta(hours=+(flightTime*2+1), minutes=+deltaMinutes*2, seconds=+deltaSeconds*2)).isoformat())
        return [DepartureFromIceland, ArrivalAtDestination, DepartureFromDestination, ArrivalAtIceland] # Assuming the rest at destination is 1 hour


if __name__ == "__main__":
    logic = AircraftLL()
    print(logic._GenerateNewAircraftID())