"""
SOUL PROJECT – CRASH COURSE IN PYTHON ESSENTIALS
Covers all core concepts needed to build a social psychology simulator.
"""

---

1. BASIC PYTHON: VARIABLES, CONTROL FLOW

---

name = "Alice"
age = 28
mood = 75
if mood > 70:
print(f"{name} feels good today.")
else:
print(f"{name} seems a bit off.")
for i in range(3):
print(f"Hour {i}: simulation tick.")

---

2. FUNCTIONS

---

def adjust_mood(person, delta):
person['mood'] += delta
person['mood'] = max(0, min(100, person['mood']))
bob = {'name': 'Bob', 'mood': 50}
adjust_mood(bob, -20)
print(bob)

---

3. CLASSES & OBJECTS

---

class Person:
def init(self, name):
self.name = name
self.mood = 50
self.energy = 100
self.friends = {}
def talk(self, other):
print(f"{self.name} talks with {other.name}.")
self.mood += 5
other.mood += 5
self.friends[other.name] = self.friends.get(other.name, 0) + 1

def **str**(self):
return f"{self.name}: mood={self.mood}, energy={self.energy}"

alice = Person("Alice")
bob = Person("Bob")
alice.talk(bob)
print(alice)

---

4. IMPORTING ACROSS FILES (FOLDER STRUCTURE)

---

In person.py:
class Person: ...
In main.py:
from person import Person

---

5. DICTIONARIES & LISTS

---

people = [alice, bob]
relationships = {
'Alice': {'Bob': 2},
'Bob': {'Alice': 1}
}

---

6. RANDOM EVENTS

---

import random
events = ["eat", "read", "nap"]
for hour in range(3):
event = random.choice(events)
print(f"At hour {hour}, Alice decides to {event}.")

---

7. TIME SIMULATION LOOP

---

for day in range(1, 4):
print(f"--- Day {day} ---")
for person in people:
person.mood += random.randint(-5, 5)
print(person)

---

8. FILE IO (OPTIONAL)

---

import json
save_data = {'people': [p.dict for p in people]}
with open("save.json", "w") as f:
json.dump(save_data, f, indent=2)

---

9. DATACLASS (OPTIONAL MODERN ALTERNATIVE)

---

from dataclasses import dataclass, field
@dataclass
class Agent:
name: str
mood: int = 50
energy: int = 100
friends: dict = field(default_factory=dict)
agent = Agent("Claire")

---

10. PROJECT STRUCTURE EXAMPLE

---

soul/
├── main.py
├── person.py -> class Person
├── world.py -> global event simulation
├── event.py -> define event types
├── utils.py -> helper functions
├── log.py -> saving, loading, logs
Ready to start building SOUL.
