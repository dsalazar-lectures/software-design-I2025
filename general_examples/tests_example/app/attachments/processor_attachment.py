from tests_example.app.i_attachment import IAttachment

class ProcessorAttachment(IAttachment):
    def __init__(self):
        self.state = "not processed"

    def use(self, minutes):
        if minutes < 4:
            self.state = "chunks"
        elif minutes <= 8:
            self.state = "processed"
        else:
            self.state = "mush"
        return f"Processed for {minutes} min"

    def get_state(self):
        return self.state
