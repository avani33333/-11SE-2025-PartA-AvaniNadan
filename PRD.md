# Space Station RPG - Object-Oriented Design

## Overview

### Game Concept
A text-based RPG set in a malfunctioning space station where players navigate through various locations, solve puzzles, and complete objectives to restore the station's systems.

### Core OOP Concepts

#### 1. Class and Object
- **Definition**: A class is a blueprint for creating objects, while an object is an instance of a class that contains both data (attributes) and behavior (methods).
- **Example**: The `Player` class defines what a player is, and each player object has unique attributes like name and score.

#### 2. Inheritance
- **Definition**: A mechanism where a new class inherits properties and methods from an existing class, promoting code reuse and establishing a hierarchical relationship.
- **Example**: `DiagnosticTool` and `EnergyCrystal` both inherit from the base `StationItem` class.

#### 3. Polymorphism
- **Definition**: The ability of different classes to be treated as instances of the same class through a common interface, allowing methods to do different things based on the object's class.
- **Example**: Different items can be used, but each has its own implementation of the `use()` method.

#### 4. Encapsulation
- **Definition**: The bundling of data with the methods that operate on that data, and restricting direct access to some of an object's components.
- **Example**: Player's score is accessed through methods rather than directly.

#### 5. Abstraction
- **Definition**: Hiding complex implementation details and showing only the necessary features of an object.
- **Example**: The game's main loop doesn't need to know how each item works internally, just that it can be used.

### Class Relationships

1. **Composition**
   - **Definition**: A strong "has-a" relationship where the child cannot exist independently of the parent.
   - **Example**: The game world contains locations that don't exist outside of it.

2. **Aggregation**
   - **Definition**: A "has-a" relationship where the child can exist independently of the parent.
   - **Example**: A location contains items that can be moved between locations.

3. **Association**
   - **Definition**: A "uses-a" relationship where objects are aware of each other and can invoke each other's methods.
   - **Example**: The player has a current location.

4. **Dependency**
   - **Definition**: A "uses" relationship where one class depends on another but doesn't maintain a permanent link.
   - **Example**: The game introduction uses the player object temporarily.

## 1. Class and Object Implementation

## 1. Class and Object Implementation

### Player Class
```python
class Player:
    def __init__(self, name: str, score: int = 0, hazards: int = 0):
        self.name = name
        self.score = score
        self.hazards = hazards
        self.current_location = None
        self.inventory = []
        self.station_items = []
        self.crystal_picked_up = False
```
**Key Methods:**
- `show_status()`: Displays player stats
- `add_to_inventory(item)`: Manages player items
- `move_to_location(location)`: Handles player movement

### StationItem Base Class
```python
class StationItem:
    def __init__(self, name, description, usable=True):
        self.name = name
        self.description = description
        self.usable = usable
    
    def use(self):
        return f"You use the {self.name}."
```

## 2. Inheritance in the Game

### Location Hierarchy
```python
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

class MaintenanceTunnel(Location):
    def __init__(self):
        super().__init__(
            "Maintenance Tunnel",
            "A dimly lit maintenance tunnel with flickering lights."
        )
```

### Item System
```python
class DiagnosticTool(StationItem):
    def __init__(self):
        super().__init__(
            "Diagnostic Tool",
            "A tool for repairing droids.",
            True
        )
        self.can_disable_droids = True
```

## 3. Polymorphism in Action

### Method Overriding
```python
# In StationItem base class
def use(self):
    return f"You use the {self.name}."

# In EnergyCrystal subclass
def use(self):
    return "The crystal pulses with energy but nothing happens."
```

### Duck Typing
```python
def interact_with_item(item):
    # Works with any object that has a use() method
    return item.use()
```

## 4. Encapsulation Patterns

### Data Protection
```python
class Player:
    def __init__(self):
        self._score = 0
        
    def add_score(self, points):
        if points > 0:
            self._score += points
            
    def get_score(self):
        return self._score
```

## 5. Class Relationships

### Composition (Strong Ownership)
```python
class GameController:
    def __init__(self):
        self.player = Player()  # GameController owns Player
        self.locations = {
            'central_hub': MaintenanceTunnel(),
            'break_room': BreakRoom()
        }
```

### Association (Uses Relationship)
```python
class Player:
    def __init__(self):
        self.current_location = None  # References a Location
```

### Aggregation (Whole-Part)
```python
class Location:
    def __init__(self):
        self.items = []  # Contains Item objects that can exist independently
```

### Dependency
```python
class GameIntroduction:
    def __init__(self, player):
        self.player = player  # Depends on Player
```

## 6. Game Flow

### 6.1 Game Progression

1. **Game Start**
   - Player enters their name
   - Introduction sequence plays
   - Player spawns in the Maintenance Tunnel

2. **Initial Exploration**
   - Player can explore connected locations
   - Discovers the damaged droid blocking progress
   - Must find the diagnostic tool in the Locker Room

3. **Droid Repair**
   - Use diagnostic tool on the droid
   - Solve the repair minigame
   - Clear the path to new areas

4. **Crystal Retrieval**
   - Navigate to the Supply Hub
   - Locate and collect the energy crystal
   - Avoid or overcome hazards

5. **Mission Completion**
   - Return to the Docking Bay
   - Use the crystal to restore power
   - Complete the mission

### 6.2 Key Interactions

#### Droid Encounter
```
[Maintenance Tunnel East Corridor]
A damaged maintenance droid blocks your path.

Actions:
1. Try to sneak past (80% chance of failure)
2. Use diagnostic tool (if in inventory)
3. Return to previous area
```

#### Item Usage
```
> use diagnostic tool

[Diagnostic Tool]
Running scan on droid...
Error Code: M-43X Detected
Droid mobility subroutine malfunctioning.

1. Attempt repair
2. Back
```

## 7. Game Components

### 7.1 Core Game Objects

#### Player
- **Purpose**: Represents the player character
- **Key Attributes**:
  - `name`: Player's name
  - `score`: Current game score
  - `hazards`: Number of hazards encountered
  - `inventory`: List of carried items
  - `current_location`: Current game location

#### Location
- **Purpose**: Base class for all game areas
- **Key Attributes**:
  - `name`: Location identifier
  - `description`: Detailed area description
  - `exits`: Connected locations
  - `items`: Interactive objects in the area

#### StationItem
- **Purpose**: Base class for all interactive items
- **Key Attributes**:
  - `name`: Item name
  - `description`: Item details
  - `usable`: Whether the item can be used

### 7.2 Key Game Mechanics

#### Item Interaction
```python
# Example of polymorphic item usage
def use_item(item):
    if hasattr(item, 'use') and callable(item.use):
        return item.use()
    return "Nothing happens."
```

#### Location Navigation
```python
# Example of association between Player and Location
class Player:
    def move_to(self, direction):
        if direction in self.current_location.exits:
            self.current_location = self.current_location.exits[direction]
            return True
        return False
```

### 7.3 Class Relationships Summary

| Relationship | Example | Description |
|--------------|---------|-------------|
| Composition | `GameController` owns `Player` | Strong ownership, lifetime control |
| Aggregation | `Location` contains `Item`s | Items can exist independently |
| Association | `Player` has `current_location` | Uses relationship |
| Dependency | `GameIntroduction` uses `Player` | Temporary usage |

## 8. Conclusion

### 8.1 Design Patterns Used

1. **Factory Pattern**
   - Item creation through factory methods
   - Location creation through dedicated factory functions

2. **State Pattern**
   - Game states (exploration, combat, dialogue)
   - Location-specific behaviors

3. **Observer Pattern**
   - Event system for game state changes
   - Player stats monitoring

### 8.2 Key Design Decisions

1. **Component-Based Architecture**
   - Decoupled game systems
   - Easy to extend with new features

2. **Data-Driven Design**
   - Game data separated from logic
   - Easy content updates without code changes

3. **Modular Code Organization**
   - Clear separation of concerns
   - Easy to maintain and test

### 8.3 Future Extensions

1. **New Game Items**
   - Additional tools and collectibles
   - Crafting system

2. **Expanded World**
   - More locations to explore
   - Additional NPCs and quests

3. **Enhanced Gameplay**
   - Combat system
   - Puzzle mechanics
   - Dialogue system
- Methods:
  - get_full_location_name(): Return formatted location name
  - display_location_header(objective=None): Show location header
  - show_description(): Display location details

#### Location Subclasses
1. MaintenanceTunnel
   - Central hub with multiple exit paths
   - Initial player spawn point
   - Mission objective display

2. BreakRoom
   - Rest area with vending machines
   - No useful items
   - Dead end location

3. LockerRoom
   - Contains diagnostic tool
   - Multiple lockers to search
   - Key location for tool acquisition

4. StorageBay
   - Cluttered with old tech
   - Dead end location
   - No useful items

5. DockingBay
   - Final mission location
   - Multiple cargo sections to search
   - Mission completion point

6. CargoSection
   - Multiple cargo units to explore
   - Contains mission-critical items
   - Complex navigation required

7. ConsoleRoom
   - Contains control terminals
   - Requires diagnostic tool usage
   - System diagnostics location

8. SupplyHub
   - Contains energy crystal
   - Final objective location
   - Mission completion point

9. MaintenanceTunnelEastCorridor
   - Connects to docking bay
   - Multiple path choices
   - Navigation challenge

### 2.4 Item Components
#### Base Class: StationItem
- Attributes:
  - name: str (Item identifier)
  - description: str (Item details)
  - usable: bool (Can be activated)
- Methods:
  - activate(): Apply item effects

#### Item Subclasses
1. EnergyCrystal
   - Mission-critical item
   - Powers station systems
   - Located in SupplyHub
   - Special activation required

2. DiagnosticTool
   - Repairs station systems
   - Required for droid repair
   - Found in LockerRoom
   - Multiple usage options

### 3. Game Flow

#### 3.1 Game Setup
1. Player enters name
2. Game introduction displayed
3. Player starts in MaintenanceTunnel
4. Initial mission objectives shown

#### 3.2 Main Game Loop
1. Display current location
2. Show available actions
3. Player makes choice
4. Execute action
5. Update game state
6. Repeat until game completion

#### 3.3 Mission Objectives
1. Find diagnostic tool
2. Repair maintenance droid
3. Find energy crystal
4. Reach docking bay
5. Complete mission

#### 3.4 Game States
1. Initial Setup
2. Tool Search
3. Droid Repair
4. Crystal Search
5. Mission Completion

### 4. Technical Requirements

#### 4.1 System Requirements
- Python 3.x
- Command-line interface
- ANSI color support
- Text-based input/output

#### 4.2 Core Game Components
1. Game Controller
   - Manages game state
   - Handles player actions
   - Controls game flow
   - Tracks mission progress

2. Location System
   - Manages station areas
   - Handles navigation
   - Controls location-specific events
   - Tracks item placement

3. Item System
   - Manages inventory
   - Handles item interactions
   - Tracks item usage
   - Controls mission items

4. Player System
   - Manages character state
   - Handles player actions
   - Tracks progress
   - Controls scoring

### 5. User Interface

#### 5.1 Text Output
- Colored text for emphasis
- Clear status displays
- Location descriptions
- Inventory listings
- Objective tracking

#### 5.2 Input Handling
- Number-based menu selection
- Enter key for progression
- Clear screen between actions
- Error handling for invalid input

#### 5.3 Status Displays
- Player stats
- Current location
- Inventory contents
- Mission objectives
- Points tracking

### 6. Success Criteria

#### 6.1 Player Progress
- Complete all mission objectives
- Find and use diagnostic tool
- Repair maintenance droid
- Locate energy crystal
- Reach docking bay

#### 6.2 Scoring System
- Points for objectives completed
- Bonus points for hazards overcome
- Time-based scoring
- Item collection points

#### 6.3 Completion Requirements
- All mission objectives completed
- Energy crystal activated
- Station systems restored
- Reach docking bay
- Type 'win' command
