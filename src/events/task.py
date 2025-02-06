from src.events import Event


class Task(Event):
    def __init__(self, 
            deadline,
            description,
            *args,
            time = None,
            location = None,
            duration = None,
            ):
        super().__init__(
            description=description,
            time=time,
            location=location,
            duration=duration,
        )

        self.deadline = deadline
        self.event_type = "Task"

    def to_markdown(self):
        # event_type - deadline - 

        info_list = [self.event_type, self.deadline]

        for info in  [self.time, self.location, self.duration]:
            if info:
                info_list.append(info)

        return " - ".join(info_list)


        