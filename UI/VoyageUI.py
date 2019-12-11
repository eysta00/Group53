from LogicLayer.LLAPI import LLAPI

class VoyageUI:
    def __init__(self):
        self.LLAPI = LLAPI()
    
    def addVoyage(self):
        return LLAPI().addVoyage()
    
    def ListVoyages(self):
        return LLAPI().ListAllVoyages()

# test1 = VoyageUI()
# test1.addVoyage()