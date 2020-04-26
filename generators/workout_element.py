from . import ContentGenerator

class WorkoutElement(ContentGenerator):
    _template = 'workout_element.html'

    def __init__(self, workout_element):
        super(WorkoutElement, self).__init__()
        self.template_vars = {
            'name': workout_element.name,
            'workout_elements': [WorkoutElement(we) for we in block.workout_elements]
        }
