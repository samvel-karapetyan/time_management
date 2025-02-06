from src.events import Event


class Meeting(Event):
    def __init__(self, 
            date,
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

        self.date = date
        self.event_type = "Meeting"

    def to_markdown(self):
        # event_type - deadline - 

        info_list = [self.event_type, self.date]

        for info in  [self.time, self.location, self.duration]:
            if info:
                info_list.append(info)

        return "- " + " - ".join(info_list)
