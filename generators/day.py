from . import ContentGenerator
from .block import Block

class Day(ContentGenerator):
    _template = 'day.html'

    def __init__(self, day):
        super(Day, self).__init__()
        self.template_vars = {
            'name': day.name,
            'blocks': [Block(b) for b in day.blocks]
        }
