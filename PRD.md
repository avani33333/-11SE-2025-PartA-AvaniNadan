1. StationItem (parent of both tool classes)
Purpose: Serves as a common parent for any item the player can pick up.

Attributes:

_name

_description

Methods:

examine()

Returns a text description specific to the item. Both subclasses override this.

2. DiagnosticTool (inherits from StationItem)
Purpose: The tool used to repair the droid.

Parent: StationItem

Attributes:

(inherits _name and _description)

Methods:

examine()

Returns a hint such as “This diagnostic tool seems designed to interface with maintenance droids.”

3. EnergyCrystal (inherits from StationItem)
Purpose: The volatile crystal that the player must collect.

Parent: StationItem

Attributes:

(inherits _name and _description)

Methods:

examine()

Returns a description like “The crystal pulses with an unstable, vibrant energy.”

4. Location
Purpose: Represents a place in the game world. Each location can hold exactly one tool, one crystal, and/or the droid.

Attributes:

name

description

exits

has_tool

has_crystal

droid_present

Methods:

__init__

Initialise the location’s name, description, and default flags (no tool, no crystal, no droid).

add_exit(direction, other_location)

Record that a given direction (e.g. “east”) leads to another Location.

describe()

Return a formatted string that includes:

The location’s name and description.

“You see a diagnostic tool here.” if has_tool is True.

“You see an energy crystal here.” if has_crystal is True.

“A maintenance droid blocks the way!” if droid_present is True.

“Exits: <list of directions>.”

remove_tool()

If has_tool is True, clear that flag and indicate success; otherwise indicate failure.

remove_crystal()

If has_crystal is True, clear that flag and indicate success; otherwise indicate failure.

set_droid_present(flag)

Set the droid_present flag to True or False.

5. DamagedMaintenanceDroid
Purpose: Blocks passage in Maintenance Tunnels until “repaired.”

Attributes:

blocking

Methods (purpose only):

__init__

Set blocking to True initially.

repair()

Change blocking to False.

is_blocking()

Return whether blocking is still True.

6. Player
Purpose: Tracks the player’s current location, which items they hold, and their score/hazard counts.

Attributes:

current_location

has_tool

has_crystal

score

hazard_count

Methods:

__init__(starting_location)

Set current_location to the given Location; set has_tool and has_crystal to False, and score and hazard_count to zero.

move(direction)

Attempt to change current_location in the given direction:
• If no such exit exists, return failure.
• If the droid is still blocking, increment hazard_count, return failure.
• Otherwise update current_location and return success.

pick_up_tool()

If current_location.has_tool is True, clear that flag, set has_tool to True, add 10 to score, and return success; otherwise return failure.

use_tool_on_droid()

If has_tool is True and current_location.droid_present is True, call the droid’s repair method, clear droid_present, add 20 to score, return success; otherwise return failure.

pick_up_crystal()

If current_location.has_crystal is True, clear that flag, set has_crystal to True, add 50 to score, return success; otherwise return failure.

get_status()

Return the current score and hazard count (students decide how to format).

7. GameController
Purpose: Creates and links all objects, runs the main input loop, and checks if the player wins.

Attributes:

maintenance_tunnels

docking_bay

droid

player

diagnostic_tool

energy_crystal

Methods:

__init__

Build the world (all locations, the droid, the two items, and the player).

setup_world()

Create two Location instances: one for “Maintenance Tunnels,” one for “Docking Bay.”

Indicate that Maintenance Tunnels starts with has_tool = True and droid_present = True.

Indicate that Docking Bay starts with has_crystal = True.

Link the two locations so that “east” from Maintenance Tunnels goes to Docking Bay, and “west” from Docking Bay goes back.

Instantiate a DamagedMaintenanceDroid and store it.

Instantiate one DiagnosticTool and one EnergyCrystal (students decide how these are held).

Instantiate a Player whose starting_location is Maintenance Tunnels.

start_game()

Print a welcome message. Then repeat:

Show current_location.describe().

Read a single line of input (allowed commands below).

Call process_input(command).

Call check_win_condition(). If True, break and end.

process_input(command)

Recognise exactly these commands (case-insensitive):

“move <direction>” → call player.move(direction) and print an appropriate message for success or failure (blocked by droid or no exit).

“pick up tool” → call player.pick_up_tool() and print success or “no tool here.”

“use tool” → call player.use_tool_on_droid() and print success or “nothing happens.”

“pick up crystal” → call player.pick_up_crystal() and print success or “no crystal here.”

“status” → call player.get_status() and print “Score: <score> Hazards: <hazard_count>”.

“win” → do nothing here (the check happens next).

Anything else → print “Invalid command.”

check_win_condition()

If all of these are true:

player.current_location is Docking Bay

player.has_crystal is True

the last command was “win”

Then add 30 to player.score, print:

Mission complete! Final Score: <score> Total Hazards: <hazard_count>
and return True; otherwise return False.

You may add any extra storyline around this, as long as the minimum requirements are met and demonstrable.
