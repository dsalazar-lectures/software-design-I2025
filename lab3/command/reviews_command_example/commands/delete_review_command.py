from commands.base_command import Command

class DeleteReviewCommand(Command):
    def __init__(self, system, tutor, index):
        self.system = system
        self.tutor = tutor
        self.index = index

    def execute(self):
        self.system.delete_review(self.tutor, self.index)
