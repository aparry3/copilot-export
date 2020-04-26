from . import ContentGenerator
from .week import Week

class Program(ContentGenerator):
    _template = 'program.html'

    def __init__(self, program):
        super(Program, self).__init__()
        self.template_vars = {
            'name': program.name,
            'weeks': [Week(w, program, i) for i, w in enumerate(program.weeks)]
        }
