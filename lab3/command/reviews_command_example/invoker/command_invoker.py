class CommandInvoker:
    def __init__(self):
        self.history = []

    def run_command(self, command):
        command.execute()
        self.history.append(command)
