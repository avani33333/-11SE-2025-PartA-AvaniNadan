from StationItem import StationItem

class EnergyCrystal(StationItem):
    def __init__(self):
        super().__init__(
            name="Energy Crystal",
            description="The crystal pulses with an unstable, vibrant energy.",
            usable=False
        )
        self.mission_critical = True
    
    def activate(self):
        return "The energy crystal pulses brighter, ready to restore station power."
