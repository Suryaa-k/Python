class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Animal: {self.name}"

    def move(self):
        return f"{self.name} moves in a generic way"

