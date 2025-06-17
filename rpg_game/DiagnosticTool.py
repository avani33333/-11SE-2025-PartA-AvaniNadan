from StationItem import StationItem
class DiagnosticTool(StationItem):
    def __init__(self, name="Diagnostic Tool", description="This diagnostic tool seems designed to interface with maintenance droids."):
        super().__init__(name, description)
        self.found = False

    def find_room(self,room=True,check_locker=False):
        if room == 1:
            return "Rusty vending machines and overturned chairs. There’s a faint hum in the wall panels. Nothing of use here. Just stale energy bars and broken circuits."
        elif room == 2:
            return "Rows of old metal lockers line the wall. A few are open, others rusted shut. You search carefully..."
            check_locker=True
            continue

        elif room == 3:
            return " Crates and crates of defunct tech. It’s too cluttered to search thoroughly right now. Looks like a dead end."
        else:
            return "Enter a valid input (1-3)."

    def check_locker(self, locker_number, room = 2):
        if locker_number == 1:
            self.found = False
            return "Empty"

        elif locker_number == 2:
            self.found = False
            return "Moldy boots"
        elif locker_number == 3:
            self.found = True
            return "You found the Diagnostic Tool!"
        else:
            return "Enter a valid input (1-3)."

