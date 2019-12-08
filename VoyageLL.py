from Voyage import Voyage
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase
from IOAPI import IOAPI
# import dateutil.parser


class VoyageLL:
    def __init__(self):
        self.data = IOAPI()

    def ListAllVoyages(self):
        return self.data.getAllVoyages()


    # We should possibly edit the code so that it doesn't access the stored instances in the classes directly but through methods
    def AddStaffToVoyage(self, voyageID, employeeSSN): 
        
        try:
            voyage = self.data.getVoyageByVoyageID(voyage.voyageID)
            employee = self.data.getEmployeeBySSN(employeeSSN)
            if employee.pilot_bool:
                voyage.pilots_lst.append(employeeSSN)
            else:
                voyage.flightAttendats_lst.append(employeeSSN)
            self.data.updateVoyage(voyage)
            return 1
        except: # error code to see if voyage is successfully updated
            return -1

    def addVoyage(self, destination_id, flightTime_str):
        
        # implement logic checking if there's enough staff available at the given time here

        try:
            voyage = Voyage(self.__GenerateNewVoyageID(), destination_id, flightTime_str)
            self.data.addVoyage(voyage)
            return 1
        except:
            return -1


    def _GenerateNewVoyageID(self):
        voyages = self.data.getAllVoyages()
        iteration = 1
        for voy in voyages:
            if iteration <= 1:
                highest_id = int(voy.voyageID)
            else:
                if int(voy.voyageID) > highest_id:
                    highest_id = int(voy.voyageID)
            
            iteration += 1
        return highest_id + 1 # returns an integer that is 1 higher than the highest id any voyage has in the database

if __name__ == "__main__":
    logic = VoyageLL()
    print(logic._GenerateNewVoyageID())