# RPG Development Changelog - Part A
**Year 11 Software Engineering 2025**

## Version 0.1.0 - Initial Setup
**Released: June 9, 2025**

### Added
- Project repository setup
- README.txt file
- To-do list template
- Product requirements documentation (copied from Canvas)

---

## Version 0.2.0 - Storyline Foundation
**Released: June 10, 2025**

### Added
- Initial RPG storyline concept
- Player choice system foundation
- Diagnostic tool recovery mechanic (prevents game ending on wrong choice)
- Draft storyboard using Canva

### Changed
- Modified storyline to include meaningful player choices instead of linear progression

### Fixed
- Addressed issue where wrong choices would end game immediately

---

## Version 0.3.0 - Enhanced Storyboard
**Released: June 11, 2025**

### Added
- Multiple room selection system for finding diagnostic tool and energy crystal
- Interactive choice system replacing simple "press enter" mechanics
- Sophisticated storyboard with branching paths

### Improved
- Player engagement through meaningful decision-making
- Game flow complexity and replayability

---

## Version 0.4.0 - UML Design
**Released: June 12-13, 2025**

### Added
- UML class diagram foundation copied from Canvas template
- Understanding of UML components and relationships
- Enhanced UML diagram based on storyboard requirements
- Inheritance structure for StationItem parent class

### Documentation
- Submitted UML class diagram and storyboard as checkpoint

---

## Version 0.5.0 - Core Classes Implementation
**Released: June 14-15, 2025**

### Added
- `StationItem.py` parent class with inheritance structure
- `DiagnosticTool` and `EnergyCrystal` classes inheriting from StationItem
- `Location.py` base class with attributes: name, description, exits, has_tool, has_crystal, droid_present
- `MaintenanceTunnel` and `DockingBay` child classes

### Technical
- Implemented `super().__init__()` for proper inheritance
- Added location management system foundation

---

## Version 0.6.0 - Player System
**Released: June 16, 2025**

### Added
- `Player.py` class with core attributes: name, score, hazards, location, inventory, items, crystal_picked_up
- Backpack system with status, inventory, and checklist options
- Player methods: show_status, show_checklist, add_score, add_hazard, move_to_location, add_to_inventory

### Features
- Interactive backpack menu (keys 4, 5, 6 for different options)
- Score and hazard tracking system

---

## Version 0.7.0 - Location System Expansion
**Released: June 17, 2025**

### Added
- Sublocation system: LockerRoom, BreakRoom, StorageBay under MaintenanceTunnel
- Central hub function for navigation
- Location-specific descriptions and interactions
- `show_tool_pickup()` method for LockerRoom class

### Fixed
- Corrected DockingBay inheritance from Location instead of StationItem
- Implemented proper sublocation navigation system

### Technical
- Enhanced location header display formatting
- Added sublocation management architecture

---

## Version 0.8.0 - Game Constants & Main Menu
**Released: June 18, 2025**

### Added
- Constants system for game messages and text
- `GameIntroduction` class for main menu
- Player name input system with capitalization

### Fixed
- Import error resolved by adding `import os`
- Constants synchronization between files

### Technical
- Consolidated classes into single file for initial testing
- Game initialization sequence implemented

---

## Version 0.9.0 - Core Game Loop
**Released: June 19, 2025**

### Added
- RPG main game loop with diagnostic tool quest
- Backpack input handling (keys 4, 5, 6)
- Location change functionality
- Player inventory management

### Fixed
- AttributeError: corrected `self.player.add_to_inventory` reference
- Location transition system bugs

### Technical
- Implemented proper object method calling
- Added location state management

---

## Version 1.0.0 - Diagnostic Tool System
**Released: June 20, 2025**

### Added
- `DiagnosticTool` class with fault detection methods
- Damaged maintenance droid repair sequence
- Diagnostic tool scan functionality
- File import system for modular code structure

### Changed
- Replaced `print` statements with `return` statements for better modularity
- Separated classes into individual files

### Technical
- Improved code organization and maintainability
- Enhanced object method structure

---

## Version 1.1.0 - Bug Fixes & Crystal System
**Released: June 22, 2025**

### Added
- Energy crystal pickup mechanics
- `handle_return_locker_room` function for tool retrieval
- `in_droid_encounter` instance attribute for state tracking
- `hazard_added` flag to prevent duplicate hazard increments

### Fixed
- **Major Bug**: Hazard counter incrementing multiple times when diagnostic tool not picked up
- Tool pickup validation system
- Score calculation for incorrect choices

### Technical
- Implemented proper state management for droid encounters
- Added error prevention for hazard tracking

---

## Version 1.2.0 - Code Standards & Organization
**Released: July 13, 2025**

### Added
- PEP 8 compliant file naming
- `constants.py` file for game text and messages
- `main.py` file as entry point
- Color-coded terminal output for aesthetic appeal

### Changed
- Reorganized code structure for better maintainability
- Removed duplicate functions calling single player class methods
- Consolidated constants into separate module

### Fixed
- Score calculation bug: prevented 140/110 instead of 110/110
- Removed duplicate score addition at game end

---

## Version 1.3.0 - Final Polish & Testing
**Released: July 15-16, 2025**

### Added
- Comprehensive code comments explaining logic rather than syntax
- `os.exit()` implementation for proper game termination
- Updated UML class diagram reflecting final code structure
- Updated structure chart documentation
- Golden path storyboard revision
- Main game flow flowchart

### Testing
- Multiple complete game playthroughs
- Bug detection and resolution
- Code review for contradictory logic

### Documentation
- Enhanced inline documentation
- Final diagram updates
- Complete system testing verification
