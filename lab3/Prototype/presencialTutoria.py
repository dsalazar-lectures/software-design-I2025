from iTutoria import iTutoria
from copy import deepcopy

class PresencialTutoria(iTutoria):
    def __init__(self, title_tutoring, tutor_id, tutor, subject, date, start_time, description, capacity):
        self.title_tutoring = title_tutoring
        self.tutor_id = tutor_id
        self.tutor = tutor
        self.subject = subject
        self.date = date
        self.start_time = start_time
        self.description = description
        self.method = "Presencial"
        self.capacity = capacity

    def clone(self):
        return deepcopy(self)
    
    def __str__(self):
        return f"Tutoría: {self.title_tutoring}, Tutor: {self.tutor}, Materia: {self.subject}, Método: {self.method}, Capacidad: {self.capacity}"