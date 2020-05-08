from . import ContentGenerator

from .day import Day

class Week(ContentGenerator):
    _template = 'week.html'

    def __init__(self, week, program, index):
        super(Week, self).__init__()
        self.template_vars = {
            'name': program.name,
            'index': index,
            'days': map(lambda d: Day(d), week.days)
        }
