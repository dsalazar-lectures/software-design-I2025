from iTutoria import iTutoria
from abc import abstractmethod
from copy import deepcopy

class presencialTutoria(iTutoria):
   
    def __init__(self, title_tutoring, tutor_id, tutor, subject, date, start_time, description, method, capacity):
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