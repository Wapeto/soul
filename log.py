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


def save_simulation_data(world: World, filename: str = "simulation_snapshot.json"):
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
            # Relationships are maintained via Person helper methods
            "relationships": p.relationships,
            "event_cooldown": p.event_cooldown
        }
        simulation_data["people"].append(person_data)

    output_dir = "simulation_data"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        json.dump(simulation_data, f, indent=4)
    print(f"Simulation snapshot saved to {filepath}")


def plot_all_trends(logger, world):
    mood_history   = logger.get_mood_history()
    energy_history = logger.get_energy_history()

    TICKS_PER_DAY = 24

    # --- process into daily averages ---
    def compute_daily_avg(raw):
        daily = defaultdict(lambda: defaultdict(list))
        for name, hist in raw.items():
            for tick, val in hist.items():
                day = tick // TICKS_PER_DAY
                daily[name][day].append(val)
        # average
        for name, days in daily.items():
            for d, vals in days.items():
                days[d] = sum(vals) / len(vals)
        return daily

    daily_mood   = compute_daily_avg(mood_history)
    daily_energy = compute_daily_avg(energy_history)

    if not daily_mood and not daily_energy:
        print("No data to plot.")
        return

    # ——— Figure 1: Mood ———
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    for name, days in daily_mood.items():
        x = sorted(days.keys())
        y = [days[d] for d in x]
        ax1.plot(x, y, marker='o', label=name)
    ax1.set_title("Average Daily Mood Trends")
    ax1.set_xlabel("Day")
    ax1.set_ylabel("Average Mood")
    ax1.set_ylim(0, 100)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(title="People")
    # give the window a clear title
    fig1.canvas.manager.set_window_title("SOUL – Mood Trends")

    # ——— Figure 2: Energy ———
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    for name, days in daily_energy.items():
        x = sorted(days.keys())
        y = [days[d] for d in x]
        ax2.plot(x, y, marker='x', label=name)
    ax2.set_title("Average Daily Energy Trends")
    ax2.set_xlabel("Day")
    ax2.set_ylabel("Average Energy")
    ax2.set_ylim(0, 100)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(title="People")
    fig2.canvas.manager.set_window_title("SOUL – Energy Trends")

    # — show both windows simultaneously —
    plt.show()