from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    mood: int = 50
    energy: int = 100
    relationships: dict = field(default_factory=dict)
    event_cooldown: int = 0
    tasks: list = field(default_factory=list)

    def add_relationship(self, other_name: str, initial: int = 0):
        """Ensure a relationship entry exists with another person."""
        if other_name not in self.relationships:
            self.relationships[other_name] = initial

    def remove_relationship(self, other_name: str):
        """Remove a relationship entry if present."""
        self.relationships.pop(other_name, None)

    def get_relationship(self, other_name: str):
        """Return the relationship value with another person or ``None``."""
        return self.relationships.get(other_name)

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

    def add_task(self, description: str):
        """Add a task to the person's task list."""
        self.tasks.append(description)
        print(f"{self.name} added task: {description}")

    def complete_task(self, index: int):
        """Complete a task by index, boosting mood and costing a bit of energy."""
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.mood = min(self.mood + 10, 100)
            self.energy = max(self.energy - 5, 0)
            print(f"{self.name} completed task: {task}")
        else:
            print(f"{self.name} tried to complete invalid task index {index}")

    def socialize(self, other: 'Person'):
        self.add_relationship(other.name)
        self.relationships[other.name] += 1
        self.mood = min(self.mood + 15, 100)
        other.mood = min(other.mood + 15, 100)
        self.event_cooldown = 5
        print(f"{self.name} socialized with {other.name}")

    def natural_drain(self):
        self.energy = max(self.energy - 5, 0)
        self.mood = max(self.mood - 2, 0)

