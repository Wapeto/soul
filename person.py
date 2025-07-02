from dataclasses import dataclass, field

@dataclass
class Person:
    name:str
    age:int
    mood:int=50
    energy:int = 100
    relationships: dict=field(default_factory=dict)
    event_cooldown:int = 0

    def print_stats(self):
        print(f"\n{self.name}\nMood: {self.mood}\nEnergy: {self.energy}")

    def eat(self):
        self.energy = min(self.energy + 10, 100)
        self.mood = min(self.mood + 5, 100)
        self.event_cooldown = 3
        print(f"{self.name} has eaten")

    def read(self):
        self.mood = min(self.mood + 10, 100)
        self.energy = max(self.energy - 5, 0)
        self.event_cooldown = 2
        print(f"{self.name} has read for a bit")

    def nap(self):
        self.energy = min(self.energy + 30, 100)
        print(f"{self.name} just took a nap")

