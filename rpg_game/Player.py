
class Player:
    def __init__(self, name: str, score: int = 0, hazards: int = 0):
        self.name = name
        self.score = score
        self.hazards = hazards
        self.current_location = None
        self.inventory = []

    def show_status(self):
        print(f"\033[1mStatus for Specialist {self.name}:\033[0m")
        print(f"Score: {self.score}")
        print(f"Hazards Encountered: {self.hazards}")
        if self.current_location:
            print(f"Current Location: {self.current_location.get_full_location_name()}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
    
    def show_checklist(self):
        print(f"\033[1m{self.name}'s Checklist:\033[0m")
        print("- Find a tool that can damage droids")
        print("- Find the energy crystal")
        print("- Reach the docking bay and type 'win' to complete the mission")

    def add_score(self, points: int):
        self.score += points
        
    def add_hazard(self):
        self.hazards += 1
    
    def move_to_location(self, location):
        self.current_location = location
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def show_inventory(self):
        print(f"\033[1m{self.name}'s Inventory:\033[0m")
        if self.inventory:
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Empty")
    
    def show_backpack_options(self):
        print("------------------------------------")
        if self.current_location:
            print(f"Location: {self.current_location.get_full_location_name()}")
        print("4: Inventory")
        print("5: Status")
        print("6: Checklist")
