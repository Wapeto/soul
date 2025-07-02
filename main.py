from person import Person
from world import World
from utils import *
from event import *
import random
from log import Logger, save_simulation_data, plot_mood_trends, plot_energy_trends



def generate_people(n:int):
    people = []
    for i in range(n):
        # name = generate_random_name()
        p = Person(generate_random_name(), random.randint(18,55))
        people.append(p)
    return people


def main_loop():
    logger = Logger() # Get the singleton logger instance
    world = World()
    world.people = generate_people(5)
    for p in world.people:
        print(p)

    while world.tick_counter < 24: # Simulating 24 hours
        world.print_date()

        # Record initial state for the tick
        for p in world.people:
            logger.record_person_state(world.tick_counter, p)

        for p in world.people:
            # Add a log entry for chosen event
            chosen_event_name = choose_random_event(p)
            if chosen_event_name: # Only log if an event actually occurred
                logger.log_event("action", f"{p.name} performed {chosen_event_name}", p.name, {"mood_before": p.mood, "energy_before": p.energy})
                # Note: mood/energy changes happen inside the person's method.
                # The next call to record_person_state will capture the new state.

        update_event_cooldowns(world)
        world.update_tick_counter()

    print("\n--- Simulation Complete ---")
    for p in world.people:
        p.print_stats()

    # After the loop, save data and plot graphs
    save_simulation_data(world, "final_simulation_state.json")
    logger.save_logs_to_file("detailed_simulation_events.json")

    plot_mood_trends(logger)
    plot_energy_trends(logger)



if __name__ == "__main__":
    main_loop()