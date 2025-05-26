from iTutoria import iTutoria


class Client:
    def __init__(self, prototype: iTutoria):
        self.prototype = prototype

    def create_tutoria(self):
        return self.prototype.clone()