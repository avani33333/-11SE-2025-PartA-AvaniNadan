class Location: 
    def __init__(self, name, description): 
        self.name = name 
        self.description = description 
        self.exits = {}  # Dictionary to hold exits to other locations.
        self.has_tool = False   # Indicates if the location has the diagnostic tool.
        self.has_crystal = False  # Indicates if the location has the energy crystal.
        self.droid_present = False  # Indicates if a droid is present in the location.
        self.sub_location = None   # Indicates if the location has a sub-location.
    
    def get_full_location_name(self): 
        """Returns the full name of the location, including sub-location."""
        if self.sub_location: 
            return f"{self.name} ({self.sub_location})" 
        return self.name 
    
    def display_location_header(self, objective=None): 
        """Displays the header for the current location with a certain objective taken from the player's checklist."""
        if objective: 
            print(f"\033[1m-{objective}\033[0m") 
        print(self.description) 
        print("------------------------------------") 
        print(f"\033[1mLocation: {self.get_full_location_name()}\033[0m") 

class MaintenanceTunnel(Location):
    def __init__(self, name="Maintenance Tunnel", description="You stand in the central hub of the maintenance tunnels.\nThree paths branch off: west to the Locker Room, east to the Break Room, and north to the Storage Bay."): 
        super().__init__(name, description) 
    
    def show_central_hub(self):
        """Displays the options for the central hub.""" 
        self.display_location_header("\033[92mFind a tool that can damage droids\033[0m") 
        print("\033[94m1: Go East (Break Room)\033[0m") 
        print("\033[94m2: Go West (Locker Room)\033[0m") 
        print("\033[94m3: Go North (Storage Bay)\033[0m") 

class BreakRoom(Location): 
    def __init__(self, name="Maintenance Tunnel", description="Rusty vending machines and overturned chairs. There's a faint hum in the wall panels.\nNothing of use here. Just stale energy bars and broken circuits."): 
        super().__init__(name, description) 
        self.sub_location = "Break Room" 
    
    def show_break_room(self):
        """Displays the options for the break room."""
        self.display_location_header("\033[92mFind a tool that can damage droids\033[0m") 
        print("\n\x1B[3m\033[94mPress enter to return to the central hub\x1B[0m\033[0m") 

class LockerRoom(Location): 
    def __init__(self, name="Maintenance Tunnel", description="Rows of old metal lockers line the wall. A few are open, others rusted shut.\nYou search carefully..."): 
        super().__init__(name, description) 
        self.sub_location = "Locker Room" 
        self.has_tool = True 
    
    def show_locker_room(self):
        """Displays the options for the locker room."""
        self.display_location_header("\033[92mFind a tool that can damage droids\033[0m") 
        print("\033[94m1: Check Locker 1\033[0m") 
        print("\033[94m2: Check Locker 2\033[0m") 
        print("\033[94m3: Check Locker 3\033[0m") 
    
    def show_tool_pickup(self): 
        """Displays the options for picking up the diagnostic tool."""
        self.display_location_header("\033[92mFind a tool that can damage droids\033[0m") 
        print("\n\x1B[3mYou stumble across an outdated Diagnostic Tool inside the locker. It may be still usable.\x1B[0m")
        print("-------------------------------------") 
        print("\033[94m1: Pick it up\033[0m") 
        print("\033[94m2: Leave it\033[0m") 
        print("-------------------------------------") 

class StorageBay(Location): 
    def __init__(self, name="Maintenance Tunnel", description="Crates and crates of defunct tech. It's too cluttered to search thoroughly right now.\nLooks like a dead end."): 
        super().__init__(name, description) 
        self.sub_location = "Storage Bay" 
    
    def show_storage_bay(self):
        """Displays the options for the storage bay."""
        self.display_location_header("\033[92mFind a tool that can damage droids\033[0m") 
        print("\n\x1B[3m\033[94mPress enter to return to the central hub\x1B[0m\033[0m") 

class DockingBay(Location): 
    def __init__(self, name="Docking Bay", description="You move east again and arrive at the Docking Bay.\nThe crystal has been relocated to ensure safety.\nChoose one of the following rooms the crystal may be"): 
        super().__init__(name, description)
    
    def show_docking_bay(self):
        """Displays the options for the docking bay."""
        self.display_location_header("\033[92mFind the energy crystal\033[0m")
        print("\033[94m1: Go to Cargo Section\033[0")
        print("\033[94m2: Go to Console Room\033[0")
        print("\033[94m3: Go to Supply Hub\033[0")

class CargoSection(Location):
    def __init__(self, name="Docking Bay", description="You enter the Cargo Section.\n\nCrates and containers are stacked high — some sealed, others partially opened.\nYou spot three distinct cargo units that stand out:"):
        super().__init__(name, description)
        self.sub_location = "Cargo Section"
    
    def show_cargo_section(self):
        """Displays the options for the cargo section."""
        self.display_location_header("\033[92mFind the energy crystal\033[0m")
        print("\033[94m1. A crate marked \"Bio-Specimens\"\033[0")
        print("\033[94m2. A metal box labeled \"Hazardous Tools\"\033[0")
        print("\033[94m3. A dusty container tagged \"Research Debris\"\033[0")
        print("\n\x1B[3mPress enter to return to the Docking Bay\x1B[0m")

class ConsoleRoom(Location):
    def __init__(self, name="Docking Bay", description="You enter the Console Room.\n\nA faint hum echoes from deep within the walls. The air is thick with static, and the screens flicker weakly. Most systems are in standby or diagnostic mode.\n\nThree old control terminals are still powered on:"):
        super().__init__(name, description)
        self.sub_location = "Console Room"
    
    def show_console_room(self):
        """Displays the options for the console room."""
        self.display_location_header("\033[92mFind the energy crystal\033[0m")
        print("\033[94m1. Access the Logistics Terminal\033[0")
        print("\033[94m2. Check the Environmental Control Panel\033[0")
        print("\033[94m3. Use the Security Console\033[0")
        print("\n\x1B[3mPress enter to return to the Docking Bay\x1B[0m")

class SupplyHub(Location):
    def __init__(self, name="Docking Bay", description="You enter the storage area. Cold, metallic, and quiet. Rows of shelves line the walls."):
        super().__init__(name, description)
        self.sub_location = "Supply Hub"
        self.has_crystal = True
    
    def show_supply_hub(self):
        """Displays the options for the supply hub."""
        self.display_location_header("\033[92mFind the energy crystal\033[0m")
        print("\033[94m1. Search Shelf A1\033[0")
        print("\033[94m2. Search Shelf A2\033[0")
        print("\033[94m3. Search Shelf A3\033[0")
        print("\n\x1B[3mPress enter to return to the Docking Bay\x1B[0m")
    
    def show_crystal_pickup(self):
        """Displays the options for picking up the energy crystal."""
        self.display_location_header("\033[92mFind the energy crystal\033[0m")
        print("You find the Energy Crystal carefully secured in a containment pod!")
        print("-------------------------------------")
        print("\033[94m1: Pick it up\033[0m")
        print("\033[94m2: Leave it\033[0m")
        print("-------------------------------------")    

class MaintenanceTunnelEastCorridor(Location):
    def __init__(self, name="Maintenance Tunnel", description="In order to arrive at the docking bay, you must choose one of the following paths."):
        super().__init__(name, description)
    
    def show_east_corridor(self):
        """Displays the options for the east corridor."""
        self.display_location_header("\033[92mFind the energy crystal\033[0m")
        print("\n\033[94m1: West pathway\033[0m")
        print("\033[94m2: East pathway\033[0m")
