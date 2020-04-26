from connection import db

from .exercise import Exercise
from .workout_element import WorkoutElement

class Superset(WorkoutElement):
    type = 'SUPERSET'

    def __init__(self, exercises, **kwargs):
        super(Superset, self).__init__(**kwargs)
        self.exercises = [Exercise(**e) for e in exercises]
