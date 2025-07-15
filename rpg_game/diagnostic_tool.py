from station_item import StationItem

class DiagnosticTool(StationItem):
    def __init__(self):
        super().__init__(
            name="Diagnostic Tool",
            description="\033[95mAn outdated but functional diagnostic tool designed to interface with maintenance droids.\033[0m",
            usable=True
        )
        self.can_disable_droids = True
    
    def use_on_droid(self):
        return "The diagnostic tool interfaces with the droid's systems."
    
    def run_diagnostic(self):
        return ("\033[32m[Running Diagnostic Scan... ███████░░░ 70%]"
                "\nError Code: M-43X Detected"
                "\nStatus: Droid mobility subroutine malfunctioning.\033[0m"
                "\n--------------------------------------\n")
    
    def diagnostic_faults(self):
        return ("\033[32mDiagnostic Complete.\033[0m\n"
                "Detected Faults:\n"
                " -Motor Controller Failure\n"
                " -Sensor Loop Error\n"
                "\n------------------------------------\n"
                "\033[1mLocation: Maintenance Tunnel\033[0m\n"
                "\033[34m1. Attempt to reboot motor controller\n"
                "2. Bypass sensor loop\n"
                "3. Exit diagnostic\033[0m")

        
