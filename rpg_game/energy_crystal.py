from station_item import StationItem

class EnergyCrystal(StationItem):
    def __init__(self):
        super().__init__(
            name="Energy Crystal",
            description="A rare energy crystal that powers the station's core systems. It pulses with a faint blue light.",
            usable=False
        )
        self.mission_critical = True  # Indicates if the crystal is critical for mission completion.
    

