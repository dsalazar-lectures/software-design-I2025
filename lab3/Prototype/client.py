from iTutoria import iTutoria

class client:
    def __init__(self, iTutoria):
        self.iTutoria = iTutoria
        

    def createTutoria(self):
        return self.iTutoria.clone()