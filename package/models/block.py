from connection import db

from .workout_element import WorkoutElement

class Block:

    def __init__(self, name=None, workout_elements=None, **kwargs):
        self.name = name
        self.workout_elements = [WorkoutElement.initialize(we) for we in (workout_elements or [])]
