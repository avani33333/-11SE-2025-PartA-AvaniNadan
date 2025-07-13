import os

class DamagedMaintenanceDroid:
    def __init__(self):
        self.name = "Damaged Maintenance Droid"
        self.description = "A malfunctioning maintenance droid with sparking circuits and erratic movements."
        self.is_blocking = True
        self.is_disabled = False
        self.diagnostic_attempted = False
    
    def show_initial_encounter(self):
        return ("You reach the east corridor — the only accessible path — but a damaged maintenance droid is guarding it.\n"
                "------------------------------------\n"
                "Location: Maintenance Tunnel\n"
                "\x1B[3mEnter: Move east and try to sneak past\x1B[0m")
    
    def show_blocked_message(self, add_hazard=True):
        print("The droid is blocking the way.")
        if add_hazard:
            print("\033[34m+1 hazard\033[0m")
        print("------------------------------------")
        print("Location: Maintenance Tunnel")
        print("\x1B[3mEnter: Use Diagnostic Tool to disable\x1B[0m")
    
    def show_diagnostic_options(self):
        return ("Would you like to run a diagnostic test?\n"
                "------------------------------------\n"
                "Location: Maintenance Tunnel\n"
                "1: Yes\n"
                "2: No")
    
    def attempt_diagnostic(self, player_has_tool):
        if player_has_tool:
            return "diagnostic_options"
        else:
            return "no_tool_available"
    
    def run_diagnostic_test(self):
        self.is_disabled = True
        self.is_blocking = False
        self.diagnostic_attempted = True
        return ("\n\033[34mAttempting reboot...\033[0m"
                "\n\033Reboot successful!\033[0m"
                "Mobility partially restored.")
    
    def is_path_clear(self):
        return not self.is_blocking
    
    def use_tool(self, run_test, found=True):
        if run_test == "1" and found == True:
            return "\033[34m[Running Diagnostic Scan... ███████░░░ 70%]\nError Code: M-43X Detected\nStatus: Droid mobility subroutine malfunctioning.\033[0m"
        elif run_test == "1" and found == False:
            return "You do not own a diagnostic tool. You need to find one to proceed."
        elif run_test == "2" and found == True:
            return "The droid is blocking the way."
    
    def droid_faults(self, run_test=1, found=True):
        return ("\033[1mDiagnostic Complete.\033[0m"
                "\n\033[94mDetected Faults:"
                "\n -Motor Controller Failure"
                "\n -Sensor Loop Error\033[0m"
                "\n------------------------------------\n"
                "\n\033[1mLocation: Maintenance Tunnel\033[0m"
                "1. Attempt to reboot motor controller\n"
                "2. Bypass sensor loop\n"
                "3. Exit diagnostic")

    def repair_droid(self, option_repair, run_test=1, found=True):
        if option_repair == "1":
            self.is_blocking = False
            self.is_disabled = True
            self.diagnostic_attempted = True
            return ("\n\033[34mAttempting reboot...\033[0m"
                   "\n\033[34mReboot successful!\033[0m"
                   "Mobility partially restored.")
        elif option_repair == "2":
            return "Bypass failed. You must fix the motor controller first."
        elif option_repair == "3":
            self.use_tool(run_test, found)
        else:
            return "Invalid option. Please choose a valid repair option (1-3)."
