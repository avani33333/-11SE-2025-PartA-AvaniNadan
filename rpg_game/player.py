
class Player: 
    def __init__(self, name: str, score: int = 0, hazards: int = 0):
        """Represents the player character in the RPG game."""
        self.name = name  # Holds player's name.
        self.score = score  # Stores the player's score.
        self.hazards = hazards  # Counts the number of hazards encountered.
        self.current_location = None  # Holds the current location of the player.
        self.inventory = []  # List to hold items in the player's inventory.
        self.station_items = []  # List to hold station items such as energy crystal and diagnostic tool.
        self.crystal_picked_up = False  # Indicates if the energy crystal has been picked up.
    
    def show_status(self):
        """Displays the player's status including score, hazards, and current location.""" 
        print(f"\033[95m\033[1mStatus for Specialist {self.name}:\033[0m\033[0m") 
        print(f"\033[95mScore: {self.score}\033[0m") 
        print(f"\033[95mHazards Encountered: {self.hazards}\033[0m") 

        if self.current_location:
            print(f"\033[95mCurrent Location: {self.current_location.get_full_location_name()}\033[0m") 

    def show_checklist(self):
        """Displays the player's checklist with completed and pending objectives."""
        print(f"\033[92m\033[1m{self.name}'s Checklist:\033[0m\033[0m") 

        if self.has_item("Diagnostic Tool"):
            print("\033[92m✓ Find a tool that can damage droids\033[0m") 

        else:
            print("\033[92m- Find a tool that can damage droids\033[0m")
        
        if self.has_item("Energy Crystal"):
            print("\033[92m✓ Find the energy crystal\033[0m")

        else:
            print("\033[92m- Find the energy crystal\033[0m")
        print("\033[92m- Reach the docking bay and type 'win' to complete the mission\033[0m")
    
    def add_score(self, points: int):
        """Adds points to the player's score.""" 
        self.score += points 
    
    def add_hazard(self):
        """Increments the hazard count by one.""" 
        self.hazards += 1 
    
    def move_to_location(self, location):
        """Sets the player's current location to the specified location.""" 
        self.current_location = location 
    
    def add_to_inventory(self, item):
        """Adds an item to the player's inventory.""" 
        self.inventory.append(item) 
    
    def add_station_item(self, station_item):
        """Adds a station item to the player's station items list."""
        self.station_items.append(station_item)
        self.inventory.append(station_item.name)
    
    def has_item(self, item_name):
        """Checks if the player has a specific item in their inventory."""
        return item_name in self.inventory
    
    def get_station_item(self, item_name):
        """Retrieves a station item by its name from the player's station items."""
        for item in self.station_items:

            if item.name == item_name:
                return item

        return None
    
    def show_inventory(self): 
        """Displays the player's inventory."""
        print(f"\033[91m\033[1m{self.name}'s Inventory:\033[0m\033[0m") 
        
        if self.inventory: 
            for item in self.inventory: 
                print(f"\033[91m- {item}\033[0m") 
        
        else: 
            print("\033[91mEmpty\033[0m") 
    
    def show_backpack_options(self):
        """Displays the options for the backpack.""" 
        print("------------------------------------") 
        print("\033[91mI: Inventory\033[0m") 
        print("\033[95mS: Status\033[0m") 
        print("\033[92mC: Checklist\033[0m")
