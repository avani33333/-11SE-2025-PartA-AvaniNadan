Part A: OOP Sci-Fi Text-Based RPG (Software Focus) - Individual Project - Weighting: 25%
(Primarily addresses: SE-11-01, SE-11-02, SE-11-06, SE-11-08, SE-11-09)

Vibe Coding is NOT ALLOWED. If you use any AI assistance, you must transparently document it in your logbook—include the original generated code and explain any edits you made. Treat AI as your intern: you will be tested on your code. If you do not fully understand any AI‐generated snippet, explicitly ask AI to explain and teach it to you; if you still cannot replicate or explain it, do not use that code.

1. Game Overview
Your task is to build a minimal text-based RPG in Python. The player must follow a fixed “golden path” and earn points exactly as described below. If the player tries to move past the droid before it is repaired, a hazard counter increases. At the end, the game displays total score and hazards.

Golden Path Steps (in order):

Maintenance Tunnels: Player begins here.

Pick up the Diagnostic Tool (awards +10 points).

Use the Diagnostic Tool on the Damaged Maintenance Droid (awards +20 points) to clear it.

Move to Docking Bay.

Pick up the Energy Crystal (awards +50 points).

Type “win” (from Docking Bay) to complete the mission (awards +30 points).

Hazard Rule:

If the player tries to move east (toward Docking Bay) while the droid is still blocking, increment the hazard counter by 1 and display a “droid blocking” message.

