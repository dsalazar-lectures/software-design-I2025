from tests_example.app.i_attachment import IAttachment

class MixerAttachment(IAttachment):
    def __init__(self):
        self.state = "not mixed"

    def use(self, minutes):
        if minutes < 3:
            self.state = "under mixed"
        else:
            self.state = "well mixed"
        return f"Mixed for {minutes} min"

    def get_state(self):
        return self.state
