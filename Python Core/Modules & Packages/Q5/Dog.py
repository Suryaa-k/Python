from Animal import Animal      
from Walkable import Walkable  

class Dog(Animal, Walkable):   # Module C
    def move(self):
        return f"Dog: {self.name} runs quickly"

# Demo
if __name__ == "__main__":
    d = Dog("Buddy")

    # Call overridden methods
    print(d.describe())   # From Animal
    print(d.move())       # From Dog (overrides both parents)
    print(d.walk_style()) # From Walkable
    print()
    # Show MRO
    print("MRO of Dog class:")
    for cls in Dog.__mro__:
        print(cls)
