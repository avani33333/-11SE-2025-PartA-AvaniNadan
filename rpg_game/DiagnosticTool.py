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
        print("[Diagnostic Complete]")
        print("Detected Faults:")
        print("- Motor Controller Failure")
        print("- Sensor Loop Error")
        print("------------------------------------")
        print("Location: Maintenance Tunnel")
        print("1. Attempt to reboot motor controller ")
        print("2. Bypass sensor loop ")
        print("3. Exit diagnostic")

        
