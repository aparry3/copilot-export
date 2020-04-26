from models import Exercise, Superset

from . import ContentGenerator
from .exercise import Exercise
from .superset import Superset

generators = {
    'EXERCISE': Exercise,
    'SUPERSET': Superset
}

class Block(ContentGenerator):
    _template = 'block.html'

    def __init__(self, block):
        super(Block, self).__init__()
        self.template_vars = {
            'name': block.name,
            'workout_elements': [generators[we.type](we) for we in block.workout_elements]
        }
