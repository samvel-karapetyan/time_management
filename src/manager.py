import os
import json

from src.events import Event, Meeting, Task


class CalendarManager:
    def __init__(self):
        # load json file
        self._data_path = os.path.join("data", "events.json")
        self._events = self.load_events()

        self.sort_events(self._events)

    def create_event_changer(self, event):
        def event_changer():
            event.change_state()
            self.save_events()

        return event_changer

    def save_events(self):
        with open(self._data_path, "w") as f:
            json.dump(
                [event.to_dict() for event in self._events], 
                f, 
                indent=4
            )

    @classmethod
    def sort_events(cls, events):
        events.sort(key=Event.is_done)

    def load_events(self):
        events = []

        if not os.path.isfile(self._data_path):
            return events

        with open(self._data_path, "r") as f:
            events_json = json.load(f)

        type_str_to_event = {
            "Հանդիպում": Meeting,
            "Առաջադրանք": Task
        } 

        for event in events_json:
            event_type = event.pop("event_type")

            events.append(
                type_str_to_event[event_type](**event)
            )

        return events

    def get_events(self):
        return self._events # list-problem
    
    def display_input(self, type_str, col):
        if type_str == Meeting.event_type:
            self.input_values = Meeting.display_input(col)
        elif type_str == Task.event_type:
            self.input_values = Task.display_input(col)
        else:
            raise ValueError(f"Unexpected type of Event: {type_str}")
        
    def create_event_from_input(self, type_str, description):
        if type_str == Meeting.event_type:
            new_event = Meeting.create_instance(description, *self.input_values)
        elif type_str == Task.event_type:
            new_event = Task.create_instance(description, *self.input_values)
        else:
            raise ValueError(f"Unexpected type of Event: {type_str}")
        
        self._events.append(new_event)
        self.save_events()