class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.has_tool = False
        self.has_crystal = False
        self.droid_present = False

class MaintenanceTunnel(Location):
    def __init__(self,name="Maintenance Tunnel"):
        super().__init__(name)



class DockingBay(StationItem):
    def __init__(self,name="Docking Bay",description=""):
       self.description = "The docking bay is filled with various ships and maintenance droids, all in various states of repair."
