class StationItem:
    """Parent class for energy crystal and diagnostic tool."""
    def __init__(self, name, description, usable=True):
        self.name = name
        self.description = description
        self.usable = usable  # Indicates if the item can be used.
    
    def use(self):
        
        if self.usable:
            return f"You use the {self.name}."
        else:
            return f"The {self.name} cannot be used right now."
    
    def examine(self):
        return self.description
