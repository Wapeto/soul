import random

class Event:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, fn):
        self.subscribers.append(fn)
    def unsubscribe(self,fn):
        self.subscribers.remove(fn)
    def fire(self, *args, **kwargs):
        for fn in self.subscribers:
            fn(*args, **kwargs)
        


names = [
    "Alice", "Bob", "Charlie", "David", "Eve",
    "Frank", "Grace", "Heidi", "Ivan", "Judy",
    "Karl", "Leo", "Mallory", "Nina", "Oscar",
    "Peggy", "Quentin", "Rupert", "Sybil", "Trent",
    "Uma", "Victor", "Walter", "Xena", "Yara", "Zane"]

def generate_random_name():
    """Generate a random name from the predefined list."""
    return random.choice(names)