from . import ContentGenerator

class Exercise(ContentGenerator):
    _template = 'exercise.html'

    def __init__(self, exercise):
        super(Exercise, self).__init__()
        self.template_vars = {
            'type': exercise.type,
            'name': exercise.name,
            'notes': exercise.notes,
            'details': []
        }
