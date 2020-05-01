from connection import db

from .workout_element import WorkoutElement

class Exercise(WorkoutElement):
    type = 'EXERCISE'

    def __init__(self, exercise, alternate_detail=None, **kwargs):
        super(Exercise, self).__init__(**kwargs)
        self.name = exercise.get('name')
        self.alternate_detail = alternate_detail
