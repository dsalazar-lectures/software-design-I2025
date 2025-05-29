from commands.base_command import Command

class AddReviewCommand(Command):
    def __init__(self, system, tutor, review):
        self.system = system
        self.tutor = tutor
        self.review = review

    def execute(self):
        self.system.add_review(self.tutor, self.review)
