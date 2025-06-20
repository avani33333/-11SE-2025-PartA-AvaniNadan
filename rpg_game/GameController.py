PLAYER_SCORE = 0
HAZARDS_ENCOUNTERED = 0


GAME_MESSAGE = (
    "\nWelcome aboard, Specialist {player_name}."
    "\nThe Celestial Outpost C.O.I.P.E.A. was last heard from 72 hours ago."
    "\nNo life signs detected. All communication offline."
    "\nThe only transmission received:"
    "\n\033[3mSystem compromised… crystal stolen… droid malfunctioning...\033[0m"
    "\nYou dock in the Maintenance Tunnels, the dim lights flickering above."
)

WELCOME_MESSAGE = (
    "\033[1mWELCOME TO MISSION COIPEA\033[0m\n"
    "\nYou are a newly recruited tech specialist aboard the Celestial Outpost, "
    "a deep-space engineering base that has gone dark after a system-wide failure. "
    "As the only responder within range, you're tasked with investigating the critical failure, "
    "clearing blocked paths, retrieving a rare energy crystal, and ensuring base recovery protocols are executed."
    "\nTime is critical. Systems are unstable. Droids are malfunctioning."
    "\nWe are relying on you to complete the mission."
    "\n"
)

def clear_screen() -> None:
    """Clears the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter() -> None:
    """Prompt the user to press Enter to continue."""
    input("\nEnter: Continue")



class GameIntroduction:
    def __init__(self, player=None) -> None:
        self.player = None
        

    def show_intro(self) -> None:
        clear_screen()
        print("\033[0m" + WELCOME_MESSAGE)  # Reset formatting

        while True:
            player_name = input("\033[3mEnter your name, Specialist: \033[0m").strip()
            if player_name:
                break
            print("Name cannot be empty. Please try again.")

        self.player = Player(player_name.capitalize())
        clear_screen()
        print(GAME_MESSAGE.format(player_name=self.player.name))


class RPGGameRun:
    def __init__(self):
        self.player = None
        self.locations = {
            'central_hub': MaintenanceTunnel(),
            'break_room': BreakRoom(),
            'locker_room': LockerRoom(),
            'storage_bay': StorageBay(),
            'docking_bay': DockingBay()
        }
    
    def start_game(self):
        game_intro = GameIntroduction()
        game_intro.show_intro()
        self.player = game_intro.player
        self.player.move_to_location(self.locations['central_hub'])
        press_enter()
        self.show_current_location()
        self.game_loop()
    
    def show_current_location(self):
        clear_screen()
        if self.player.current_location == self.locations['central_hub']:
            self.locations['central_hub'].show_central_hub()
        elif self.player.current_location == self.locations['break_room']:
            self.locations['break_room'].show_break_room()
        elif self.player.current_location == self.locations['locker_room']:
            self.locations['locker_room'].show_locker_room()
        elif self.player.current_location == self.locations['storage_bay']:
            self.locations['storage_bay'].show_storage_bay()
        
        print("------------------------------------")
        self.player.show_backpack_options()
    
    def move_player(self, location_key):
        if location_key in self.locations:
            self.player.move_to_location(self.locations[location_key])
            self.show_current_location()
    
    def handle_central_hub_input(self, choice):
        if choice == '1':  # go to the break room to find diagnositic tool (WRONG)
            self.move_player('break_room')
        elif choice == '2': #go to the locker room to find diagnositic tool (CORRECT)
            self.move_player('locker_room')
        elif choice == '3':   # go to the storage room to find diagnositic tool (WRONG)
            self.move_player('storage_bay')
        else:
            self.handle_backpack_input(choice)
    
    def handle_break_room_input(self, choice):
        if choice == '' or choice.lower() == 'enter':
            self.move_player('central_hub')
        else:
            self.handle_backpack_input(choice)
    
    def handle_locker_room_input(self, choice):
        if choice == '1':  # Check Locker 1
            print("This locker is empty.")
            press_enter()
        if choice == '2': # check locker 2
            print("This locker contains old moldy boots.")
            self.show_current_location()
        elif choice == '3':  # Check Locker 3 (has tool)
            self.show_tool_pickup()
        else:
            self.handle_backpack_input(choice)
    
    def handle_storage_bay_input(self, choice):
        if choice == '' or choice.lower() == 'enter':
            self.move_player('central_hub')
        else:
            self.handle_backpack_input(choice)
    
    def show_tool_pickup(self):
        clear_screen()
        self.locations['locker_room'].show_tool_pickup()
        
        while True:
            choice = input("\nEnter your choice: ").strip()
            if choice == '1':  # Pick it up
                self.player.add_to_inventory("Diagnostic Tool")
                self.player.add_score(10)
                print("This diagnostic tool seems designed to interface with maintenance droids.")
                print("+ added to inventory")
                print(f"+ 10 points to score (Total: {self.player.score})")
                press_enter()
                self.move_player('locker_room')
                break
            elif choice == '2':  # Leave it
                print("You decide to leave the tool for now.")
                press_enter()
                self.move_player('central_hub')
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def handle_backpack_input(self, choice):
        """Handle backpack/inventory inputs."""
        if choice == '4':  # Inventory
            print("\n")
            self.player.show_inventory()
            press_enter()
            self.show_current_location()
        elif choice == '5':  # Status
            print("\n")
            self.player.show_status()
            press_enter()
            self.show_current_location()
        elif choice == '6':  # Checklist
            print("\n")
            self.player.show_checklist()
            press_enter()
            self.show_current_location()
        else:
            print("Invalid choice. Please try again.")
            press_enter()
            self.show_current_location()
    
    def game_loop(self):
        while True:
            try:
                choice = input("\nEnter your choice: ").strip()
                
                if self.player.current_location == self.locations['central_hub']:
                    self.handle_central_hub_input(choice)
                elif self.player.current_location == self.locations['break_room']:
                    self.handle_break_room_input(choice)
                elif self.player.current_location == self.locations['locker_room']:
                    self.handle_locker_room_input(choice)
                elif self.player.current_location == self.locations['storage_bay']:
                    self.handle_storage_bay_input(choice)
                
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                press_enter()
                self.show_current_location()

#start the game
if __name__ == "__main__":
    start_RPG = RPGGameRun()
    start_RPG.start_game()
