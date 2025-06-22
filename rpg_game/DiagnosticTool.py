from StationItem import StationItem

class DiagnosticTool(StationItem):
    def __init__(self):
        super().__init__(
            name="Diagnostic Tool",
            description="An outdated but functional diagnostic tool designed to interface with maintenance droids.",
            usable=True
        )
        self.can_disable_droids = True
    
    def use_on_droid(self):
        return "The diagnostic tool interfaces with the droid's systems."
    
    def run_diagnostic(self):
        return "[Running Diagnostic Scan... ███████░░░ 70%]\nError Code: M-43X Detected\nStatus: Droid mobility subroutine malfunctioning." 
    
    def diagnostic_faults(self):
        return ("\033[1mDiagnostic Complete.\033[0m\n"
                "Detected Faults:\n"
                "- Motor Controller Failure\n"
                "- Sensor Loop Error\n"
                "\n------------------------------------\n"
                "Location: Maintenance Tunnel\n"
                "1. Attempt to reboot motor controller\n"
                "2. Bypass sensor loop\n"
                "3. Exit diagnostic")

        
