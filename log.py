import json
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
import os
from person import Person
from world import World

class Logger:
    """
    A simple logging utility for the simulation.
    Records events and can save them to a file.
    """
    _instance = None # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_entries = []
            cls._instance.person_mood_history = defaultdict(lambda: defaultdict(int))
            cls._instance.person_energy_history = defaultdict(lambda: defaultdict(int))
        return cls._instance

    def log_event(self, event_type: str, description: str, person_name: str = None, details: dict = None):
        """
        Logs a general event in the simulation.
        :param event_type: Type of the event (e.g., "action", "interaction", "world_update").
        :param description: A brief description of the event.
        :param person_name: The name of the person involved (optional).
        :param details: A dictionary for additional event-specific data.
        """
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": event_type,
            "description": description,
            "person": person_name,
            "details": details if details is not None else {}
        }
        self.log_entries.append(entry)
        # print(f"LOG: [{event_type}] {description} (Person: {person_name})") # Optional: print to console

    def record_person_state(self, tick: int, person):
        """
        Records a person's mood and energy at a given tick.
        :param tick: The current simulation tick.
        :param person: The Person object whose state is being recorded.
        """
        self.person_mood_history[person.name][tick] = person.mood
        self.person_energy_history[person.name][tick] = person.energy

    def get_mood_history(self):
        return self.person_mood_history

    def get_energy_history(self):
        return self.person_energy_history

    def save_logs_to_file(self, filename: str = "simulation_log.json"):
        """
        Saves all recorded log entries to a JSON file.
        :param filename: The name of the file to save the logs to.
        """
        output_dir = "simulation_data"
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(self.log_entries, f, indent=4)
        print(f"Simulation logs saved to {filepath}")

    def clear_logs(self):
        """Clears all stored log entries."""
        self.log_entries = []
        self.person_mood_history = defaultdict(lambda: defaultdict(int))
        self.person_energy_history = defaultdict(lambda: defaultdict(int))


def save_simulation_data(world, filename: str = "simulation_snapshot.json"):
    """
    Saves the current state of the entire simulation (World and all People) to a JSON file.
    :param world: The World object representing the current state of the simulation.
    :param filename: The name of the file to save the snapshot to.
    """
    simulation_data = {
        "tick_counter": world.tick_counter,
        "day": world.day,
        "people": []
    }

    for p in world.people:
        person_data = {
            "name": p.name,
            "age": p.age,
            "mood": p.mood,
            "energy": p.energy,
            "relationships": p.relationships, # Assuming relationships are simple dicts
            "event_cooldown": p.event_cooldown
        }
        simulation_data["people"].append(person_data)

    output_dir = "simulation_data"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        json.dump(simulation_data, f, indent=4)
    print(f"Simulation snapshot saved to {filepath}")


def plot_mood_trends(logger: Logger, title: str = "Mood Trends Over Time"):
    """
    Generates and displays a plot of mood trends for all people over simulation ticks.
    :param logger: The Logger instance containing mood history data.
    :param title: The title of the plot.
    """
    mood_history = logger.get_mood_history()

    plt.figure(figsize=(12, 7))
    for person_name, history in mood_history.items():
        ticks = sorted(history.keys())
        moods = [history[tick] for tick in ticks]
        plt.plot(ticks, moods, label=person_name, marker='o', markersize=4)

    plt.title(title)
    plt.xlabel("Simulation Tick")
    plt.ylabel("Mood")
    plt.ylim(0, 100) # Mood typically ranges from 0 to 100
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title="People")
    plt.tight_layout()
    plt.show()

def plot_energy_trends(logger: Logger, title: str = "Energy Trends Over Time"):
    """
    Generates and displays a plot of energy trends for all people over simulation ticks.
    :param logger: The Logger instance containing energy history data.
    :param title: The title of the plot.
    """
    energy_history = logger.get_energy_history()

    plt.figure(figsize=(12, 7))
    for person_name, history in energy_history.items():
        ticks = sorted(history.keys())
        energies = [history[tick] for tick in ticks]
        plt.plot(ticks, energies, label=person_name, marker='x', markersize=4)

    plt.title(title)
    plt.xlabel("Simulation Tick")
    plt.ylabel("Energy")
    plt.ylim(0, 100) # Energy typically ranges from 0 to 100
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title="People")
    plt.tight_layout()
    plt.show()