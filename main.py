from person import Person
from world import World
from utils import *
from event import *
import random


def generate_people(n:int):
    people = []
    for i in range(n):
        # name = generate_random_name()
        p = Person(generate_random_name(), random.randint(18,55))
        people.append(p)
    return people


def main_loop():
    world = World()
    world.people = generate_people(5)
    for p in world.people:
        print(p)

    while world.tick_counter < 24:
        world.print_date()
        for p in world.people:
            choose_random_event(p)
        update_event_cooldowns(world)
        world.update_tick_counter()

    for p in world.people:
        p.print_stats()



if __name__ == "__main__":
    main_loop()