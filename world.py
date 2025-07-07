from dataclasses import dataclass, field
from typing import List
from utils import Event
from person import Person

@dataclass
class World:
    tick_counter:int = 0
    day:int = 0
    people: List[Person]=field(default_factory=list)
    on_tick_update = Event()

    def update_tick_counter(self):
        self.day = self.tick_counter // 24
    
        self.tick_counter += 1
        self.on_tick_update.fire()

    def print_date(self):
        time = self.tick_counter if self.tick_counter//24 > 10 else "0"+str(self.tick_counter//24)
        print(f"\nDay: {self.day} Time: {time}:00 Tick: {self.tick_counter}\n")
