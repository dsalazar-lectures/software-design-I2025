from tests_example.app.i_cooking_artifact import ICookingArtifact
from tests_example.app.i_attachment import IAttachment

class BlenderArtifact(ICookingArtifact):
    def __init__(self, attachment: IAttachment):
        self.attachment = attachment
        self.state = "idle"

    def cook(self, minutes):
        result = self.attachment.use(minutes)
        self.state = self.attachment.get_state()
        return result

    def get_cooking_state(self):
        return self.state
