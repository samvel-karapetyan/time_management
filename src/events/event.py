from abc import ABC, abstractmethod


class Event(ABC):
    event_type = "Event"

    @abstractmethod
    def __init__(self, 
            description,
            done = False,
            ):
        self.description = description
        self.done = done

    @classmethod
    def get_event_type(cls):
        return cls.event_type
    
    @abstractmethod
    def to_markdown(self):
        """
        Returns object information as markdown string.
        """
        pass

    @classmethod
    @abstractmethod
    def display_input(cls):
        pass

    @classmethod
    @abstractmethod
    def create_instance(cls):
        pass

    def is_done(self):
        return self.done
    
    def change_state(self):
        self.done = not self.done

    def to_dict(self, **kwargs):
        return dict(
            event_type=self.event_type,
            description=self.description,
            done=self.done,
        )
        
    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)
    