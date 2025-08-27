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

def clear_screen() -> None: 
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear') 

def press_enter() -> None: 
    """Prompts the player to press Enter to continue."""
    input("\033[3mEnter: Continue\033[0m") 

class GameIntroduction: 
    """Handles the game introduction and player name input."""
    def __init__(self, player=None) -> None: 
        self.player = None  # Player instance will be set later, once player enters their name.
    
    def show_intro(self) -> None:
        """Shows the introduction message and prompts for player name."""
        clear_screen() 
        print("\033[0m" + WELCOME_MESSAGE)
        
        while True:  # Loop until valid name entered.
            player_name = input("\033[3mEnter your name, Specialist: \033[0m").strip()

            if player_name: 
                break 
            print("Name cannot be empty. Please try again.") 

        self.player = Player(player_name.capitalize())  # Create a new Player instance with the entered name.
        clear_screen() 
        print(GAME_MESSAGE.format(player_name=self.player.name))  # Using the player's name for the game message (constant).

class RPGGameRun:
    """Main class to run the RPG game."""
    def __init__(self): 
        self.player = None  # Player instance will be set after the introduction.
        self.droid = DamagedMaintenanceDroid()  # Creates the maintenance droid encounter
        self.droid_encounter_triggered = False  # Checks if the droid encounter has been triggered.
        self.in_droid_encounter = False  # Checks if the player is currently in a droid encounter.
        self.droid_repaired = False  # Checks if the droid has been repaired.
        self.crystal_encountered = False  # Checks if the crystal has been found.
        self.crystal_left_behind = False  # Checks if the crystal was left behind.
        self.tool_picked_up_before_droid = False  # Checks if the diagnostic tool was picked up before the droid encounter.
        self.hazard_added = False  # Checks if a hazard has been added during the droid encounter, ensuring it only happens once.
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
        }  # Dictionary containing all the locations in the game.
    
    def start_game(self):
        """Starts the RPG game by showing the introduction and setting up the player."""
        game_intro = GameIntroduction()  # Creates a new instance for GameIntroduction.
        game_intro.show_intro()  # Shows the introduction message and prompts for player name.
        self.player = game_intro.player  # Player name is set as self.player in RPGGameRun class.
        self.player.move_to_location(self.locations['central_hub'])  # Moves player to the central hub.
        press_enter() 
        self.show_current_location()  # Displays the current location of the player, in this case, the central hub.
        self.game_loop()  # Begins the main loop of the game.
    
    def show_current_location(self):
        """Displays the current location of the player and its description."""
        clear_screen() 
        if self.player.current_location == self.locations['central_hub']: 
            self.locations['central_hub'].show_central_hub()  # Checks if player is in central hub and shows the show_central_hub() function in maintenance tunnel class.

        elif self.player.current_location == self.locations['break_room']: 
            self.locations['break_room'].show_break_room()  # Checks if player is in break room and shows the show_break_room() function in break room class.

        elif self.player.current_location == self.locations['locker_room']: 
            self.locations['locker_room'].show_locker_room()  # Checks if player is in locker room and shows the show_locker_room() function in locker room class.

        elif self.player.current_location == self.locations['storage_bay']: 
            self.locations['storage_bay'].show_storage_bay()  # Checks if player is in storage bay and shows the show_storage_bay() function in storage bay class.

        elif self.player.current_location == self.locations['east_corridor']:
            self.locations['east_corridor'].show_east_corridor()  # Checks if player is in east corridor and shows the show_east_corridor() function in maintenance tunnel east corridor class.

        elif self.player.current_location == self.locations['docking_bay']:
            self.locations['docking_bay'].show_docking_bay()  # Checks if player is in docking bay and shows the show_docking_bay() function in docking bay class.

        elif self.player.current_location == self.locations['cargo_section']:
            self.locations['cargo_section'].show_cargo_section()  # Checks if player is in cargo section and shows the show_cargo_section() function in cargo section class.

        elif self.player.current_location == self.locations['console_room']:
            self.locations['console_room'].show_console_room()  # Checks if player is in console room and shows the show_console_room() function in console room class.

        elif self.player.current_location == self.locations['supply_hub']:
            self.locations['supply_hub'].show_supply_hub()  # Checks if player is in supply hub and shows the show_supply_hub() function in supply hub class.

        self.player.show_backpack_options() # Displays the backpack options for the player which includes inventory, status, and checklist.
        print("------------------------------------")

    def move_player(self, location_key):
        """Checks if the location_key is valid in the dictionary self.locations"""
        if location_key in self.locations:
            self.player.move_to_location(self.locations[location_key])  # Gets the location from the dictionary and moves the player to that location
            self.show_current_location()  # Displays the new location.
    
    def handle_central_hub_input(self, choice):
        """Handles the input when player is in the central hub location."""
        if choice == '1':  # Go to Break Room.
            self.move_player('break_room')

        elif choice == '2':  # Go to Locker Room.
            self.move_player('locker_room')

        elif choice == '3':  # Go to Storage Bay.
            self.move_player('storage_bay')

        else:  # Player chooses either status, inventory, checklist or invalid input.
            self.handle_backpack_input(choice) 

    
    def handle_break_room_input(self, choice): 
        """Handles the input when player is in the break room location."""
        if choice == '' or choice.lower() == 'enter': 
            self.move_player('central_hub')  # Moves the player back to the central hub.

        else:  # Player chooses either status, inventory, checklist or invalid input.
            self.handle_backpack_input(choice) 
    
    def handle_locker_room_input(self, choice): 
        """Handles the input when player is in the locker room location."""
        if choice == '1':  # Player checks Locker 1.
            print("This locker is empty.") 
            press_enter() 
            self.show_current_location()  # Displays the current location of the player, in this case, the locker room.

        elif choice == '2':  # Player checks Locker 2.
            print("This locker contains old moldy boots.") 
            press_enter()
            self.show_current_location()  # Displays the current location of the player, in this case, the locker room.

        elif choice == '3':  # Player checks Locker 3.
            self.show_tool_pickup()  # Shows the tool pickup scene in the locker room.

        else:  # Player chooses either status, inventory, checklist or invalid input.
            self.handle_backpack_input(choice) 
    
    def handle_storage_bay_input(self, choice):
        """Handles the input when player is in the storage bay location."""
        if choice == '' or choice.lower() == 'enter': 
            self.move_player('central_hub')  # Moves the player back to the central hub.

        else:  # Player chooses either status, inventory, checklist or invalid input. 
            self.handle_backpack_input(choice)

    def handle_east_corridor_input(self, choice):
        """Handles the input when player is in the maintenance tunnel corridor location."""
        if choice == '1' :  # Displays West pathway message and then goes back to maintenance tunnel (path selection).
            clear_screen()
            print(WEST_TUNNEL_MESSAGE)
            press_enter()
            self.show_current_location()

        elif choice == '2':  # Player goes through the east pathway that leads to the go to docking bay.
            self.move_player('docking_bay')

        else:  # Player chooses either status, inventory, checklist or invalid input. 
            self.handle_backpack_input(choice)
        
    def show_tool_pickup(self):
        """Shows the tool pickup scene in the locker room and handles the player's choice."""
        clear_screen() 
        self.locations['locker_room'].show_tool_pickup()  # Displays the tool pickup scene which is in the locker room class.
        
        while True:  # Loop until valid choice is made.
            choice = input("\nEnter your choice: ").strip() 
            
            if choice == '1':  # Player picks up the tool.
                diagnostic_tool = DiagnosticTool()  # Creates a new instance of the DiagnosticTool class.
                clear_screen()
                self.player.add_station_item(diagnostic_tool)  # Adds the diagnostic tool to the player's inventory.
                
                if not self.droid_encounter_triggered:  # Player only gets points if they pick up the tool before the droid encounter.
                    self.player.add_score(10)  # Adds 10 points to the player's score.
                    self.tool_picked_up_before_droid = True
                    print("\033[95mThis diagnostic tool seems designed to interface with maintenance droids.\033[0m") 
                    print("\033[95m+ added to inventory\033[0m") 
                    print(f"\033[95m+ 10 points to score \033[0m") 

                else:  # No points if picked up after droid encounter already started.
                    print("\033[95mThis diagnostic tool seems designed to interface with maintenance droids.\033[0m") 
                    print("\033[95m+ added to inventory\033[0m") 
                    print(f"\033[95m(No points awarded - you should have picked this up earlier!)\033[0m") 
                
                print("-------------------------------------")
                press_enter() 
                self.trigger_droid_encounter()  # Triggers the droid encounter after picking up the tool.
                break

            elif choice == '2':  # Leave the tool.    
                print("You decide to leave the tool for now.") 
                press_enter() 
                self.trigger_droid_encounter()  # Triggers the droid encounter even if tool is left behind.
                break

            else: # Invalid input chosen.
                print("Invalid choice. Please enter 1 or 2.")
                press_enter() 
                clear_screen()
                self.show_tool_pickup()  # Displays the tool pickup scene again.


    def trigger_droid_encounter(self):
        """Triggers the droid encounter if it hasn't been triggered yet."""
        self.droid_encounter_triggered = True  # Sets the droid encounter as triggered.
        self.in_droid_encounter = True  # Sets the player in a currently in droid encounter state.
        clear_screen()
        print(self.droid.show_initial_encounter())  # Shows the initial encounter with the droid in the DamagedMaintenceDroid class.
        input()
        clear_screen()

        if not self.hazard_added:
            self.player.add_hazard()  # Adds a hazard to the player score.
            self.hazard_added = True  # Sets the hazard added state to True to prevent multiple hazards from being added.
        
        self.droid.show_blocked_message(add_hazard=False) # Shows the message that the droid is blocking the way without adding another hazard.
        input()
        clear_screen()
        self.handle_droid_diagnostic()  

    def handle_droid_diagnostic(self):
        """Handles the damaged maintence droid and repair sequence."""
        has_diagnostic_tool = self.player.has_item("Diagnostic Tool")  # Checks if the player has the diagnostic tool in their inventory.
        
        if has_diagnostic_tool:
            print(self.droid.show_diagnostic_options())  # Displays the diagnostic options within the DamagedMaintenanceDroid class.
            
            while True:
                choice = input("\nEnter your choice: ").strip()
                
                if choice == '1':  # Runs the diagnostic test.
                    diagnostic_tool = self.player.get_station_item("Diagnostic Tool")  # Get diagnostic tool from inventory
                    clear_screen()
                    print(BACKPACK_OPTIONS)
                    clear_screen()

                    while True:
                        print(diagnostic_tool.diagnostic_faults())
                        fault_choice = input("\nEnter your choice: ").strip()
                        
                        if fault_choice == '1':  # Attempt to reboot motor controller.
                            clear_screen()
                            print(self.droid.run_diagnostic_test())
                            self.player.add_score(20)  # Adds 20 points to player's score.
                            print(f"\033[95m+ 20 points to score\033[0m")
                            print("\nThe path is now clear! You can continue your mission.")
                            self.droid_repaired = True  # Sets the droid repaired state to True.
                            self.in_droid_encounter = False  # Player is no longer in a droid encounter.
                            print(BACKPACK_OPTIONS)
                            
                            while True:  # Handles post-repair options of choosing which corridoor option.
                                post_choice = input("\nEnter your choice: ").strip()
                                
                                if post_choice == '' or post_choice.lower() == 'enter':
                                    self.move_player('east_corridor') 
                                    return
                                
                                elif post_choice.upper() in ['I', 'S', 'C']:  # Player chooses either status, inventory, checklist
                                    self.handle_post_repair_backpack_input(post_choice) 
                                
                                else:  # Invalid input chosen.
                                    print("Invalid choice. Press Enter to continue or use I/S/C options.")
                            
                        elif fault_choice == '2':  # Bypassing sensor loop, without fixing the motor.
                            print("Bypass failed. You must fix the motor controller first.")
                            press_enter()
                            clear_screen()
                            continue
                            
                        elif fault_choice == '3': # Exit diagnostic test.
                            print("Exiting diagnostic mode.")
                            press_enter()
                            clear_screen()
                            self.droid.show_blocked_message(add_hazard=False)  # Ensure the droid is still blocking the way and hazard isn't added again.
                            input()
                            clear_screen()
                            print(self.droid.show_diagnostic_options())
                            break 
                        
                        else:  # Invalid input chosen.
                            print("Invalid choice. Please enter 1, 2, or 3")
                            clear_screen()
                    
                    continue
                    
                elif choice == '2':  # Player chooses not to run the diagnostic test.
                    clear_screen()
                    self.droid.show_blocked_message(add_hazard=False)  # Ensure the droid is still blocking the way and hazard isn't added again.
                    input()
                    clear_screen()
                    print(self.droid.show_diagnostic_options()) 
                    continue
                
                else:  # Invalid input chosen.
                    print("Invalid choice. Please enter 1 or 2.")
        
        else:  # If the player tries to do the droid diagnostic without the diagnostic tool.
            print(RUN_DIAGNOSTIC_OPTIONS)
            
            while True:
                choice = input("\nEnter your choice: ").strip()

                if choice == '1':  # Runs the diagnostic test, however player does not have diagnostic tool in the inventory.
                    print("You don't have the diagnostic tool! You need to find it first.")
                    press_enter()
                    self.handle_return_to_locker_room()
                    break

                elif choice == '2':  # Player chooses not to run the diagnostic test, however player does not have diagnostic tool in the inventory.
                    print("Without the diagnostic tool, you cannot disable the droid.")
                    print("You return to the central hub to search for the tool.")
                    press_enter()
                    self.handle_return_to_locker_room()
                    break

                else:  # Invalid input chosen.
                    print("Invalid choice. Please enter 1 or 2.")

    def handle_return_to_locker_room(self):
        """Sends player to return back to the locker room to attain diagnostic tool."""
        self.in_droid_encounter = False  # Player is no longer in a droid encounter.
        self.move_player('locker_room')  # Player returns to the locker room to pick up the diagnostic tool.
                
    def handle_post_repair_backpack_input(self, choice):
        """Handle backpack options inventory, status, checklist after droid repair."""
        if choice.upper() == 'I':  # Displays the player's inventory.
            print("\n")
            self.player.show_inventory()
            press_enter()
            clear_screen()
            print(BACKPACK_OPTIONS)

        elif choice.upper() == 'S':  # Displays the player's status.
            print("\n")
            self.player.show_status()
            press_enter()
            clear_screen()
            print(BACKPACK_OPTIONS)

        elif choice.upper() == 'C':  # Displays the player's checklist.
            print("\n")
            self.player.show_checklist()
            press_enter()
            clear_screen()
            print(BACKPACK_OPTIONS)
    
    def handle_docking_bay_input(self, choice):
        if choice == '1':  # Player moves to the cargo section.
            self.move_player('cargo_section')

        elif choice == '2':  # Player moves to the console room.
            self.move_player('console_room')

        elif choice == '3':  # Player moves to the supply hub.
            self.move_player('supply_hub')

        else:  # Player chooses either status, inventory, checklist or invalid input. 
            self.handle_backpack_input(choice)
        
    def handle_cargo_section_input(self, choice):
        """Handles the input when player is in the cargo section location."""
        if choice == '1':  # Player checks the Bio-Specimens crate.
            clear_screen()
            print(CHOICE_1_CARGO_SECTION)
            input()
            self.show_current_location()

        elif choice == '2':  # Player checks the Hazardous Tools box.
            clear_screen()
            print(CHOICE_2_CARGO_SECTION)
            input()
            self.show_current_location()

        elif choice == '3':  # Player checks the Research Debris container.
            clear_screen()
            print(CHOICE_3_CARGO_SECTION)
            input()
            self.show_current_location()

        elif choice == '' or choice.lower() == 'enter':  # Player returns to docking bay.
            self.move_player('docking_bay')

        else:  # Player chooses either status, inventory, checklist or invalid input.
            self.handle_backpack_input(choice)

    def handle_console_room_input(self, choice):
        '""Handles the input when player is in the console room location."""'
        if choice == '1':  # Player accesses the Logistics Terminal.
            clear_screen()
            print(CHOICE_1_CONSOLE_ROOM)
            input()
            self.show_current_location()

        elif choice == '2':  # Player checks the Environmental Control Panel.
            clear_screen()
            print(CHOICE_2_CONSOLE_ROOM)
            input()
            self.show_current_location()

        elif choice == '3':  # Player uses the Security Console.
            clear_screen()
            print(CHOICE_3_CONSOLE_ROOM)
            input()
            self.show_current_location()

        elif choice == '' or choice.lower() == 'enter':  # Player returns to docking bay.
            self.move_player('docking_bay')

        else:  # Player chooses either status, inventory, checklist or invalid input.
            self.handle_backpack_input(choice)

    def handle_supply_hub_input(self, choice):
        """Handles the input when player is in the supply hub location."""
        if choice == '1':  # Player searches Shelf A1.
            clear_screen()
            print(CHOICE_1_SUPPLY_HUB)
            input()
            self.show_current_location() 

        elif choice == '2':  # Player searches Shelf A2.
            clear_screen()
            print(CHOICE_2_SUPPLY_HUB)
            input()
            self.show_current_location()

        elif choice == '3':  # Player searches Shelf A3.
            self.show_crystal_pickup()  # Shows the crystal pickup scene in the supply hub.
            print("-------------------------------------")

        elif choice == '' or choice.lower() == 'enter':  # Player returns to docking bay.
            
            if self.crystal_encountered and not self.player.has_item("Energy Crystal"):  # Checks if crystal was encountered however not picked up.
                self.show_cannot_continue_message()  # Shows the message that the player cannot continue without the crystal.
            
            else:
                self.move_player('docking_bay')
        
        else:  # Player chooses either status, inventory, checklist or invalid input.
            self.handle_backpack_input(choice)
    
    def show_crystal_pickup(self):
        """Display energy crystal pickup sequence."""
        clear_screen()
        self.crystal_encountered = True  # Sets the crystal encountered state to True.

        if self.crystal_left_behind:  # If the crystal was left behind, show the return pickup sequence.
            self.show_crystal_return_pickup()

        else:
            self.show_crystal_first_pickup()  # If crystal was picked up the first try, shows the first pickup sequence for the crystal.
    
    def show_crystal_first_pickup(self):
        """Display the energy crystal pickup sequence, when the crystal was picked up the first try."""
        self.locations['supply_hub'].show_crystal_pickup()
        while True:
            choice = input("\nEnter your choice: ").strip()

            if choice == '1':  # Picks up the crystal.
                clear_screen()
                energy_crystal = EnergyCrystal()
                self.player.add_station_item(energy_crystal)  # Adds the energy crystal into the player's inventory.
                self.player.add_score(50)  # Adds 50 points to the player's score.
                print(POINTS_REWARD_CRYSTAL)
                print(BACKPACK_OPTIONS)
                print("------------------------------------")

                while True:
                    post_choice = input("\nEnter your choice: ").strip()

                    if post_choice == '' or post_choice.lower() == 'enter':
                        self.show_win_prompt()
                        return

                    elif post_choice.upper() in ['I', 'S', 'C']:  # Player chooses either status, inventory, checklist or invalid input.
                        self.handle_post_crystal_backpack_input(post_choice)

                    else:  # Invalid input chosen.
                        print("Invalid choice. Please try again.")
                break

            elif choice == '2':  # Player leaves the crystal behind.
                self.crystal_left_behind = True  
                print("To continue with the mission, you must pick up the crystal.")
                print("You cannot proceed without the Energy Crystal.")
                press_enter()
                self.show_crystal_return_pickup()  # Displays the crystal return pickup sequence.
                break

            else:  # Invalid input chosen.
                print("Invalid choice. Please enter 1 or 2.")
                press_enter()
                clear_screen()
                self.show_crystal_first_pickup()  # Displays the crystal pickup sequence again until valid input is given.
        
    def show_cannot_continue_message(self):
        """Displays a message displaying that the player cannot continue without the crystal."""
        clear_screen()
        print("To continue with the mission, you must pick up the crystal.")
        print("You cannot proceed without the Energy Crystal.")
        print("You must return to Shelf A3 and pick up the Energy Crystal to complete your mission.")
        press_enter()
        self.show_current_location()
    
    def show_crystal_return_pickup(self):
        """Displays the energy crystal return pickup sequence, when the crystal was left behind."""
        clear_screen()
        print("The Energy Crystal is still here, glowing softly.")
        print("You need this crystal to complete your mission.")
        print("-------------------------------------")
        print("\n\033[34m1. Pick up the Energy Crystal\033[0m")
        print("\n\033[34m2. Leave the crystal\033[0m")
        
        while True:
            choice = input("\nEnter your choice: ").strip()

            if choice == '1':  
                clear_screen()
                energy_crystal = EnergyCrystal()
                self.player.add_station_item(energy_crystal)  # Adds the energy crystal into the player's inventory.
                self.crystal_left_behind = False   # Sets the crystal left behind state to False.
                print(NO_POINTS_REWARD_CRYSTAL)
                print(BACKPACK_OPTIONS)
                print("------------------------------------")

                while True:
                    post_choice = input("\nEnter your choice: ").strip()

                    if post_choice == '' or post_choice.lower() == 'enter':
                        self.show_win_prompt()
                        return

                    elif post_choice.upper() in ['I', 'S', 'C']:  # Player chooses either status, inventory, checklist.
                        self.handle_post_crystal_no_points_backpack_input(post_choice)

                    else:
                        print("Invalid choice. Please try again.")
                break

            elif choice == '2':  # Player leaves the crystal behind.
                print("To continue with the mission, you must pick up the crystal.")
                print("You cannot proceed without the Energy Crystal.")
                press_enter()
                clear_screen()
                self.show_crystal_return_pickup()  # Keep showing until they pick it up

            else:  # Invalid input chosen.
                print("Invalid choice. Please enter 1 or 2.")
                press_enter()
                clear_screen()
                self.show_crystal_return_pickup()
                        
    def handle_post_crystal_backpack_input(self, choice):
        """Handle backpack options inventory, status, checklist after crystal pickup."""
        if choice.upper() == 'I':  # Displays players inventory
            print("\n")
            self.player.show_inventory()
            press_enter()
            clear_screen()
            print(POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()

        elif choice.upper() == 'S':  # Displays players status
            print("\n")
            self.player.show_status()
            press_enter()
            clear_screen()
            print(POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()

        elif choice.upper() == 'C':  # Displays players checklist
            print("\n")
            self.player.show_checklist()
            press_enter()
            clear_screen()
            print(POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()

    def handle_post_crystal_no_points_backpack_input(self, choice):
        """Handle backpack options inventory, status, checklist after crystal pickup without points."""
        if choice.upper() == 'I':   # Displays players inventory
            print("\n")
            self.player.show_inventory()
            press_enter()
            clear_screen()
            print(NO_POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()

        elif choice.upper() == 'S':  # Displays players status
            print("\n")
            self.player.show_status()
            press_enter()
            clear_screen()
            print(NO_POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()

        elif choice.upper() == 'C':  # Displays players checklist
            print("\n")
            self.player.show_checklist()
            press_enter()
            clear_screen()
            print(NO_POINTS_REWARD_CRYSTAL)
            self.player.show_backpack_options()

    def show_win_prompt(self):
        """Displays the win prompt when the player has completed all objectives."""
        clear_screen()
        print(TYPE_WIN_DOCKING_BAY)
        self.player.show_backpack_options()
        
        while True:
            choice = input("\nEnter your choice: ").strip()
            if choice.lower() == 'win':

                if (self.player.has_item("Diagnostic Tool") and 
                    self.player.has_item("Energy Crystal")):
                    self.player.add_score(30)
                    clear_screen()

                    if self.player.score == 110:  # If the player's score is 110, they have won.
                        print(f"Well done {self.player.name}, Mission Complete.")
                        print("YOU HAVE WON!")
                        print(f"Points Scored: {self.player.score}/110")
                        print(f"Hazards Encountered: {self.player.hazards}/1")
                        print("Thank you for restoring the Celestial Outpost.")

                    else:  # If the player's score is less than 110, they have lost.
                        print(f"Mission Failed, {self.player.name}.")
                        print("The Celestial Outpost remains lost.")
                        print("YOU HAVE LOST.")
                        print(f"Points Scored: {self.player.score}/110")
                        print(f"Hazards Encountered: {self.player.hazards}/1")
                        print("Despite your efforts, the station has succumbed to the unknown.")
                        print("Better luck next time, Specialist.")
                    
                    print("\nPress Enter to exit...")
                    input()
                    os._exit(0)  # Forceful exit to ensure the game ends.

                else:  # If the player has not completed all objectives.
                    missing_items = []  # Creates a list that states to the player what objectives are incomplete.

                    if not self.player.has_item("Diagnostic Tool"):  # Checks if player has diagnostic tool.
                        missing_items.append("- Find the diagnostic tool")  # Adds diagnostic tool to the missing items list.

                    if not self.player.has_item("Energy Crystal"):  # Checks if player has energy crystal.
                        missing_items.append("- Find the energy crystal")  # Adds energy crystal to the missing items list.
                    print("You haven't completed all objectives yet!")

                    if missing_items:
                        print("Still needed:")

                        for item in missing_items:  # Prints the list of objectives that are incomplete.
                            print(item)

                    press_enter()
                    clear_screen()
                    print(TYPE_WIN_DOCKING_BAY)
                    self.player.show_backpack_options()
                    continue

            elif choice.upper() in ['I', 'S', 'C']:  # Player chooses either status, inventory, checklist.
                if choice.upper() == 'I':
                    print("\n")
                    self.player.show_inventory()
                    press_enter()
                    clear_screen()
                    print(TYPE_WIN_DOCKING_BAY)
                    self.player.show_backpack_options()

                elif choice.upper() == 'S':
                    print("\n")
                    self.player.show_status()
                    press_enter()
                    clear_screen()
                    print(TYPE_WIN_DOCKING_BAY)
                    self.player.show_backpack_options()

                elif choice.upper() == 'C':
                    print("\n")
                    self.player.show_checklist()
                    press_enter()
                    clear_screen()
                    print(TYPE_WIN_DOCKING_BAY)
                    self.player.show_backpack_options()

            else:  # Invalid input chosen.
                print("Invalid choice. Type 'win' to complete your mission, or use I/S/C for backpack options.")
                press_enter()
                clear_screen()
                print(TYPE_WIN_DOCKING_BAY)
                self.player.show_backpack_options()

    def show_win_prompt_without_crystal(self):
        """Displays the win prompt when the player has completed all objectives without the crystal."""
        clear_screen()
        print(COMPLETED_GAME_MESSAGE)
        self.player.show_backpack_options()

    def handle_backpack_input(self, choice): 
        """Handles the player's input for inventory, status, and checklist options."""
        if choice.upper() == 'I':  # Displays the player's inventory.
            print("\n") 
            self.player.show_inventory() 
            press_enter() 
            if self.in_droid_encounter:
                clear_screen()
                self.handle_droid_diagnostic()
            else:
                self.show_current_location()

        elif choice.upper() == 'S':  # Displays the player's status.
            print("\n") 
            self.player.show_status() 
            press_enter() 
            if self.in_droid_encounter:
                clear_screen()
                self.handle_droid_diagnostic()
            else:
                self.show_current_location() 

        elif choice.upper() == 'C':  # Displays the player's checklist.
            print("\n") 
            self.player.show_checklist() 
            press_enter() 
            if self.in_droid_encounter:
                clear_screen()
                self.handle_droid_diagnostic()
            else:
                self.show_current_location()

        else:  # Invalid input chosen.
            if not self.in_droid_encounter:
                print("Invalid choice. Please try again.") 
                press_enter() 
                self.show_current_location()
    
    def game_loop(self):
        """Main game loop that handles player input and game progression."""
        while True: 
            try: 
                choice = input("\nEnter your choice: ").strip()

                if choice.lower() == 'win':  # Checks if player typed 'win' to complete the mission.

                    if (self.player.has_item("Diagnostic Tool") and  # Checks if player has diagnostic tool and energy crystal.
                        self.player.has_item("Energy Crystal") and 
                        (self.player.current_location == self.locations['docking_bay'] or  # Checks if player is in a valid location.
                        self.player.current_location == self.locations['supply_hub'] or
                        self.player.current_location == self.locations['cargo_section'] or
                        self.player.current_location == self.locations['console_room'])):
                        self.player.add_score(30)  # Adds 30 points to the player's score.
                        clear_screen()

                        if self.player.score == 110:  # If the player's score is 110, they have won.
                            print(f"\033[94mWell done {self.player.name}, Mission Complete.\033[0m")
                            print("\033[94mYOU HAVE WON!\033[0m")
                            print(f"\033[94mPoints Scored: {self.player.score}/110\033[0m")
                            print(f"\033[94mHazards Encountered: {self.player.hazards}/1\033[0m")
                            print("\033[94mThank you for restoring the Celestial Outpost.\033[0m")

                        else:  # If the player's score is less than 110, they have lost.
                            print(f"\033[94mMission Failed, {self.player.name}.\033[0m")
                            print("\033[94mThe Celestial Outpost remains lost.\033[0m")
                            print("\033[94mYOU HAVE LOST.\033[0m")
                            print(f"\033[94mPoints Scored: {self.player.score}/110\033[0m")
                            print(f"\033[94mHazards Encountered: {self.player.hazards}/1\033[0m")
                            print("\033[94mDespite your efforts, the station has succumbed to the unknown.\033[0m")
                            print("\033[94mBetter luck next time, Specialist.\033[0m")
                            
                        print("\nPress Enter to exit...")
                        input()
                        os._exit(0)  # Forceful exit to ensure the game ends.

                    else:
                        missing_items = []  # Creates a list that states to the player what objectives are incomplete.

                        if not self.player.has_item("Diagnostic Tool"):
                            missing_items.append("- Find the diagnostic tool")

                        if not self.player.has_item("Energy Crystal"):
                            missing_items.append("- Find the energy crystal")
                        
                        print("You haven't completed all objectives yet!")

                        if missing_items:
                            print("Still needed:")
                            for item in missing_items:
                                print(item)  # Prints the list of objectives that are incomplete.

                        press_enter()
                        self.show_current_location()  
                        continue
                
                if self.in_droid_encounter:  # If the player is in a droid encounter, inputs are interpreted differently.

                    if choice.upper() in ['I', 'S', 'C']:  # If player chooses inventory, status or checklist during droid encounter.
                        self.handle_backpack_input(choice)

                    else:  # If player is in droid encounter, handle the droid diagnostic.
                        self.handle_droid_diagnostic()

                elif self.player.current_location == self.locations['central_hub']:
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
                    self.show_current_location()  # Displays the current location again if an invalid choice is made.
                    
            except KeyboardInterrupt:  # If the player interrupts the game with Ctrl+C.
                print("\n\nGame interrupted. Goodbye!")
                break   # Exits the game.

            except Exception as e:  # Catches any other exceptions that may occur.
                print(f"An error occurred: {e}")
                press_enter() 
                if not self.in_droid_encounter:  # If not in droid encounter, show the current location.
                    self.show_current_location()
