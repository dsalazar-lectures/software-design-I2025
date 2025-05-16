from tests_example.app.i_attachment import IAttachment

class BlenderAttachment(IAttachment):
    def __init__(self):
        self.state = "not blended"

    def use(self, minutes):
        if minutes < 2:
            self.state = "poorly blended"
        elif minutes <= 5:
            self.state = "smooth"
        else:
            self.state = "overblended"
        return f"Blended for {minutes} min"

    def get_state(self):
        return self.state
