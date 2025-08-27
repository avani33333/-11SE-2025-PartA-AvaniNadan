# Player status constants.
PLAYER_SCORE = 0
HAZARDS_ENCOUNTERED = 0

# Game messages constants.
WELCOME_MESSAGE = (
    "\033[1m\033[34mWELCOME TO MISSION COIPEA\033[0m\n"
    "\nYou are a newly recruited tech specialist aboard the Celestial "
    "Outpost, \na deep-space engineering base that has gone dark after a "
    "system-wide failure. \nAs the only responder within range, you're "
    "tasked with investigating the critical failure, \nclearing blocked "
    "paths, retrieving a rare energy crystal, and ensuring base recovery "
    "protocols are executed. \nTime is critical. Systems are unstable. "
    "Droids are malfunctioning. \nWe are relying on you to complete the "
    "mission. \n\033[0m"
)


GAME_MESSAGE = (
    "\n\033[1mWelcome aboard, Specialist {player_name}.\033[0m\n"
    "\nThe Celestial Outpost C.O.I.P.E.A. was last heard from 72 hours ago."
    "\nNo life signs detected. All communication offline."
    "\nThe only transmission received:\n"
    "\n\033[94m\033[3mSystem compromised… crystal stolen… droid "
    "malfunctioning...\033[0m\033[0m\n"
    "\nYou dock in the Maintenance Tunnels, the dim lights flickering "
    "above.\n"
)

WEST_TUNNEL_MESSAGE = (
    "\nThe hallway stretches forward into darkness."
    "\nA collapsed beam blocks the path ahead. Chunks of ceiling tile and "
    "\nloose wires hang like vines."
    "\nDead end."
    "\nYou return back."
    "\n------------------------------------\n"
)


BACKPACK_OPTIONS = (
    "\n------------------------------------"
    "\n\033[91mI: Inventory\033[0m"
    "\n\033[95mS: Status\033[0m"
    "\n\033[92mC: Checklist\033[0m"
    "\n\033[3mEnter: Continue \033[0m"
    "\n------------------------------------"
)

RUN_DIAGNOSTIC_OPTIONS = (
    "\n\033[1mWould you like to run a diagnostic test?\033[0m"
    "\n------------------------------------"
    "\n\033[1mLocation: Maintenance Tunnel\033[0m"
    "\n\033[94m1: Yes\033[0m"
    "\n\033[94m2: No\033[0m"
    "\n------------------------------------"
)

CHOICE_1_CARGO_SECTION = (
    "\nYou pry open the crate."
    "\n"
    "\n\033[94m\033[1mInside:\033[0m\033[0m\n"
    "\n\033[94m - Empty stasis jars\033[0m"
    "\n\033[94m - Broken cryo-pods\033[0m"
    "\n\033[94m - A labelled vial of something long since "
    "evaporated\033[0m"
    "\n\nNothing to use in here."
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CHOICE_2_CARGO_SECTION = (
    "\nYou unlatch the metal box."
    "\n"
    "\n\033[94m\033[1mInside:\033[0m\033[0m\n"
    "\n\033[94m - A broken plasma cutter\033[0m"
    "\n\033[94m - Melted wiring\033[0m"
    "\n\033[94m - A manual titled: \"How to Handle High-Risk Repairs\" "
    "(most pages missing)\033[0m"
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CHOICE_3_CARGO_SECTION = (
    "\nYou open the container and sift through wires and junk."
    "\n\033[94m\033[1mInside:\033[0m\033[0m\n"
    "\n\033[94m - A snapped antenna\033[0m"
    "\n\033[94m - Cracked memory chips\033[0m"
    "\n\033[94m - A data slate with the message: \"Error 404 – Logs Not "
    "Found\"\033[0m"
    "\nA pile of worthless junk"
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CHOICE_1_CONSOLE_ROOM = (
    "\nYou tap the blinking key."
    "\nThe screen loads..."
    "\n"
    "\n\033[34m> [CARGO INTAKE LOG - 27 DAYS AGO]"
    "\n> \"6x Power Cells, 14x Ration Crates, 1x Decorative Plant, 0x "
    "Crystal.\"\033[0m"
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CHOICE_2_CONSOLE_ROOM = (
    "\nYou boot the panel."
    "\nThe screen floods with flashing alerts:"
    "\n"
    "\n\033[34m> `OXYGEN FLOW ERROR: FILTER FAILURE`"
    "\n> `TEMP STABILITY: CRITICAL LOW`"
    "\n> `CRYSTAL COOLANT: UNKNOWN`\033[0m"
    "\nThat last one catches your eye… but when you click it:"
    "\n\033[34m> [DATA CORRUPTED - FILE CANNOT LOAD]\033[0m"
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CHOICE_3_CONSOLE_ROOM = (
    "\nYou boot the terminal and wait as the screen stabilizes."
    "\nAfter a moment, a video log blinks on screen."
    "\n"
    "\n\033[34m> `LAST ITEM TRANSPORTED:`"
    "\n> `Item: ENERGY CRYSTAL`"
    "\n> `Destination: SUPPLY AREA - Compartment 3`\033[0m"
    "\n"
    "\nThe system beeps and displays a log:"
    "\n"
    "\n>\033[34m `CRYSTAL HANDLED UNDER PROTOCOL 8421`"
    "\n> `Access Level: Specialist Clearance`\033[0m"
    "\nThis may be useful."
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CHOICE_1_SUPPLY_HUB = (
    "\nYou pull open the sliding shelf and rummage through it."
    "\n"
    "\n\033[94m\033[1mInside:\033[0m\033[0m\n"
    "\n\033[94m - A stack of empty crates"
    "\n - A faded sign that reads: \"DEFECTIVE - DO NOT REUSE\""
    "\n - An ancient sandwich wrapper\033[0m"
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CHOICE_2_SUPPLY_HUB = (
    "\nShelf A2 contains various power cores, some still glowing faintly."
    "\nYou dig deeper…"
    "\n"
    "\n\033[94m\033[1mFindings:\033[0m\033[0m\n"
    "\n\033[94m - Burnt wiring"
    "\n - An empty crystal stabilizer frame"
    "\n - A box labelled \"For Training Only\"\033[0m"
    "\n------------------------------------"
    "\n\033[3mPress enter to continue back to the open crates scene "
    "\033[0m"
    "\n------------------------------------"
)

CRYSTAL_PICKUP_MESSAGE = (
    "\nYou return to Shelf A3 where the Energy Crystal still glows softly."
    "\nThe crystal pulses with an unstable, vibrant energy."
    "\n------------------------------------"
    "\n\033[1mWhat do you want to do?\033[0m\n"
    "\n------------------------------------"
    "\n\0331: Pick it up"
    "\n2: Leave it\033[0m"
    "\n------------------------------------"
)

POINTS_REWARD_CRYSTAL = (
    "\n\033[95mThe crystal pulses with an unstable, vibrant energy."
    "\n+crystal removed"
    "\n+50 points\033[0m"
    "\n------------------------------------"
)

NO_POINTS_REWARD_CRYSTAL = (
    "\n\033[95mThe crystal pulses with an unstable, vibrant energy."
    "\n+crystal removed"
    "\n(No points awarded - you should have picked this up "
    "earlier!)\033[0m"
    "\n------------------------------------"
)

TYPE_WIN_DOCKING_BAY = (
    "\nYou have arrived at the control console of the Docking Bay. "
    "Systems flicker back online."
    "\n------------------------------------"
    "\n\033[1mLocation: Docking Bay\033[0m\n"
    "\n\033[94mType 'win' to complete your mission!\033[0m"
    "\n------------------------------------"
)

COMPLETED_GAME_MESSAGE = (
    "\nReach the docking bay and type \"win\" to complete the mission "
    "(press enter to confirm)"
    "\nYou have arrived at the control console of the Docking Bay. "
    "Systems flicker back online."
    "\n------------------------------------"
    "\n\033[1mLocation: Docking Bay\033[0m\n"
    "\n\033Enter:\033[0m"
)
