from commands.base_command import Command

class EditReviewCommand(Command):
    def __init__(self, system, tutor, index, new_review):
        self.system = system
        self.tutor = tutor
        self.index = index
        self.new_review = new_review

    def execute(self):
        self.system.edit_review(self.tutor, self.index, self.new_review)
