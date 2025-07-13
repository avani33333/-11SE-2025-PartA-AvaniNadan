import sys
import os
from player import Player
from location import MaintenanceTunnel
from location import BreakRoom
from location import LockerRoom
from location import StorageBay
from location import DockingBay
from damaged_maintenance_droid import DamagedMaintenanceDroid
from diagnostic_tool import DiagnosticTool
from energy_crystal import EnergyCrystal
from location import MaintenanceTunnelEastCorridor
from location import CargoSection
from location import ConsoleRoom
from location import SupplyHub
from constants import (
    PLAYER_SCORE, HAZARDS_ENCOUNTERED, GAME_MESSAGE, WELCOME_MESSAGE, WEST_TUNNEL_MESSAGE, BACKPACK_OPTIONS, RUN_DIAGNOSTIC_OPTIONS, CHOICE_1_CARGO_SECTION, CHOICE_2_CARGO_SECTION, CHOICE_3_CARGO_SECTION, CHOICE_1_CONSOLE_ROOM, CHOICE_2_CONSOLE_ROOM, CHOICE_3_CONSOLE_ROOM, CHOICE_1_SUPPLY_HUB, CHOICE_2_SUPPLY_HUB, POINTS_REWARD_CRYSTAL, NO_POINTS_REWARD_CRYSTAL, TYPE_WIN_DOCKING_BAY, COMPLETED_GAME_MESSAGE
)

#clear the terminal screen
def clear_screen() -> None: 
    os.system('cls' if os.name == 'nt' else 'clear') 

#asks player to press enter to continue
def press_enter() -> None: 
    input("Enter: Continue") 

class GameIntroduction: 
    def __init__(self, player=None) -> None: 
        self.player = None #player instance will be set later, once player enters their name
    
    def show_intro(self) -> None: 
        clear_screen() 
        print("\033[0m" + WELCOME_MESSAGE) #print welcome message
        
        while True: 
            player_name = input("\033[3mEnter your name, Specialist: \033[0m").strip() #prompt for player name
            if player_name: 
                break #if name is not empty the loop breaks 
            print("Name cannot be empty. Please try again.") 
        
        self.player = Player(player_name.capitalize()) 
        clear_screen() 
        print(GAME_MESSAGE.format(player_name=self.player.name)) #using the player's name for the game message (constant)

class RPGGameRun: #class for the main rpg to run
    def __init__(self): 
        self.player = None 
        self.droid = DamagedMaintenanceDroid() 
        self.droid_encounter_triggered = False
        self.in_droid_encounter = False 
        self.droid_repaired = False
        self.crystal_encountered = False 
        self.crystal_left_behind = False  
        self.locations = { 
            'central_hub': MaintenanceTunnel(), 
            'break_room': BreakRoom(), 
            'locker_room': LockerRoom(), 
            'storage_bay': StorageBay(), 
            'docking_bay': DockingBay(),
            'east_corridor': MaintenanceTunnelEastCorridor(),
            'cargo_section': CargoSection(),
            'console_room': ConsoleRoom(),
            'supply_hub': SupplyHub()
        }
    
    def start_game(self): 
        game_intro = GameIntroduction() #creates a new instance for GameIntroduction 
        game_intro.show_intro() #shows the introduction message and prompts for player name
        self.player = game_intro.player #player name is set as self.player in RPGGameRun class
        self.player.move_to_location(self.locations['central_hub']) #moves player to the central hub
        press_enter() 
        self.show_current_location() #shows the current location of the player which is central hub 
        self.game_loop() #starts the main loop of the game
    
    def show_current_location(self): # displays the current location of the player 
        clear_screen() 
        if self.player.current_location == self.locations['central_hub']: 
            self.locations['central_hub'].show_central_hub() #checks if player is in central hub and shows the show_central_hub() function in maintenance tunnel class
        elif self.player.current_location == self.locations['break_room']: 
            self.locations['break_room'].show_break_room()  # checks if player is in break room and shows the show_break_room() function in break room class
        elif self.player.current_location == self.locations['locker_room']: 
            self.locations['locker_room'].show_locker_room() # checks if player is in locker room and shows the show_locker_room() function in locker room class
        elif self.player.current_location == self.locations['storage_bay']: 
            self.locations['storage_bay'].show_storage_bay() # checks if player is in storage bay and shows the show_storage_bay() function in storage bay class
        elif self.player.current_location == self.locations['east_corridor']:
            self.locations['east_corridor'].show_east_corridor() # checks if player is in east corridor and shows the show_east_corridor() function in maintenance tunnel east corridor class
        elif self.player.current_location == self.locations['docking_bay']:
            self.locations['docking_bay'].show_docking_bay() # checks if player is in docking bay and shows the show_docking_bay() function in docking bay class
        elif self.player.current_location == self.locations['cargo_section']:
            self.locations['cargo_section'].show_cargo_section() # checks if player is in cargo section and shows the show_cargo_section() function in cargo section class
        elif self.player.current_location == self.locations['console_room']:
            self.locations['console_room'].show_console_room() # checks if player is in console room and shows the show_console_room() function in console room class
        elif self.player.current_location == self.locations['supply_hub']:
            self.locations['supply_hub'].show_supply_hub() # checks if player is in supply hub and shows the show_supply_hub() function in supply hub class
        
    
        self.player.show_backpack_options() # displays the backpack options for the player which includes inventory, status, and checklist
        print("------------------------------------")

    def move_player(self, location_key): #moves the player to a certain location based on which key
        if location_key in self.locations: #checks if the location_key is valid in the dictionary self.locations
            self.player.move_to_location(self.locations[location_key]) #gets the location from the dictionary and moves the player to that location
            self.show_current_location() #displays the new location
    
    def handle_central_hub_input(self, choice): #central hub inputs
        if choice == '1':  # Go to Break Room
            self.move_player('break_room') 
        elif choice == '2': # Go to Locker Room
            self.move_player('locker_room') 
        elif choice == '3': # Go to Storage Bay
            self.move_player('storage_bay') 
        else: # status, inventory, checklist or invalid input
            self.handle_backpack_input(choice) 

    
    def handle_break_room_input(self, choice): 
        if choice == '' or choice.lower() == 'enter': 
            self.move_player('central_hub') #moves the player back to the central hub
        else: 
            self.handle_backpack_input(choice)  # status, inventory, checklist or invalid input
    
    def handle_locker_room_input(self, choice): 
        if choice == '1': # Check Locker 1 
            print("This locker is empty.") 
            press_enter() 
            self.show_current_location() #goes back to locker room scene
        elif choice == '2': # check locker 2 
            print("This locker contains old moldy boots.") 
            press_enter()
            self.show_current_location() #goes back to locker room scene
        elif choice == '3': # Check Locker 3 (has tool) 
            self.show_tool_pickup() # shows the tool pickup scene
        else: 
            self.handle_backpack_input(choice) 
    
    def handle_storage_bay_input(self, choice): 
        if choice == '' or choice.lower() == 'enter': 
            self.move_player('central_hub') #moves the player back to the central hub
        else: 
            self.handle_backpack_input(choice)  # status, inventory, checklist or invalid input

    def handle_east_corridor_input(self, choice): # handles the input for the corridor with only a west and east pathway
        if choice == '1':  #West pathway (dead end)
            clear_screen()
            print(WEST_TUNNEL_MESSAGE) #shows the west tunnel message
            press_enter()
            self.show_current_location()  # go back to pathway selections 
        elif choice == '2':  # east pathway (go to docking bay)
            self.move_player('docking_bay') # moves the player to the docking bay
        else:
            self.handle_backpack_input(choice) # status, inventory, checklist or invalid input
    
    def show_tool_pickup(self): # shows the diagnostic tool pickup scene in the locker room
        clear_screen() 
        self.locations['locker_room'].show_tool_pickup() # displays the tool pickup scene which is in the locker room class
        while True: 
            choice = input("\nEnter your choice: ").strip() 
            if choice == '1':  # Pick up the tool
                diagnostic_tool = DiagnosticTool()
                self.player.add_station_item(diagnostic_tool) #adds the diagnostic tool to the player's inventory
                self.player.add_score(10) #plus 10 points to the player's score
                print("\033[94mThis diagnostic tool seems designed to interface with maintenance droids.\033[0m") 
                print("\033[94m+ added to inventory\033[0m") 
                print(f"\033[94m+ 10 points to score \033[0m") 
                press_enter() 
                self.trigger_droid_encounter() # triggers the droid encounter
                break 
            elif choice == '2': # Leave the tool    
                print("You decide to leave the tool for now.") 
                press_enter() 
                self.trigger_droid_encounter() # triggers the droid encounter
                break 
            else: 
                print("Invalid choice. Please enter 1 or 2.") 
    
    def trigger_droid_encounter(self): 
        self.droid_encounter_triggered = True 
        self.in_droid_encounter = True
        clear_screen()
        print(self.droid.show_initial_encounter()) # shows the initial encounter with the droid in the DamagedMaintenceDroid class
        input()
        clear_screen()
        self.droid.show_blocked_message(add_hazard=True) # displays droid block message in DamagedMaintenceDroid class
        self.player.add_hazard() #adds a +1 to players hazard status in player class
        input()
        clear_screen()
        self.handle_droid_diagnostic() 
    
    def handle_return_to_locker_room(self): #getting diagnostic tool in the locker room
        clear_screen()
        print("You return to the locker room to retrieve the diagnostic tool.")
        press_enter()
        clear_screen()
        self.locations['locker_room'].show_tool_pickup() #goes back to locker room to pick up diagnostic tool
        
        while True:
            choice = input("\nEnter your choice: ").strip()
            if choice == '1': #Picks up diagnostic tool
                diagnostic_tool = DiagnosticTool() #creates a new instance for DiagnosticTool
                self.player.add_station_item(diagnostic_tool) #adds the diagnostic tool to players inventory
                print("You pick up the diagnostic tool.")
                print("+ added to inventory")
                print("(No points awarded - you should have picked this up earlier!)")
                press_enter()
                clear_screen()
                self.handle_droid_diagnostic() #droid message
                break
            elif choice == '2': #leave the diagnostic tool
                print("You need the diagnostic tool to proceed! You must pick it up.")
                press_enter()
                continue
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def show_post_repair_options(self):
        self.player.show_backpack_options()
        press_enter()
        print("------------------------------------")
        
    def handle_droid_diagnostic(self):
        has_diagnostic_tool = self.player.has_item("Diagnostic Tool")
        
        if has_diagnostic_tool: #if player has the diagnostic tool
            print(self.droid.show_diagnostic_options()) #run a diagnostic tool
            while True:
                choice = input("\nEnter your choice: ").strip()
                if choice == '1': #'yes' run the test
                    diagnostic_tool = self.player.get_station_item("Diagnostic Tool") #get diagnostic tool
                    clear_screen()
                    print(diagnostic_tool.run_diagnostic()) #runs the test
                    press_enter()
                    clear_screen()

                    while True:
                        print(diagnostic_tool.diagnostic_faults()) #detects droids faults
                        fault_choice = input("\nEnter your choice: ").strip()
                        
                        if fault_choice == '1': #fix the droid (correct choice)
                            clear_screen()
                            print(self.droid.run_diagnostic_test()) #fixed droid message
                            self.player.add_score(20) #adds 20 points to score
                            print(f"+ 20 points to score ")
                            print("\nThe path is now clear! You can continue your mission.")

                            self.droid_repaired = True 
                            self.in_droid_encounter = False
                            
                            self.show_post_repair_options() #the corridor option of 2 pathways
                            
                            while True:
                                post_choice = input("\nEnter your choice: ").strip()
                                if post_choice == '' or post_choice.lower() == 'enter':
                                    self.move_player('east_corridor') 
                                    return
                                elif post_choice.upper() in ['I', 'S', 'C']: #inventory, status, checklist
                                    self.handle_post_repair_backpack_input(post_choice)
                                else:
                                    print("Invalid choice. Press Enter to continue or use I/S/C options.")
                            
                        elif fault_choice == '2': #don't fix the droid (wrong)
                            print("Bypass failed. You must fix the motor controller first.")
                            press_enter()
                            clear_screen()
                            continue
                            
                        elif fault_choice == '3':# exit fixing  the droid (wrong)
                            print("Exiting diagnostic mode.")
                            press_enter()
                            clear_screen()
                            self.droid.show_blocked_message(add_hazard=False)
                            input()
                            clear_screen()
                            print(self.droid.show_diagnostic_options())
                            break 
                        else:
                            print("Invalid choice. Please enter 1, 2, or 3")
                            clear_screen()
                    
                    continue
                    
                elif choice == '2':  #don't run the diagnostic test
                    clear_screen()
                    self.droid.show_blocked_message(add_hazard=False) #don't add another hazard to status
                    input()
                    clear_screen()
                    print(self.droid.show_diagnostic_options()) 
                    continue
                else:
                    print("Invalid choice. Please enter 1 or 2.")
        else: #if the player tries to do the droid diagnostic without the diagnostic tool
            print(RUN_DIAGNOSTIC_OPTIONS)
            
            while True: #
                choice = input("\nEnter your choice: ").strip()
                if choice == '1': 
                    print("You don't have the diagnostic tool! You need to find it first.")
                    press_enter()
                    self.handle_return_to_locker_room() #go back to locker room to get diagnostic tool
                    break
                elif choice == '2':
                    print("Without the diagnostic tool, you cannot disable the droid.")
                    print("You return to the central hub to search for the tool.")
                    press_enter()
                    self.in_droid_encounter = False
                    self.move_player('central_hub') #go back to central to get diagnostic tool
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")

    def handle_post_repair_backpack_input(self, choice):
        if choice.upper() == 'I': #inventory
            print("\n")
            self.player.show_inventory()
            press_enter()
            clear_screen()
            self.show_post_repair_options()
        elif choice.upper() == 'S': #status
            print("\n")
            self.player.show_status()
            press_enter()
            clear_screen()
            self.show_post_repair_options()
        elif choice.upper() == 'C': #checklist
            print("\n")
            self.player.show_checklist()
            press_enter()
            clear_screen()
            self.show_post_repair_options()
    
    def handle_docking_bay_input(self, choice):
        if choice == '1':  # Go to Cargo Section
            self.move_player('cargo_section')
        elif choice == '2':  # Go to Console Room
            self.move_player('console_room')
        elif choice == '3':  # Go to Supply Hub
            self.move_player('supply_hub')
        else:
            self.handle_backpack_input(choice)
        
    def handle_cargo_section_input(self, choice):
        if choice == '1':  # Bio-Specimens crate
            clear_screen()
            print(CHOICE_1_CARGO_SECTION)
            input()
            self.show_current_location()
        elif choice == '2':  # Hazardous Tools box
            clear_screen()
            print(CHOICE_2_CARGO_SECTION)
            input()
            self.show_current_location()
        elif choice == '3':  # Research Debris container
            clear_screen()
            print(CHOICE_3_CARGO_SECTION)
            input()
            self.show_current_location()
        elif choice == '' or choice.lower() == 'enter':  # Return to docking bay
            self.move_player('docking_bay')
        else:
            self.handle_backpack_input(choice) #inventory, status, checklist

    def handle_console_room_input(self, choice):
        if choice == '1':  # Access the Logistics Terminal
            clear_screen()
            print(CHOICE_1_CONSOLE_ROOM)
            input()
            self.show_current_location() #current location of console room
        elif choice == '2':  # Check the Environmental Control Panel
            clear_screen()
            print(CHOICE_2_CONSOLE_ROOM)
            input()
            self.show_current_location() #current location of console room
        elif choice == '3':  # Use the Security Console
            clear_screen()
            print(CHOICE_3_CONSOLE_ROOM)
            input()
            self.show_current_location() #current location of console room
        elif choice == '' or choice.lower() == 'enter':  # Return to docking bay
            self.move_player('docking_bay')
        else:
            self.handle_backpack_input(choice)

    def handle_supply_hub_input(self, choice):
        if choice == '1':  # Search Shelf A1
            clear_screen()
            print(CHOICE_1_SUPPLY_HUB)
            input()
            self.show_current_location() #current location of supply hub
        elif choice == '2':  # Search Shelf A2
            clear_screen()
            print(CHOICE_2_SUPPLY_HUB)
            input()
            self.show_current_location() #current location of supply hub
        elif choice == '3':  # Search Shelf A3 (has crystal)
            self.show_crystal_pickup() #picks up the crystal
        elif choice == '' or choice.lower() == 'enter':  # Return to docking bay
            # Check if crystal was encountered but not picked up
            if self.crystal_encountered and not self.player.has_item("Energy Crystal"):
                self.show_cannot_continue_message() #you must pick up the crystal or you cant continue
            else:
                self.move_player('docking_bay') #moves player to the docking bay
        else:
            self.handle_backpack_input(choice) # inventory, status, checklist
    
    def show_cannot_continue_message(self):
        clear_screen()
        print("You cannot continue without the crystal.")
        print("You must return to Shelf A3 and pick up the Energy Crystal to complete your mission.")
        press_enter()
        self.show_current_location() #current location is supply hub
    
    def show_crystal_pickup(self):
        clear_screen()
        self.crystal_encountered = True 

        if self.crystal_left_behind:
            self.show_crystal_return_pickup()
        else:
            self.show_crystal_first_pickup()
    
    def show_crystal_first_pickup(self):
        self.locations['supply_hub'].show_crystal_pickup()
        while True:
            choice = input("\nEnter your choice: ").strip()
            if choice == '1':
                clear_screen()
                energy_crystal = EnergyCrystal()
                self.player.add_station_item(energy_crystal) #adds crystal in players inventory
                self.player.add_score(50) # adds 50 points in players score
                print(POINTS_REWARD_CRYSTAL)
                print("------------------------------------")
                self.player.show_backpack_options() #inventory, status, checklist
                press_enter()
                print("------------------------------------")

                while True:
                    post_choice = input("\nEnter your choice: ").strip()
                    if post_choice == '' or post_choice.lower() == 'enter':
                        self.show_win_prompt() 
                        return
                    elif post_choice.upper() in ['I', 'S', 'C']:
                        self.handle_post_crystal_backpack_input(post_choice)  #inventory, status, checklist
                    else:
                        print("Invalid choice. Please try again.")
                break
            elif choice == '2':
                self.crystal_left_behind = True  
                print("You decide to leave the crystal for now.")
                press_enter()
                self.show_current_location() #supply bay is current location
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def show_crystal_return_pickup(self):
        print(CRYSTAL_PICKUP_MESSAGE)
        
        while True:
            choice = input("\nEnter your choice: ").strip()
            if choice == '1':  
                clear_screen()
                energy_crystal = EnergyCrystal()
                self.player.add_station_item(energy_crystal) #adds energy crystal into the inventory
                print(NO_POINTS_REWARD_CRYSTAL)
                print("------------------------------------")
                self.player.show_backpack_options() # inventory, status, checklist
                print("------------------------------------")

                while True:
                    post_choice = input("\nEnter your choice: ").strip()
                    if post_choice == '' or post_choice.lower() == 'enter':
                        self.show_win_prompt() #asks if you won
                        return
                    elif post_choice.upper() in ['I', 'S', 'C']: # inventory, status, checklist
                        self.handle_post_crystal_no_points_backpack_input(post_choice) 
                    else:
                        print("Invalid choice. Please try again.")
                break
            elif choice == '2':
                print("You cannot continue without the crystal.")
                press_enter()
                continue
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def handle_post_crystal_backpack_input(self, choice):
        if choice.upper() == 'I':  # Inventory
            print("\n")
            self.player.show_inventory()
            press_enter()
            clear_screen()
            print(POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()
            press_enter()
        elif choice.upper() == 'S':  # Status
            print("\n")
            self.player.show_status()
            press_enter()
            clear_screen()
            print(POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()
            press_enter()
        elif choice.upper() == 'C':  # Checklist
            print("\n")
            self.player.show_checklist()
            press_enter()
            clear_screen()
            print(POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()
            press_enter()

    def handle_post_crystal_no_points_backpack_input(self, choice):
        if choice.upper() == 'I':  # Inventory
            print("\n")
            self.player.show_inventory()
            press_enter()
            clear_screen()
            print(NO_POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()
            press_enter()
        elif choice.upper() == 'S':  # Status
            print("\n")
            self.player.show_status()
            press_enter()
            clear_screen()
            print(NO_POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()
            press_enter()
        elif choice.upper() == 'C':  # Checklist
            print("\n")
            self.player.show_checklist()
            press_enter()
            clear_screen()
            print(NO_POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()
            press_enter()

    def show_win_prompt(self):
        clear_screen()
        print(TYPE_WIN_DOCKING_BAY)
        self.player.show_backpack_options()

    def show_win_prompt_without_crystal(self):
        clear_screen()
        print(COMPLETED_GAME_MESSAGE)
        self.player.show_backpack_options()

    def handle_backpack_input(self, choice): 
        if choice.upper() == 'I': # Inventory 
            print("\n") 
            self.player.show_inventory() 
            press_enter() 
            if self.in_droid_encounter:
                clear_screen()
                self.handle_droid_diagnostic()
            else:
                self.show_current_location() 
        elif choice.upper() == 'S': # Status 
            print("\n") 
            self.player.show_status() 
            press_enter() 
            if self.in_droid_encounter:
                clear_screen()
                self.handle_droid_diagnostic()
            else:
                self.show_current_location() 
        elif choice.upper() == 'C': # Checklist 
            print("\n") 
            self.player.show_checklist() 
            press_enter() 
            if self.in_droid_encounter:
                clear_screen()
                self.handle_droid_diagnostic()
            else:
                self.show_current_location() 
        else: 
            if not self.in_droid_encounter:
                print("Invalid choice. Please try again.") 
                press_enter() 
                self.show_current_location() 
    
    def game_loop(self): 
        while True: 
            try: 
                choice = input("\nEnter your choice: ").strip() 
                if choice.lower() == 'win':
                    if (self.player.has_item("Diagnostic Tool") and  #checks if player has diagnostic tool and energy crystal
                        self.player.has_item("Energy Crystal") and 
                        (self.player.current_location == self.locations['docking_bay'] or #checks if player is in a valid location
                         self.player.current_location == self.locations['supply_hub'] or
                         self.player.current_location == self.locations['cargo_section'] or
                         self.player.current_location == self.locations['console_room'])):
                        self.player.add_score(30) #{+30 points to players score}
                        clear_screen()
                        if self.player.score == 110: #if players score is 110 means they won
                            print(f"Well done {self.player.name}, Mission Complete.")
                            print("YOU HAVE WON!")
                            print(f"Points Scored: {self.player.score}/110")
                            print(f"Hazards Encountered: {self.player.hazards}/1")
                            print("Thank you for restoring the Celestial Outpost.")
                        else: #anything less than the score = 110, means the player lost
                            print(f"Mission Failed, {self.player.name}.")
                            print("The Celestial Outpost remains lost.")
                            print("YOU HAVE LOST.")
                            print(f"Points Scored: {self.player.score}/110")
                            print(f"Hazards Encountered: {self.player.hazards}/1")
                            print("Despite your efforts, the station has succumbed to the unknown.")
                            print("Better luck next time, Specialist.")
                        break
                    else:
                        missing_items = [] #creates a list that states to the player what objectives are incomplete
                        if not self.player.has_item("Diagnostic Tool"):
                            missing_items.append("- Find the diagnostic tool")
                        if not self.player.has_item("Energy Crystal"):
                            missing_items.append("- Find the energy crystal")
                        
                        print("You haven't completed all objectives yet!")
                        if missing_items:
                            print("Still needed:")
                            for item in missing_items:
                                print(item) #prints the list of objectives that are incomplete
                        press_enter()
                        self.show_current_location() #shows current location
                        continue
                
                if self.in_droid_encounter: 
                    if choice.upper() in ['I', 'S', 'C']: # inventory, status and checklist
                        self.handle_backpack_input(choice)
                    else:
                        self.handle_droid_diagnostic()
                elif self.player.current_location == self.locations['central_hub']: # if not in droid enncounter, inputs are interpreted correctly depending on where the player is
                    self.handle_central_hub_input(choice) 
                elif self.player.current_location == self.locations['break_room']: 
                    self.handle_break_room_input(choice) 
                elif self.player.current_location == self.locations['locker_room']: 
                    self.handle_locker_room_input(choice) 
                elif self.player.current_location == self.locations['storage_bay']: 
                    self.handle_storage_bay_input(choice)
                elif self.player.current_location == self.locations['east_corridor']:
                    self.handle_east_corridor_input(choice)
                elif self.player.current_location == self.locations['docking_bay']:
                    self.handle_docking_bay_input(choice)
                elif self.player.current_location == self.locations['cargo_section']:
                    self.handle_cargo_section_input(choice)
                elif self.player.current_location == self.locations['console_room']:
                    self.handle_console_room_input(choice)
                elif self.player.current_location == self.locations['supply_hub']:
                    self.handle_supply_hub_input(choice)
                else:
                    print("Invalid choice. Please try again.") 
                    press_enter() 
                    self.show_current_location() #displays the current location
                    
            except KeyboardInterrupt: # if the player presses Ctrl + C
                print("\n\nGame interrupted. Goodbye!")
                break #exits the game
            except Exception as e: #if an error occurs
                print(f"An error occurred: {e}") #shows the error that occurred
                press_enter() 
                if not self.in_droid_encounter:
                    self.show_current_location()



