from Voyage import Voyage
from Exceptions import EntryInDatabase
from Exceptions import EntryNotInDatabase
from IOAPI import IOAPI


class VoyageLL:
    def __init__(self):
        self.data = IOAPI()

    def ListAllVoyages(self):
        return self.data.VoyageData.getAllVoyages()
        