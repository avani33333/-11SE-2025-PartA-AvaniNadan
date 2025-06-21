class StationItem:
    def __init__(self, name, description, usable=True):
        self.name = name
        self.description = description
        self.usable = usable
    
    def use(self):
        if self.usable:
            return f"You use the {self.name}."
        else:
            return f"The {self.name} cannot be used right now."
    
    def examine(self):
        return self.description
