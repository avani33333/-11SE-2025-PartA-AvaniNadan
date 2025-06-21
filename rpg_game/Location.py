class Location: 
    def __init__(self, name, description): 
        self.name = name 
        self.description = description 
        self.exits = {} 
        self.has_tool = False 
        self.has_crystal = False 
        self.droid_present = False 
        self.sub_location = None 
    
    def get_full_location_name(self): 
        if self.sub_location: 
            return f"{self.name} ({self.sub_location})" 
        return self.name 
    
    def display_location_header(self, objective=None): 
        if objective: 
            print(f"\033[1m-{objective}\033[0m") 
        print(self.description) 
        print("------------------------------------") 
        print(f"\033[1mLocation: {self.get_full_location_name()}\033[0m") 

class MaintenanceTunnel(Location): 
    def __init__(self, name="Maintenance Tunnel", description="You stand in the central hub of the maintenance tunnels.\nThree paths branch off: west to the Locker Room, east to the Break Room, and north to the Storage Bay."): 
        super().__init__(name, description) 
    
    def show_central_hub(self): 
        self.display_location_header("Find a tool that can damage droids") 
        print("1: Go East (Break Room)") 
        print("2: Go West (Locker Room)") 
        print("3: Go North (Storage Bay)") 

class BreakRoom(Location): 
    def __init__(self, name="Maintenance Tunnel", description="Rusty vending machines and overturned chairs. There's a faint hum in the wall panels.\nNothing of use here. Just stale energy bars and broken circuits."): 
        super().__init__(name, description) 
        self.sub_location = "Break Room" 
    
    def show_break_room(self): 
        self.display_location_header("Find a tool that can damage droids") 
        print("\x1B[3mPress enter to return to the central hub\x1B[0m") 

class LockerRoom(Location): 
    def __init__(self, name="Maintenance Tunnel", description="Rows of old metal lockers line the wall. A few are open, others rusted shut.\nYou search carefully..."): 
        super().__init__(name, description) 
        self.sub_location = "Locker Room" 
        self.has_tool = True 
    
    def show_locker_room(self): 
        self.display_location_header("Find a tool that can damage droids") 
        print("1: Check Locker 1") 
        print("2: Check Locker 2") 
        print("3: Check Locker 3") 
    
    def show_tool_pickup(self): 
        self.display_location_header("Find a tool that can damage droids") 
        print("You stumble across an outdated Diagnostic Tool inside the locker. It may be still usable.") 
        print("1: Pick it up") 
        print("2: Leave it") 

class StorageBay(Location): 
    def __init__(self, name="Maintenance Tunnel", description="Crates and crates of defunct tech. It's too cluttered to search thoroughly right now.\nLooks like a dead end."): 
        super().__init__(name, description) 
        self.sub_location = "Storage Bay" 
    
    def show_storage_bay(self): 
        self.display_location_header("Find a tool that can damage droids") 
        print("\x1B[3mPress enter to return to the central hub\x1B[0m") 

class DockingBay(Location): 
    def __init__(self, name="Docking Bay", description="The docking bay is filled with various ships and maintenance droids, all in various states of repair."): 
        super().__init__(name, description) 
