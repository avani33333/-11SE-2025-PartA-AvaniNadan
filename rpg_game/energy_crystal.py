from StationItem import StationItem

class EnergyCrystal(StationItem):
    def __init__(self):
        super().__init__(
            name="Energy Crystal",
            description="A rare energy crystal that powers the station's core systems. It pulses with a faint blue light.",
            usable=False
        )
        self.mission_critical = True
    
    def activate(self):
        return "The energy crystal pulses brighter, ready restore station power."
