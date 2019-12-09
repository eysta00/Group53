from VoyageLL import VoyageLL

class VoyageUI:
    def __init__(self):
        self.VoyageLL = VoyageLL()
    
    def addVoyage(self):
        return VoyageLL().addVoyage()
    
    def ListVoyages(self):
        return VoyageLL().ListAllVoyages()

test1 = VoyageUI()
test1.addVoyage()