from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    def __init__(self, 
            description,
            time = None,
            location = None,
            duration = None,
            ):
        self.description = description
        self.time = time
        self.location = location
        self.duration = duration

    def get_event_type(self):
        return self.event_type
    
    @abstractmethod
    def to_markdown(self):
        """
        Returns object information as markdown string.
        """
        pass