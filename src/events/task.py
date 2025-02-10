from src.events import Event


class Task(Event):
    event_type = "Առաջադրանք"

    def __init__(self, 
            deadline,
            description,
            *args,
            time = None,
            done = False,
            ):
        super().__init__(
            description=description,
            done=done,
        )

        self.deadline = deadline
        self.time = time

    def to_markdown(self):
        info_list = [self.event_type, self.deadline]

        for info in [self.description]:
            if info:
                info_list.append(info)

        return " - ".join(info_list)

    @classmethod
    def display_input(cls, col):
        col1, col2, col3 = col.columns([3, 1, 2])
        
        deadline = col1.date_input(label="Վերջնաժամկետը (Ամսաթիվ)").strftime("%d.%m.%Y")

        col2.write("######")
        time_on = col2.checkbox("Նշել ժամ")

        time = col3.time_input(label="Վերջնաժամկետը (Ժամ)", 
                                disabled=not time_on).strftime("%H:%M:%S")

        return deadline, time_on, time

    @classmethod
    def create_instance(
        cls,
        description,
        deadline, 
        time_on, 
        time
    ):
        return cls(
            description=description,
            deadline=deadline,
            time=time if time_on else None
        )
    
    def to_dict(self):
        return dict(
            **super().to_dict(),
            deadline=self.deadline,
            time=self.time,
        )