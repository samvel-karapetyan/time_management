from src.events import Meeting, Task


class CalendarManager:
    def __init__(self):
        # load json file
        self._events = []

        self._events.append(
            Task("12.02.2026", "write a book")
        )
        
    def add_event(self):
        pass

    def mark_event_as_done(self, idx):
        pass

    def save_events(self):
        pass

    def load_events(self):
        pass

    def get_events(self):
        return self._events # list-problem