import random
from world import World
from person import Person

events = ['eat', 'read', 'nap', 'perform_task']

def choose_random_event(p:Person):
    if p.event_cooldown != 0 :
        # print(f"{p.name} is on cooldown for {p.event_cooldown} ticks.") # Optional: for debugging
        
        return None # Return None if no event is chosen due to cooldown

    event = random.choice(events)

    match event:
        case 'eat':
            p.eat()
        case 'read':
            p.read()
        case 'nap':
            p.nap()
        case 'perform_task':
            if p.tasks:
                idx = random.randrange(len(p.tasks))
                p.complete_task(idx)
            else:
                p.add_task("General task")
    return event

def update_event_cooldowns(world:World):
    for p in world.people:
        p.event_cooldown = max(p.event_cooldown - 1, 0)

