from . import ContentGenerator

class Exercise(ContentGenerator):
    _template = 'exercise.html'

    def __init__(self, exercise):
        super(Exercise, self).__init__()
        self.template_vars = {
            'type': exercise.type,
            'name': exercise.name,
            'notes': exercise.notes,
            'details': [(k, v) for k,v in exercise.details.items()] if exercise.details is not None else []
        }
