import random
from world import World
from person import Person

events = ['eat', 'read', 'nap']

def choose_random_event(p:Person):
    if p.event_cooldown != 0 : return

    event = random.choice(events)
    
    match event:
        case 'eat':
            p.eat()
        case 'read':
            p.read()

def update_event_cooldowns(world:World):
    for p in world.people:
        p.event_cooldown = max(p.event_cooldown - 1, 0)