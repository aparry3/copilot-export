from connection import db

class WorkoutElement:

    @classmethod
    def initialize(cls, workout_element):
        type = workout_element.get('type')
        classes = [c for c in cls.__subclasses__() if type == c.type]
        klass = classes[0] if len(classes) > 0 else cls
        return klass(**workout_element)

    def __init__(self, type=None, notes=None, details=None, scheme=None, alternate=False, **kwargs):
        self.details = details
        self.type = type
        self.notes = notes
        self.scheme = scheme
        self.alternate = alternate
