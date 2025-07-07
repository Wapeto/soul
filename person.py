from dataclasses import dataclass, field

# Logger is imported lazily inside methods to avoid circular imports

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

    def socialize(self, other: 'Person'):
        from log import Logger  # local import to avoid circular dependency

        logger = Logger()

        # Record state before interaction
        self_mood_before = self.mood
        self_energy_before = self.energy
        other_mood_before = other.mood
        other_energy_before = other.energy

        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        self.relationships[other.name] += 1
        relationship_value = self.relationships[other.name]

        self.mood = min(self.mood + 15, 100)
        other.mood = min(other.mood + 15, 100)
        self.event_cooldown = 5

        logger.log_event(
            "interaction",
            f"{self.name} socialized with {other.name}. Relationship now {relationship_value}",
            self.name,
            {
                "self_mood_before": self_mood_before,
                "self_energy_before": self_energy_before,
                "self_mood_after": self.mood,
                "self_energy_after": self.energy,
                "other": other.name,
                "other_mood_before": other_mood_before,
                "other_energy_before": other_energy_before,
                "other_mood_after": other.mood,
                "other_energy_after": other.energy,
                "relationship": relationship_value,
            },
        )

        print(f"{self.name} socialized with {other.name}")

    def natural_drain(self):
        self.energy = max(self.energy - 5, 0)
        self.mood = max(self.mood - 2, 0)

