class StationItem:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def examine(self):
        return self._description


class DiagnosticTool(StationItem):
    def __init__(self):
        super().__init__("This diagnostic tool seems designed to interface with maintenance droids.")


class EnergyCrystal(StationItem):
    def __init__(self):
        super().__init__("The crystal pulses with an unstable, vibrant energy.")
