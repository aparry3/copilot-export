from . import ContentGenerator

from .exercise import Exercise
from .superset_header import SupersetHeader


class Superset(ContentGenerator):
    _template = 'superset.html'

    def __init__(self, superset):
        super(Superset, self).__init__()
        self.template_vars = {
            'header': SupersetHeader(superset.scheme, superset.details),
            'type': superset.type,
            'exercises': [Exercise(e) for e in superset.exercises],
            'notes': superset.notes,
            'details': [(k, v) for k,v in superset.details.items()] if superset.details is not None else []
        }
