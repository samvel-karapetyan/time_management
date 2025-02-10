from src.events import Event


class Meeting(Event):
    event_type = "Հանդիպում"
    
    def __init__(self, 
            date,
            description,
            *args,
            time = None,
            location = None,
            duration = None,
            done = False,
            ):
        super().__init__(
            description=description,
            done=done,
        )

        self.date = date
        self.time = time
        self.location = location
        self.duration = duration

    def to_markdown(self):
        info_list = [self.event_type, self.date]

        for info in [self.time, self.description, self.location, self.duration]:
            if info:
                info_list.append(info)

        return "- " + " - ".join(info_list)

    @classmethod
    def display_input(cls, col):
        col1, col2, col3 = col.columns([3, 1, 2])
        date = col1.date_input(label="Ամսաթիվը").strftime("%d.%m.%Y")

        col2.write("######")
        time_on = col2.checkbox("Նշել ժամ")
        
        time = col3.time_input(label="Ժամը", disabled=not time_on).strftime("%H:%M")

        col4, col5 = col.columns([1, 1])
        location = col4.text_input(label="Հանդիպման վայր")
        duration = col5.time_input(label="Տևողությունը", value="00-00").strftime("%H:%M")
        
        return date, time_on, time, location, duration

    @classmethod
    def create_instance(
        cls,
        description,
        date,
        time_on, 
        time,
        location,
        duration,
    ):
        return cls(
            description=description,
            date=date,
            time=time if time_on else None,
            location=location,
            duration=duration,
        )
    
    def to_dict(self):
        return dict(
            **super().to_dict(),
            date=self.date,
            time=self.time,
            location=self.location,
            duration=self.duration,
        )